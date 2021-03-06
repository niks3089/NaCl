// This file is a part of the IncludeOS unikernel - www.includeos.org
//
// Copyright 2017 IncludeOS AS, Oslo, Norway
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Autogenerated by NaCl

#include <iostream>
#include <net/inet>
#include <net/super_stack.hpp>
#include <net/ip4/cidr.hpp>
#include <os>
#include <profile>
#include <microLB>
static void print_stats(int);
#define STATS_PERIOD 30s
#include <syslogd>

using namespace net;

namespace nacl {
  class Filter {
  public:
    virtual Filter_verdict<IP4> operator()(IP4::IP_packet_ptr pckt, Inet& stack, Conntrack::Entry_ptr ct_entry) = 0;
    virtual ~Filter() {}
  };
}

static microLB::Balancer* nacl_lb_obj = nullptr;
void register_plugin_nacl() {
	INFO("NaCl", "Registering NaCl plugin");

	auto& outside = Super_stack::get(1);
	outside.network_config(IP4::addr{10,0,0,43}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});
	auto& inside = Super_stack::get(2);
	inside.network_config(IP4::addr{10,0,0,44}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});
	auto& uplink = Super_stack::get(0);
	uplink.network_config(IP4::addr{10,0,0,42}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});


	// Load balancers

	inside.tcp().set_MSL(15s);
	nacl_lb_obj = new microLB::Balancer(outside, 80, inside);

	Socket socket_0{ IP4::addr{10,0,0,1}, 6001 };
	nacl_lb_obj->nodes.add_node(inside, socket_0, nacl_lb_obj->get_pool_signal());

	Socket socket_1{ IP4::addr{10,0,0,1}, 6002 };
	nacl_lb_obj->nodes.add_node(inside, socket_1, nacl_lb_obj->get_pool_signal());

	Socket socket_2{ IP4::addr{10,0,0,1}, 6003 };
	nacl_lb_obj->nodes.add_node(inside, socket_2, nacl_lb_obj->get_pool_signal());

	Socket socket_3{ IP4::addr{10,0,0,1}, 6004 };
	nacl_lb_obj->nodes.add_node(inside, socket_3, nacl_lb_obj->get_pool_signal());

	// Load balancer statistics
	Timers::periodic(1s, STATS_PERIOD, print_stats);
	StackSampler::begin();

	/*
	Name: lb
	Layer: tcp

	Clients iface: outside
	Clients port: 80
	Clients wait queue limit: 1000
	Clients session limit: 1000

	Servers iface: inside
	Servers algorithm: round_robin
	Servers pool:

	Node address: IP4::addr{10,0,0,1}
	Node port: 6001

	Node address: IP4::addr{10,0,0,1}
	Node port: 6002

	Node address: IP4::addr{10,0,0,1}
	Node port: 6003

	Node address: IP4::addr{10,0,0,1}
	Node port: 6004
	*/
}

/// statistics ///
#include <timers>
#include <ctime>
using namespace std::chrono;

static std::string now()
{
  auto  tnow = time(0);
  auto* curtime = localtime(&tnow);

  char buff[48];
  int len = strftime(buff, sizeof(buff), "%c", curtime);
  return std::string(buff, len);
}

static void print_heap_info()
{
  static intptr_t last = 0;
  // show information on heap status, to discover leaks etc.
  auto heap_begin = OS::heap_begin();
  auto heap_end   = OS::heap_end();
  auto heap_usage = OS::heap_usage();
  intptr_t heap_size = heap_end - heap_begin;
  auto diff = heap_size - last;
  printf("Heap size %lu Kb  diff %ld (%ld Kb)  usage  %lu kB\n",
        heap_size / 1024, diff, diff / 1024, heap_usage / 1024);
  last = (int32_t) heap_size;
}

template <int N, typename T>
struct rolling_avg {
  std::deque<T> values;

  void push(T value) {
    if (values.size() >= N) values.pop_front();
    values.push_back(value);
  }
  double avg() const {
    double ps = 0.0;
    if (values.empty()) return ps;
    for (auto v : values) ps += v;
    return ps / values.size();
  }
};

void print_stats(int)
{
  static int64_t last = 0;
  const auto& nodes = nacl_lb_obj->nodes;

  auto totals = nodes.total_sessions();
  int  growth = totals - last;  last = totals;

  printf("*** [%s] ***\n", now().c_str());
  printf("Total %ld (%+d) Sess %d Wait %d TO %d - Pool %d C.Att %d Err %d\n",
         totals, growth, nodes.open_sessions(), nacl_lb_obj->wait_queue(),
         nodes.timed_out_sessions(), nodes.pool_size(),
         nodes.pool_connecting(), nacl_lb_obj->connect_throws());

  // node information
  int n = 0;
  for (auto& node : nodes) {
    printf("[%s %s P=%d C=%d]  ", node.address().to_string().c_str(),
        (node.is_active() ? "ONL" : "OFF"),
        node.pool_size(), node.connection_attempts());
    if (++n == 2) { n = 0; printf("\n"); }
  }
  if (n > 0) printf("\n");

  // CPU-usage statistics
  static uint64_t last_total = 0, last_asleep = 0;
  uint64_t tdiff = StackSampler::samples_total() - last_total;
  last_total = StackSampler::samples_total();
  uint64_t adiff = StackSampler::samples_asleep() - last_asleep;
  last_asleep = StackSampler::samples_asleep();

  if (tdiff > 0)
  {
    double asleep = adiff / (double) tdiff;
    static rolling_avg<5, double> asleep_avg;
    asleep_avg.push(asleep);

    printf("CPU usage: %.2f%%  Idle: %.2f%%  Active: %ld Existing: %ld Free: %ld\n",
          (1.0 - asleep) * 100.0, asleep * 100.0,
          Timers::active(), Timers::existing(), Timers::free());
  }
  else {
    printf("CPU usage unavailable due to lack of samples\n");
  }

  // heap statistics
  print_heap_info();
  // stack sampling
  StackSampler::print(3);
}

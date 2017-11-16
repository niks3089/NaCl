#include <iostream>
#include <net/inet4>
#include <net/ip4/cidr.hpp>
#include <plugins/nacl.hpp>

using namespace net;

std::shared_ptr<Conntrack> nacl_ct_obj;

namespace custom_made_classes_from_nacl {

class Ip_Filter : public nacl::Filter {
public:
	Filter_verdict<IP4> operator()(IP4::IP_packet_ptr pckt, Inet<IP4>& stack, Conntrack::Entry_ptr ct_entry) {
		if (not ct_entry) {
return {std::move(pckt), Filter_verdict_type::DROP};
}
std::cout << "CT state: " << static_cast<unsigned>(ct_entry->state) << "\n";
std::cout << "IP saddr: " << pckt->ip_src().to_string() << "\n";
std::cout << "IP daddr: " << pckt->ip_dst().to_string() << "\n";
std::cout << "IP version: " << static_cast<unsigned>(pckt->ip_version()) << "\n";
std::cout << "IP hdrlength: " << static_cast<unsigned>(pckt->ip_header_length()) << "\n";
std::cout << "IP dscp: " << static_cast<unsigned>((uint8_t) pckt->ip_dscp()) << "\n";
std::cout << "IP ecn: " << static_cast<unsigned>((uint8_t) pckt->ip_ecn()) << "\n";
std::cout << "IP length: " << static_cast<unsigned>(pckt->ip_total_length()) << "\n";
std::cout << "IP id: " << static_cast<unsigned>(pckt->ip_id()) << "\n";
std::cout << "IP frag-off: " << static_cast<unsigned>(pckt->ip_frag_offs()) << "\n";
std::cout << "IP ttl: " << static_cast<unsigned>(pckt->ip_ttl()) << "\n";
std::cout << "IP protocol: " << static_cast<unsigned>(pckt->ip_protocol()) << "\n";
std::cout << "IP checksum: " << static_cast<unsigned>(pckt->ip_checksum()) << "\n";
if (pckt->ip_protocol() == Protocol::TCP) {
auto& tcp_pckt = static_cast<tcp::Packet&>(*pckt);

std::cout << "TCP sport: " << static_cast<unsigned>(tcp_pckt.src_port()) << "\n";
std::cout << "TCP dport: " << static_cast<unsigned>(tcp_pckt.dst_port()) << "\n";
std::cout << "TCP sequence: " << static_cast<unsigned>(tcp_pckt.seq()) << "\n";
std::cout << "TCP ackseq: " << static_cast<unsigned>(tcp_pckt.ack()) << "\n";
std::cout << "TCP doff: " << static_cast<unsigned>(tcp_pckt.offset()) << "\n";
std::cout << "TCP reserved: " << static_cast<unsigned>(tcp_pckt.tcp_header().offset_flags.offset_reserved) << "\n";
std::cout << "TCP flags: " << static_cast<unsigned>(tcp_pckt.tcp_header().offset_flags.flags) << "\n";
std::cout << "TCP window: " << static_cast<unsigned>(tcp_pckt.win()) << "\n";
std::cout << "TCP checksum: " << static_cast<unsigned>(tcp_pckt.tcp_checksum()) << "\n";
std::cout << "TCP urgptr: " << static_cast<unsigned>(tcp_pckt.tcp_header().urgent) << "\n";
}
if (pckt->ip_protocol() == Protocol::UDP) {
auto& udp_pckt = static_cast<PacketUDP&>(*pckt);

std::cout << "UDP sport: " << static_cast<unsigned>(udp_pckt.src_port()) << "\n";
std::cout << "UDP dport: " << static_cast<unsigned>(udp_pckt.dst_port()) << "\n";
std::cout << "UDP length: " << static_cast<unsigned>(udp_pckt.length()) << "\n";
std::cout << "UDP checksum: " << static_cast<unsigned>(udp_pckt.checksum()) << "\n";
}
if (pckt->ip_protocol() == Protocol::ICMPv4) {
auto icmp_pckt = icmp4::Packet(std::move(pckt));

std::cout << "ICMP type: " << static_cast<unsigned>(icmp_pckt.type()) << "\n";
pckt = static_unique_ptr_cast<IP4::IP_packet>(icmp_pckt.release());
}
return {std::move(pckt), Filter_verdict_type::ACCEPT};

	}
};

} //< namespace custom_made_classes_from_nacl

void register_plugin_nacl() {
	INFO("NaCl", "Registering NaCl plugin");

	auto& eth0 = Inet4::stack<0>();
	eth0.network_config(IP4::addr{10,0,0,45}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});

	custom_made_classes_from_nacl::Ip_Filter ip_filter;

	eth0.ip_obj().prerouting_chain().chain.push_back(ip_filter);

	// Ct

	nacl_ct_obj = std::make_shared<Conntrack>();

	INFO("NaCl", "Enabling Conntrack on eth0");
	eth0.enable_conntrack(nacl_ct_obj);
}
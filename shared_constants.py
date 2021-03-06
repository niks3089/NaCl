# This file is a part of the IncludeOS unikernel - www.includeos.org
#
# Copyright 2017 IncludeOS AS, Oslo, Norway
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# Languages that NaCl can be transpiled to

CPP = "cpp"

valid_languages = [
	CPP
]

# Operators

GREATER_THAN_OR_EQUAL 	= ">="
LESS_THAN_OR_EQUAL 		= "<="
GREATER_THAN 			= ">"
LESS_THAN 				= "<"
EQUALS 					= "=="
NOT_EQUALS 				= "!="

NOT = "!"

IN = "in"

AND = "and"
OR 	= "or"

ARROW 	= "->"
DOT 	= "."

PARENTHESIS_START 	= "("
PARENTHESIS_END 	= ")"

# Other

MASK_LIMIT = 32
BYTE_LIMIT = 255

IS_LIST = True

TRUE 	= "true"
FALSE 	= "false"

# Available NaCl types
TYPE_IFACE 			= "iface"
TYPE_VLAN 			= "vlan"
TYPE_GATEWAY 		= "gateway"
TYPE_CONNTRACK 		= "conntrack"
TYPE_LOAD_BALANCER 	= "load_balancer"
TYPE_SYSLOG 		= "syslog"
TYPE_FILTER 		= "filter"
TYPE_REWRITE 		= "rewrite"
TYPE_NAT 			= "nat"

valid_nacl_types = [
	TYPE_IFACE,
	TYPE_VLAN,
	TYPE_GATEWAY,
	TYPE_CONNTRACK,
	TYPE_LOAD_BALANCER,
	TYPE_SYSLOG,
	TYPE_FILTER,
	TYPE_REWRITE,
	TYPE_NAT
]

BASE_TYPE_FUNCTION 		= "function"
BASE_TYPE_UNTYPED_INIT 	= "untyped_init"
BASE_TYPE_TYPED_INIT 	= "typed_init"

# ---- Iface keys ----

IFACE_KEY_ADDRESS 		= "address"
IFACE_KEY_NETMASK 		= "netmask"
IFACE_KEY_GATEWAY		= "gateway"
IFACE_KEY_DNS 			= "dns"
IFACE_KEY_INDEX 		= "index"
IFACE_KEY_VLAN 			= "vlan"
IFACE_KEY_MASQUERADE 	= "masquerade"
IFACE_KEY_CONFIG 		= "config"

IFACE_KEY_PREROUTING 	= "prerouting"
IFACE_KEY_INPUT 		= "input"
IFACE_KEY_OUTPUT 		= "output"
IFACE_KEY_POSTROUTING 	= "postrouting"

chains = [
	IFACE_KEY_PREROUTING,
	IFACE_KEY_INPUT,
	IFACE_KEY_OUTPUT,
	IFACE_KEY_POSTROUTING
]

predefined_iface_keys = [
	IFACE_KEY_ADDRESS,
	IFACE_KEY_NETMASK,
	IFACE_KEY_GATEWAY,
	IFACE_KEY_DNS,
	IFACE_KEY_INDEX,
	IFACE_KEY_VLAN,
	IFACE_KEY_MASQUERADE,
	IFACE_KEY_CONFIG
]
predefined_iface_keys.extend(chains)

DHCP_CONFIG 			= "dhcp"
DHCP_FALLBACK_CONFIG 	= "dhcp-with-fallback"
STATIC_CONFIG 			= "static"

predefined_config_types = [
	DHCP_CONFIG,
	DHCP_FALLBACK_CONFIG,
	STATIC_CONFIG
]

# ---- Vlan keys ----

VLAN_KEY_ADDRESS 	= IFACE_KEY_ADDRESS
VLAN_KEY_NETMASK 	= IFACE_KEY_NETMASK
VLAN_KEY_GATEWAY 	= IFACE_KEY_GATEWAY
VLAN_KEY_DNS 		= IFACE_KEY_DNS
VLAN_KEY_INDEX 		= IFACE_KEY_INDEX

predefined_vlan_keys = [
	VLAN_KEY_ADDRESS,
	VLAN_KEY_NETMASK,
	VLAN_KEY_GATEWAY,
	VLAN_KEY_INDEX
]

# ---- Gateway keys ----

GATEWAY_KEY_SEND_TIME_EXCEEDED 	= "send_time_exceeded"
GATEWAY_KEY_FORWARD 			= "forward"

GATEWAY_KEY_HOST 	= "host"
GATEWAY_KEY_NET 	= "net"
GATEWAY_KEY_NETMASK = "netmask"
GATEWAY_KEY_NEXTHOP = "nexthop"
GATEWAY_KEY_IFACE 	= "iface"
GATEWAY_KEY_COST 	= "cost"

# Valid keys for Gateway routes
predefined_gateway_route_keys = [
	GATEWAY_KEY_HOST,
	GATEWAY_KEY_NET,
	GATEWAY_KEY_NETMASK,
	GATEWAY_KEY_NEXTHOP,
	GATEWAY_KEY_IFACE,
	GATEWAY_KEY_COST
]

# Valid Gateway keys for members that are not objects (routes)
predefined_gateway_keys = [
	GATEWAY_KEY_SEND_TIME_EXCEEDED,
	GATEWAY_KEY_FORWARD
]

# ---- General ----

AUTO = "auto"

TCP 	= "tcp"
UDP 	= "udp"
IP 		= "ip"
ICMP 	= "icmp"
CT 		= "ct"

# ---- Conntrack keys ----

CONNTRACK_KEY_LIMIT 	= "limit"
CONNTRACK_KEY_RESERVE 	= "reserve"
CONNTRACK_KEY_TIMEOUT 	= "timeout"

predefined_conntrack_keys = [
	CONNTRACK_KEY_LIMIT,
	CONNTRACK_KEY_RESERVE,
	CONNTRACK_KEY_TIMEOUT
]

CONNTRACK_TIMEOUT_KEY_ESTABLISHED = "established"
CONNTRACK_TIMEOUT_KEY_UNCONFIRMED = "unconfirmed"
CONNTRACK_TIMEOUT_KEY_CONFIRMED = "confirmed"

predefined_conntrack_timeout_keys = [
	CONNTRACK_TIMEOUT_KEY_ESTABLISHED,
	CONNTRACK_TIMEOUT_KEY_UNCONFIRMED,
	CONNTRACK_TIMEOUT_KEY_CONFIRMED
]

predefined_conntrack_timeout_inner_keys = [
	TCP,
	UDP,
	ICMP
]

# ---- Load_balancer keys ----

LB_KEY_LAYER = "layer"
LB_KEY_CLIENTS = "clients"
LB_KEY_SERVERS = "servers"

predefined_lb_keys = [
	LB_KEY_LAYER,
	LB_KEY_CLIENTS,
	LB_KEY_SERVERS
]

LB_KEY_IFACE = "iface"
LB_KEY_PORT = "port"

LB_CLIENTS_KEY_WAIT_QUEUE_LIMIT = "wait_queue_limit"
LB_CLIENTS_KEY_SESSION_LIMIT = "session_limit"

predefined_lb_clients_keys = [
	LB_KEY_IFACE,
	LB_KEY_PORT,
	LB_CLIENTS_KEY_WAIT_QUEUE_LIMIT,
	LB_CLIENTS_KEY_SESSION_LIMIT
]

LB_SERVERS_KEY_ALGORITHM = "algorithm"
LB_SERVERS_KEY_POOL = "pool"

predefined_lb_servers_keys = [
	LB_KEY_IFACE,
	LB_SERVERS_KEY_ALGORITHM,
	LB_SERVERS_KEY_POOL
]

LB_NODE_KEY_ADDRESS = "address"

predefined_lb_node_keys = [
	LB_NODE_KEY_ADDRESS,
	LB_KEY_PORT
]

# Load balancer algorithms
# Note: Only round_robin is supported in microLB for now (the algo/algorithm field is ignored)
ROUND_ROBIN = "round_robin"
# FEWEST_CONNECTIONS = "fewest_connections"
valid_lb_servers_algos = [
	ROUND_ROBIN
	# FEWEST_CONNECTIONS
]

INCLUDEOS_ROUND_ROBIN = ROUND_ROBIN

# Load balancer layers

valid_lb_layers = [
	TCP
]

# ---- Syslog keys ----

SYSLOG_KEY_ADDRESS 	= IFACE_KEY_ADDRESS
SYSLOG_KEY_PORT 	= LB_KEY_PORT

predefined_syslog_keys = [
	SYSLOG_KEY_ADDRESS,
	SYSLOG_KEY_PORT
]

# ---- Syslog severity levels ----

EMERG = "emerg"
ALERT = "alert"
CRIT = "crit"
ERR = "err"
WARNING = "warning"
NOTICE = "notice"
INFO = "info"
DEBUG = "debug"

# ---- IncludeOS syslog severity levels

INCLUDEOS_SYSLOG_SEVERITY_EMERG = "LOG_EMERG"
INCLUDEOS_SYSLOG_SEVERITY_ALERT = "LOG_ALERT"
INCLUDEOS_SYSLOG_SEVERITY_CRIT = "LOG_CRIT"
INCLUDEOS_SYSLOG_SEVERITY_ERR = "LOG_ERR"
INCLUDEOS_SYSLOG_SEVERITY_WARNING = "LOG_WARNING"
INCLUDEOS_SYSLOG_SEVERITY_NOTICE = "LOG_NOTICE"
INCLUDEOS_SYSLOG_SEVERITY_INFO = "LOG_INFO"
INCLUDEOS_SYSLOG_SEVERITY_DEBUG = "LOG_DEBUG"

# ---- General ----

# Constants related to the log action (std::cout)
TO_UNSIGNED = "TO_UNSIGNED"
TO_STRING = "TO_STRING"

INCLUDEOS_NAT_OBJ_NAME 	= "nacl_natty_obj"
INCLUDEOS_ROUTER_OBJ_NAME = "nacl_router_obj"

# Pckt variable names, used in transpiled text/code
TCP_PCKT 		= "tcp_pckt"
UDP_PCKT 		= "udp_pckt"
IP_PCKT 		= "pckt"
ICMP_PCKT 		= "icmp_pckt"

pckt_names = {
	TCP: 	TCP_PCKT,
	UDP: 	UDP_PCKT,
	IP: 	IP_PCKT,
	ICMP: 	ICMP_PCKT
}

# IncludeOS packet classes
INCLUDEOS_TCP_PCKT_CLASS 	= "tcp::Packet"
INCLUDEOS_UDP_PCKT_CLASS 	= "PacketUDP"
INCLUDEOS_ICMP_PCKT_CLASS 	= "icmp4::Packet"
INCLUDEOS_IP_PCKT_CLASS 	= "IP4::IP_packet"

cpp_pckt_classes = {
	TCP: 	INCLUDEOS_TCP_PCKT_CLASS,
	UDP: 	INCLUDEOS_UDP_PCKT_CLASS,
	ICMP: 	INCLUDEOS_ICMP_PCKT_CLASS,
	IP: 	INCLUDEOS_IP_PCKT_CLASS
}

INCLUDEOS_ICMP_RELEASE_METHOD = "release()"

INCLUDEOS_DEREFERENCE_OP = "*"
INCLUDEOS_REFERENCE_OP = "&"

# IncludeOS class names
INCLUDEOS_IP4_ADDR_CLASS = "IP4::addr"
INCLUDEOS_IP4_CIDR_CLASS = "ip4::Cidr"

# NaCl verdicts/actions
ACCEPT 	= 'accept'
DROP 	= 'drop'
LOG 	= 'log'
SYSLOG 	= 'syslog'
SNAT 	= 'snat'
DNAT 	= 'dnat'

valid_default_filter_verdicts = [
	ACCEPT,
	DROP
]

MASQUERADE = "masquerade"

# IncludeOS (C++) Filter return values
INCLUDEOS_VERDICT_TYPE = "Filter_verdict_type::"
INCLUDEOS_VERDICT_TYPE_DROP = INCLUDEOS_VERDICT_TYPE + "DROP"
INCLUDEOS_VERDICT_TYPE_ACCEPT = INCLUDEOS_VERDICT_TYPE + "ACCEPT"
NULLPTR = "nullptr"

INCLUDEOS_DROP = "return {" + NULLPTR + ", " + INCLUDEOS_VERDICT_TYPE_DROP + "};\n"

def INCLUDEOS_ACCEPT(subtype):
	if subtype.lower() != ICMP:
		return "return {std::move(" + IP_PCKT + "), " + INCLUDEOS_VERDICT_TYPE_ACCEPT + "};\n"
	else:
		return "return {" + ICMP_PCKT + DOT + INCLUDEOS_ICMP_RELEASE_METHOD + ", " + INCLUDEOS_VERDICT_TYPE_ACCEPT + "};\n"

INCLUDEOS_CT_ENTRY = "ct_entry"

SSH 	= "ssh"
DNS 	= "dns"
HTTP 	= "http"
HTTPS 	= "https"

# TCP, UDP and IP packet properties (NaCl)

SPORT 		= "sport"
DPORT 		= "dport"
SEQUENCE 	= "sequence"
ACKSEQ 		= "ackseq"
DOFF 		= "doff"
RESERVED 	= "reserved"
FLAGS 		= "flags"
WINDOW 		= "window"
CHECKSUM 	= "checksum"
URGPTR 		= "urgptr"
LENGTH 		= "length"

VERSION 	= "version"
HDRLENGTH 	= "hdrlength"
DSCP 		= "dscp"
ECN 		= "ecn"
ID 			= "id"
FRAG_OFF 	= "frag-off"
TTL 		= "ttl"
PROTOCOL 	= "protocol"
SADDR 		= "saddr"
DADDR 		= "daddr"

# TCP, UDP and IP packet properties/methods in IncludeOS (C++)

INCLUDEOS_SPORT = "src_port()"
INCLUDEOS_DPORT = "dst_port()"

INCLUDEOS_TCP_SEQUENCE 	= "seq()"
INCLUDEOS_TCP_ACKSEQ 	= "ack()"
INCLUDEOS_TCP_DOFF 		= "offset()"
INCLUDEOS_TCP_RESERVED 	= "tcp_header().offset_flags.offset_reserved"
INCLUDEOS_TCP_FLAGS 	= "tcp_header().offset_flags.flags"
INCLUDEOS_TCP_WINDOW 	= "win()"
INCLUDEOS_TCP_CHECKSUM 	= "tcp_checksum()"
INCLUDEOS_TCP_URGPTR 	= "tcp_header().urgent"

INCLUDEOS_UDP_CHECKSUM 	= "checksum()"
INCLUDEOS_UDP_LENGTH 	= "length()"

INCLUDEOS_IP_VERSION 	= "ip_version()"
INCLUDEOS_IP_HDRLENGTH 	= "ip_header_length()"
INCLUDEOS_IP_DSCP 		= "ip_dscp()"
INCLUDEOS_IP_ECN 		= "ip_ecn()"
INCLUDEOS_IP_LENGTH 	= "ip_total_length()"
INCLUDEOS_IP_ID 		= "ip_id()"
INCLUDEOS_IP_FRAG_OFF 	= "ip_frag_offs()"
INCLUDEOS_IP_TTL 		= "ip_ttl()"
INCLUDEOS_IP_PROTOCOL 	= "ip_protocol()"
INCLUDEOS_IP_CHECKSUM 	= "ip_checksum()"
INCLUDEOS_IP_SADDR 		= "ip_src()"
INCLUDEOS_IP_DADDR 		= "ip_dst()"

# ICMP and CT properties (NaCl)

TYPE 	= "type"
STATE 	= "state"

# ICMP and CT properties/methods in IncludeOS (C++)

INCLUDEOS_ICMP_TYPE = "type()"
INCLUDEOS_CT_STATE 	= "state"

# Protocols in IncludeOS (C++)

INCLUDEOS_PROTO_TCP 	= "Protocol::TCP"
INCLUDEOS_PROTO_UDP 	= "Protocol::UDP"
INCLUDEOS_PROTO_ICMP 	= "Protocol::ICMPv4"
INCLUDEOS_PROTO_IP4		= "Protocol::IPv4"
# INCLUDEOS_PROTO_IP6 	= "Protocol::IPv6"

# IncludeOS ICMP packet method to access IP part of packet

INCLUDEOS_ICMP_IP_ACCESS_METHOD = "ip()"

# ICMP types (NaCl)

ECHO_REPLY 			= "echo-reply"
DEST_UNREACHABLE 	= "destination-unreachable"
REDIRECT 			= "redirect"
ECHO_REQUEST 		= "echo-request"
TIME_EXCEEDED 		= "time-exceeded"
PARAMETER_PROBLEM 	= "parameter-problem"
TIMESTAMP_REQUEST 	= "timestamp-request"
TIMESTAMP_REPLY 	= "timestamp-reply"

# ICMP types in IncludeOS (C++)

ICMP_TYPE_NS = "icmp4::Type::"
INCLUDEOS_TYPE_ECHO_REPLY 			= ICMP_TYPE_NS + "ECHO_REPLY"
INCLUDEOS_TYPE_DEST_UNREACHABLE 	= ICMP_TYPE_NS + "DEST_UNREACHABLE"
INCLUDEOS_TYPE_REDIRECT 			= ICMP_TYPE_NS + "REDIRECT"
INCLUDEOS_TYPE_ECHO_REQUEST 		= ICMP_TYPE_NS + "ECHO"
INCLUDEOS_TYPE_TIME_EXCEEDED		= ICMP_TYPE_NS + "TIME_EXCEEDED"
INCLUDEOS_TYPE_PARAMETER_PROBLEM 	= ICMP_TYPE_NS + "PARAMETER_PROBLEM"
INCLUDEOS_TYPE_TIMESTAMP_REQUEST 	= ICMP_TYPE_NS + "TIMESTAMP"
INCLUDEOS_TYPE_TIMESTAMP_REPLY 		= ICMP_TYPE_NS + "TIMESTAMP_REPLY"

# CT states (NaCl)

ESTABLISHED = "established"
NEW 		= "new"
RELATED 	= "related"
INVALID 	= "invalid"

# CT states in IncludeOS (C++)

CT_STATE_NS = "Conntrack::State::"
INCLUDEOS_STATE_ESTABLISHED	= CT_STATE_NS + "ESTABLISHED"
INCLUDEOS_STATE_NEW 		= CT_STATE_NS + "NEW"
INCLUDEOS_STATE_RELATED 	= CT_STATE_NS + "RELATED"
INCLUDEOS_STATE_INVALID 	= CT_STATE_NS + "INVALID"

INCLUDEOS_CT_ENTRY_NULLPTR_CHECK = "if (not " + INCLUDEOS_CT_ENTRY + ") {\n" + INCLUDEOS_DROP + "}\n"

# TCP flags (NaCl)

FIN = "fin"
SYN = "syn"
RST = "rst"
PSH = "psh"
ACK = "ack"
URG = "urg"
CWR = "cwr"
# Also available in IncludeOS:
ECE = "ece"
NS 	= "ns"

# TCP flags in IncludeOS (C++)

TCP_FLAG_NS = "tcp::Flag::"
INCLUDEOS_FLAG_FIN 	= TCP_FLAG_NS + "FIN"
INCLUDEOS_FLAG_SYN 	= TCP_FLAG_NS + "SYN"
INCLUDEOS_FLAG_RST 	= TCP_FLAG_NS + "RST"
INCLUDEOS_FLAG_PSH 	= TCP_FLAG_NS + "PSH"
INCLUDEOS_FLAG_ACK 	= TCP_FLAG_NS + "ACK"
INCLUDEOS_FLAG_URG 	= TCP_FLAG_NS + "URG"
INCLUDEOS_FLAG_CWR 	= TCP_FLAG_NS + "CWR"
INCLUDEOS_FLAG_ECE 	= TCP_FLAG_NS + "ECE"
INCLUDEOS_FLAG_NS 	= TCP_FLAG_NS + "NS"

# All elements (Iface, Filter, Port, etc.) that have been identified in the NaCl file
# (by the visitor) are placed here because each language template (f.ex. cpp_template.py)
# needs to access the elements when resolving a variable name f.ex.
# Dictionary where key is the name of the Element and the value is the Element object or
# subtype of this
elements = {}

# Available/legal object types for given subtypes (tcp, udp, icmp, ip)
legal_obj_types = {
	TCP: 	[TCP, IP, CT],
	UDP: 	[UDP, IP, CT],
	ICMP: 	[ICMP, IP, CT],
	IP: 	[IP, CT]
}

legal_nested_subtypes = {
	TCP:	[IP, TCP],
	UDP:	[IP, UDP],
	ICMP: 	[IP, ICMP],
	IP: 	[IP, TCP, UDP, ICMP]
}

# TODO
# To be implemented in IncludeOS:

OIF 	= "oif"
OIFNAME = "oifname"
IIF 	= "iif"
IIFNAME = "iifname"

INCLUDEOS_OIF 		= "stack2.oif()"
INCLUDEOS_OIFNAME 	= "stack2.oifname()"
INCLUDEOS_IIF 		= "stack.iif()"
INCLUDEOS_IIFNAME 	= "stack.iifname()"

# Built-in/predefined constants that can be used as values in NaCl
predefined_values_cpp = {

	OIF:		INCLUDEOS_OIF,
	OIFNAME:	INCLUDEOS_OIFNAME,
	IIF:		INCLUDEOS_IIF,
	IIFNAME:	INCLUDEOS_IIFNAME,

	# TCP flags
	
	FIN: 	INCLUDEOS_FLAG_FIN,
	SYN: 	INCLUDEOS_FLAG_SYN,
	RST: 	INCLUDEOS_FLAG_RST,
	PSH: 	INCLUDEOS_FLAG_PSH,
	ACK: 	INCLUDEOS_FLAG_ACK,
	URG: 	INCLUDEOS_FLAG_URG,
	CWR: 	INCLUDEOS_FLAG_CWR,
	# Also available in IncludeOS:
	ECE:	INCLUDEOS_FLAG_ECE,
	NS: 	INCLUDEOS_FLAG_NS,

	# Named ports

	SSH: 	22,
	DNS: 	53,
	HTTP: 	80,
	HTTPS: 	443,

	# IP protocols
	
	TCP: 	INCLUDEOS_PROTO_TCP,
	UDP: 	INCLUDEOS_PROTO_UDP,
	ICMP: 	INCLUDEOS_PROTO_ICMP,
	IP: 	INCLUDEOS_PROTO_IP4,

	# ICMP types

	ECHO_REPLY: 		INCLUDEOS_TYPE_ECHO_REPLY,
	DEST_UNREACHABLE: 	INCLUDEOS_TYPE_DEST_UNREACHABLE,
	REDIRECT: 			INCLUDEOS_TYPE_REDIRECT,
	ECHO_REQUEST: 		INCLUDEOS_TYPE_ECHO_REQUEST,
	TIME_EXCEEDED: 		INCLUDEOS_TYPE_TIME_EXCEEDED,
	PARAMETER_PROBLEM: 	INCLUDEOS_TYPE_PARAMETER_PROBLEM,
	TIMESTAMP_REQUEST: 	INCLUDEOS_TYPE_TIMESTAMP_REQUEST,
	TIMESTAMP_REPLY: 	INCLUDEOS_TYPE_TIMESTAMP_REPLY,

	# CT states
	
	ESTABLISHED: 	INCLUDEOS_STATE_ESTABLISHED,
	NEW: 			INCLUDEOS_STATE_NEW,
	RELATED: 		INCLUDEOS_STATE_RELATED,
	INVALID: 		INCLUDEOS_STATE_INVALID,

	# TCP Load balancer
	ROUND_ROBIN: 	INCLUDEOS_ROUND_ROBIN
}

class Tcp:
	def __init__(self):
		self.properties = [
			SPORT,
			DPORT,
			SEQUENCE,
			ACKSEQ,
			DOFF,
			RESERVED,
			FLAGS,
			WINDOW,
			CHECKSUM,
			URGPTR
		]

		self.cpp_properties = {
			SPORT: 		INCLUDEOS_SPORT,
			DPORT: 		INCLUDEOS_DPORT,
			SEQUENCE: 	INCLUDEOS_TCP_SEQUENCE,
			ACKSEQ:		INCLUDEOS_TCP_ACKSEQ,
			DOFF: 		INCLUDEOS_TCP_DOFF,
			RESERVED: 	INCLUDEOS_TCP_RESERVED,
			FLAGS: 		INCLUDEOS_TCP_FLAGS,
			WINDOW: 	INCLUDEOS_TCP_WINDOW,
			CHECKSUM: 	INCLUDEOS_TCP_CHECKSUM,
			URGPTR: 	INCLUDEOS_TCP_URGPTR
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop, ctx):
		if language == CPP:
			return self.resolve_method_cpp(prop, ctx)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in TCP")
		return self.cpp_properties[prop]

	def get_cout_convert_to_type_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in TCP")
		return TO_UNSIGNED

class Udp:
	def __init__(self):
		self.properties = [
			SPORT,
			DPORT,
			LENGTH,
			CHECKSUM
		]

		self.cpp_properties = {
			SPORT: 		INCLUDEOS_SPORT,
			DPORT: 		INCLUDEOS_DPORT,
			LENGTH: 	INCLUDEOS_UDP_LENGTH,
			CHECKSUM: 	INCLUDEOS_UDP_CHECKSUM
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop, ctx):
		if language == CPP:
			return self.resolve_method_cpp(prop, ctx)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in UDP")
		return self.cpp_properties[prop]

	def get_cout_convert_to_type_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in UDP")
		return TO_UNSIGNED

class Ip:
	def __init__(self):
		self.properties = [
			VERSION,
			HDRLENGTH,
			DSCP,
			ECN,
			LENGTH,
			ID,
			FRAG_OFF,
			TTL,
			PROTOCOL,
			CHECKSUM,
			SADDR,
			DADDR
		]

		self.cpp_properties = {
			VERSION: 	INCLUDEOS_IP_VERSION,
			HDRLENGTH:	INCLUDEOS_IP_HDRLENGTH,
			DSCP: 		INCLUDEOS_IP_DSCP,
			ECN: 		INCLUDEOS_IP_ECN,
			LENGTH: 	INCLUDEOS_IP_LENGTH,
			ID: 		INCLUDEOS_IP_ID,
			FRAG_OFF: 	INCLUDEOS_IP_FRAG_OFF,
			TTL: 		INCLUDEOS_IP_TTL,
			PROTOCOL: 	INCLUDEOS_IP_PROTOCOL,
			CHECKSUM: 	INCLUDEOS_IP_CHECKSUM,
			SADDR: 		INCLUDEOS_IP_SADDR,
			DADDR: 		INCLUDEOS_IP_DADDR
		}

		# ?
		self.cpp_protocols = {
			TCP: 	INCLUDEOS_PROTO_TCP,
			UDP:	INCLUDEOS_PROTO_UDP,
			ICMP: 	INCLUDEOS_PROTO_ICMP,
			IP: 	INCLUDEOS_PROTO_IP4
		}

		self.cpp_cout_conversion_types = {
			VERSION: 	TO_UNSIGNED,
			HDRLENGTH:	TO_UNSIGNED,
			DSCP: 		TO_UNSIGNED,
			ECN: 		TO_UNSIGNED,
			LENGTH: 	TO_UNSIGNED,
			ID: 		TO_UNSIGNED,
			FRAG_OFF: 	TO_UNSIGNED,
			TTL: 		TO_UNSIGNED,
			PROTOCOL: 	TO_UNSIGNED,
			CHECKSUM: 	TO_UNSIGNED,
			SADDR: 		TO_STRING,
			DADDR: 		TO_STRING
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop, ctx):
		if language == CPP:
			return self.resolve_method_cpp(prop, ctx)

	def resolve_protocol(self, language, nacl_proto, ctx):
		if language == CPP:
			return self.resolve_protocol_cpp(nacl_proto, ctx)

	def resolve_cast_cpp(self, prop):
		if prop != DSCP and prop != ECN:
			return ""
		return "(uint8_t)"

	def resolve_method_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in IP")
		return self.cpp_properties[prop]

	# Returns the correct C++/IncludeOS IP protocol constant based on the
	# incoming (NaCl) protocol (tcp, udp, icmp)
	def resolve_protocol_cpp(self, nacl_proto, ctx):
		proto = nacl_proto.lower()
		if proto not in self.cpp_protocols:
			sys.exit("line " + get_line_and_column(ctx) + " No protocol named " + nacl_proto + " exists")
		return self.cpp_protocols[proto]

	def get_cout_convert_to_type_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in IP")
		return self.cpp_cout_conversion_types[prop]

class Icmp:
	def __init__(self):
		self.properties = [
			TYPE
		]

		self.cpp_properties = {
			TYPE: INCLUDEOS_ICMP_TYPE
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop, ctx):
		if language == CPP:
			return self.resolve_method_cpp(prop, ctx)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in ICMP")
		return self.cpp_properties[prop]

	def get_cout_convert_to_type_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in ICMP")
		return TO_UNSIGNED

class Ct:
	def __init__(self):
		self.properties = [
			STATE
		]

		self.cpp_properties = {
			STATE: INCLUDEOS_CT_STATE
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop, ctx):
		if language == CPP:
			return self.resolve_method_cpp(prop, ctx)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in CT")
		return self.cpp_properties[prop]

	def get_cout_convert_to_type_cpp(self, prop, ctx):
		if prop not in self.properties:
			sys.exit("line " + get_line_and_column(ctx) + " No property named " + prop + " in TCP")
		return TO_UNSIGNED

Tcp_obj = Tcp()
Udp_obj = Udp()
Ip_obj = Ip()
Icmp_obj = Icmp()
Ct_obj = Ct()

proto_objects = {
	TCP: 	Tcp_obj,
	UDP: 	Udp_obj,
	IP: 	Ip_obj,
	ICMP: 	Icmp_obj,
	CT: 	Ct_obj
}

def get_line_and_column(ctx):
	return str(ctx.start.line) + ":" + str(ctx.start.column)
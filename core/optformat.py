import os, sys
from termcolor import cprint, colored

from core.packet import Packet
from core.segment import *
from core.frame import NetworkFrame
from core.config import Config, Babyshark, PCAP


class ProtoOutput(object):
    def __write_ipv4_normal_output__(self, packet_data):
     
        pk = Packet()
        cfg = Config()
        esp = Babyshark()

        try:
            (packet_version, packet_header_length, packet_ttl, packet_protocol, packet_source, packet_destination,
            packet_data) = pk.handle_ipv4_packet(packet_data)

            esp.print_babyshark_message("IPv4 Packet Contents {}".format(cfg.ESPI_ASCII_DOWN_ARROW))
            esp.print_babyshark_notab("\t <-- Protocol: {}, Source: {}, Destination: {}".format(packet_protocol, packet_source, packet_destination))

        except: pass

    def __write_ipv4_verbose_output__(self, packet_data):
        pk = Packet()
        cfg = Config()
        esp = Babyshark()

        try:
            (packet_version, packet_header_length, packet_ttl, packet_protocol, packet_source, packet_destination,
            packet_data) = pk.handle_ipv4_packet(packet_data)

            esp.print_babyshark_message("IPv4 Packet Contents {}".format(cfg.ESPI_ASCII_DOWN_ARROW))
            esp.print_babyshark_notab("Version: " + str(packet_version) + ", TTL: " + str(packet_ttl) + ", Header: " + str(packet_header_length))
            esp.print_babyshark_notab("\tProtocol: " + str(packet_protocol) + ", Source: " + str(packet_source) + ", Destination: " + str(packet_destination))
        except:
            pass

    def __write_icmp_normal_output__(self, packet_data):
        pk = Packet()
        cfg = Config()
        esp = Babyshark()

        try:
            icmp_packet_type, icmp_packet_code, icmp_check_summation, icmp_packet_data = pk.handle_icmp_packet(packet_data)

            esp.print_babyshark_message("ICMP Contents {}".format(cfg.ESPI_ASCII_DOWN_ARROW))
            esp.print_babyshark_notab("ICMP Checksum: {}, ICMP Type: {}, ICMP Code: {}".format(icmp_check_summation, icmp_packet_type,
            icmp_packet_code))
        except: pass

    def __write_icmp_verbose_output__(self, packet_data):
      
        pk = Packet()
        cfg = Config()
        esp = Babyshark()
        try:
            icmp_packet_type, icmp_packet_code, icmp_check_summation, icmp_packet_data = pk.handle_icmp_packet(packet_data)

            esp.print_babyshark_message("ICMP Contents {}".format(cfg.ESPI_ASCII_DOWN_ARROW))
            esp.print_babyshark_notab("ICMP Checksum: {}, ICMP Type: {}, ICMP Code: {}".format(icmp_check_summation, icmp_packet_type,
            icmp_packet_code))
            esp.print_babyshark_notab("\t\tICMP Data: {}".format(icmp_packet_data))
        except: pass

class SegmentOutput(object):
    def __write_tcp_segment_normal_output__(self, segment_data):
        pk = Packet()
        cfg = Config()
        esp = Babyshark()

        try:
            (segment_source_port, segment_destination_port, segment_sequence, segment_acknowledgment, __urg_flag__, __ack_flag__,
            __psh_flag__, __rst_flag__, __syn_flag__, __fin_flag__) = pk.unpack_packet(cfg.ESPI_TCP_STRUCT_SEGMENT_FORMAT, segment_data, 24)

            esp.print_babyshark_noprefix("\tTCP Segment {}".format(cfg.ESPI_ASCII_DOWN_ARROW))
            esp.print_babyshark_notab("\t\tSource Port # {}, Destination Port # {}, [Sequence] {}".format(segment_source_port,
            segment_destination_port, segment_sequence))
        except: pass


    def __write_tcp_segment_verbose_output__(self, segment_data):
        pk = Packet()
        cfg = Config()
        esp = Babyshark()

        try:
            (segment_source_port, segment_destination_port, segment_sequence, segment_acknowledgment, __urg_flag__, __ack_flag__,
            __psh_flag__, __rst_flag__, __syn_flag__, __fin_flag__) = pk.unpack_packet(cfg.ESPI_TCP_STRUCT_SEGMENT_FORMAT, segment_data, 24)

            esp.print_babyshark_noprefix("\tTCP Segment {}".format(cfg.ESPI_ASCII_DOWN_ARROW))
            esp.print_babyshark_notab("\t\tSource Port # {}, Destination Port # {}, [Sequence] {}".format(segment_source_port,
            segment_destination_port, segment_sequence))
            # Write Flags
            esp.print_babyshark_noprefix("\t\tTCP Segment Flags")
            esp.print_babyshark_notab("\t\tFLAG_URG: {}, FLAG_ACK: {}, FLAG_PSH: {}, FLAG_RST: {}".format(__urg_flag__,
            __ack_flag__, __psh_flag__, __rst_flag__))
            # SYN/FIN
            esp.print_babyshark_notab("\t\tFLAG_SYN: {}, FLAG_FIN: {}".format(__syn_flag__, __fin_flag__))
        except: pass

    def __write_udp_segment_normal_verbose_output__(self, segment_data):
        seg = Segment()
        cfg = Config()
        esp = Babyshark()

        try:
            segment_source_port, segment_destination_port, segment_length, segdata = seg.load_udp_segment(segment_data)
            esp.print_babyshark_noprefix("\tUDP Segment (len={}) {}".format(segment_length, cfg.ESPI_ASCII_DOWN_ARROW))
            esp.print_babyshark_notab("\t\tSource Port: {}, Target Port: {}".format(segment_source_port, segment_destination_port))
        except: pass

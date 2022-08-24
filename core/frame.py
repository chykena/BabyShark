import struct
import socket
import textwrap

from core.config import *
from core.packet import Packet



class NetworkFrame(object):

    def retrieve_mac_address(self, bytes_address):
        
        bytes_mapper = map('{:02x}'.format, bytes_address)
        mac_address = ':'.join(bytes_mapper).upper()

        return mac_address

    def unpack_ether_frame(self, frame_data):
        cfg = Config()
        pk = Packet()
        nf = NetworkFrame()

        destination, source, protocol = pk.unpack_packet(cfg.ESPI_ETHERNET_FRAME_STR, frame_data, 14)

        return nf.retrieve_mac_address(destination), nf.retrieve_mac_address(source), socket.htons(protocol), frame_data[14:]

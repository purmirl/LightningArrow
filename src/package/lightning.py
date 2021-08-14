"""
 Copyright 2021~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Lightning Arrow Project (UDP Launcher) by PeTrA. 2021~
 LightningArrow 1.0
 Language : Python3.8.2 on pycharm IDE
 Library : Scapy2.4.3
 ------
 @ lightning.py
    * LightningArrow/src/package/lightning.py
    * lightning (UDP launcher module) code file
"""
from scapy.layers.inet import IP, UDP
from scapy.packet import Raw
from scapy.sendrecv import send

def send_packet(_target_ip_address):
    send(IP(dst = _target_ip_address) / UDP(dport = 53,) / Raw(load = "abc"))
    return

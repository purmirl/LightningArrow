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
import threading
import time

from scapy.layers.inet import IP, UDP
from scapy.packet import Raw
from scapy.sendrecv import send

""" @Packet Launcher class
"""
class PacketLauncher(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(PacketLauncher, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.reset_value()

    """ @reset class value
    """
    def reset_value(self):
        self.target_ip_address = ""
        self.thread_key = 0
        return

    """ @packet launcher function on thread
    """
    def run(self):
        self.thread_key = 1
        testing_count = 0
        while True:
            if self.thread_key == 0:
                break
            elif self.thread_key == 1:
                testing_count = testing_count + 1
                print("LightningArrow Threading Systems Testing" + str(testing_count))
                """ warning! send_packet function here is dangerous!
                
                """
                time.sleep(1) # safeguard
                continue
            else:
                break

    """ @set target ip in class
    @:param
        target ip address
    @:return
        null
    """
    def set_target_ip_address(self, _target_ip_address):
        self.target_ip_address = _target_ip_address
        return

    """ @set thread stop
    @:param
        null
    @:return
        null
    """
    def set_thread_stop(self):
        self.thread_key = 0
        return

""" @send packet function
"""
def send_packet(_target_ip_address):
    send(IP(dst = _target_ip_address) / UDP(dport = 53,) / Raw(load = "abc")) # DNS protocol
    return


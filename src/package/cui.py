"""
 Copyright 2021~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Lightning Arrow Project (UDP Launcher) by PeTrA. 2021~
 LightningArrow 1.0
 Language : Python3.8.2 on pycharm IDE
 Library : Scapy2.4.3
 ------
 @ cui.py
    * LightningArrow/src/package/cui.py
    * console user interface code file
"""
from src.package.function import is_protocol_address


class Cui:
    def __init__(self):
        self.reset_value()
        return

    def reset_value(self):
        self.target_ip_address == ""

    def cui_engine(self):
        while True:
            main_command = self.get_command("main")
            if main_command == "?":
                self.print_main_option()
                continue
            elif main_command == "target":
                target_ip_address = self.set_target()
                continue
            elif main_command == "launch":
                self.lightning_start()
                continue
            elif main_command == "stop":
                self.lightning_stop()
                continue
            else:
                continue
        return

    def print_main_option(self):
        main_option = "\n" \
                      " 01. target : set target (ip address) \n" \
                      " 02. launch : UDP launch start \n" \
                      " 03. stop : UDP launch stop \n" \
                      " 04. version : show software version \n" \
                      " 05. exit : program exit \n" \
                      ""
        print(main_option)
        return

    def set_target(self):
        while True:
            target_ip_address = ""
            target_ip_address = input(" target ip address : ")
            if (is_protocol_address(target_ip_address) == 0):
                print(" error, check ip address!")
                continue
            else:
                break
        return target_ip_address

    def lightning_start(self):
        return

    def lightning_stop(self):
        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@lightningarrow:~# ")
        return result

    def print_rights(self):
        print("Copyright 2021~ PeTrA. All rights reserved.")
        print("LightningArrow 1.0\n")
        return
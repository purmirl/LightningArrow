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
from src.package import lightning
from src.package.function import is_protocol_address

""" @Cui class
"""
class Cui:
    def __init__(self):
        self.reset_value()
        return

    def reset_value(self):
        self.target_ip_address = ""
        self.lightning_engine = lightning.PacketLauncher()
        return

    """ @cui engine function
    @:map
        @:main
            @:?
            @:target
            @:launch
            @:stop
            @:version
            @:exit
    """
    def cui_engine(self):
        self.print_rights()
        while True:
            main_command = self.get_command("main")
            if main_command == "?":
                self.print_main_option()
                continue
            elif main_command == "target":
                self.target_ip_address = self.set_target()
                self.lightning_engine.set_target_ip_address(self.target_ip_address)
                continue
            elif main_command == "launch":
                self.lightning_start()
                continue
            elif main_command == "stop":
                print("break")
                self.lightning_stop()
                continue
            elif main_command == "version":
                self.print_software_version()
                continue
            elif main_command == "exit":
                break
            else:
                continue
        return

    """ @main option
    """
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

    """ @set target
    """
    def set_target(self):
        while True:
            input_value = ""
            print("")
            input_value = input(" target ip address : ")
            if (is_protocol_address(input_value) == 0):
                print(" error, check ip address!")
                continue
            else:
                print("")
                break
        return input_value

    """ @lightning thread start
    """
    def lightning_start(self):
        self.lightning_engine.daemon = True
        self.lightning_engine.start()
        return

    """ @lightning thread stop
    """
    def lightning_stop(self):
        self.lightning_engine.set_thread_stop()
        self.lightning_engine.join()
        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@lightningarrow:~# ")
        return result

    def print_rights(self):
        print("Copyright 2021~ PeTrA. All rights reserved.")
        print("LightningArrow 1.0\n")
        return

    def print_software_version(self):
        software_version_string = "\n" \
                                  " LightningArrow v 1.0 by PeTrA. 2021.AGUST Updated.\n" \
                                  ""
        print(software_version_string)
        return
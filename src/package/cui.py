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

class Cui:
    def __init__(self):
        return


    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@lightningarrow:~# ")
        return result
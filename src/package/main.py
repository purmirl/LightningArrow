"""
 Copyright 2021~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Lightning Arrow Project (UDP Launcher) by PeTrA. 2021~
 LightningArrow 1.0
 Language : Python3.8.2 on pycharm IDE
 Library : Scapy2.4.3
 ------
 @ main.py
    * LightningArrow/src/package/main.py
    * main function code file
"""
from src.package import cui

""" @main function
"""
def main():
    main_cui_engine = cui.Cui()
    main_cui_engine.cui_engine()
    return

""" @call main
"""
if __name__ == "__main__":
    main()

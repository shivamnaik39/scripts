# menu.py           author:- Shivam S Naik

import os
import sys


def menu():
    print("""
    
        1.Update the system
        2.Create hotspot
        3.Wi-Fi Strength
        4.Disable Internal Keyboard  5.Enable Internal Keyboard   
        6.Start Samba Server         7.Stop Samba Server
        8.Exit

    """)


def update():

    # #### Ubuntu/Debian #####
    # os.system("sudo apt update")
    # os.system("sudo apt upgrade")

    ####### KDE NEON #####
    # os.system("sudo apt update")

    # os.system("sudo pkcon update")

    # print("The Sysytem was updated successfully!")

    ####### Arch Based #####
    # os.system("sudo pacman -Syu")

    ####### Solus #####
    os.system("sudo eopkg upgrade")


def hotspot():
    print("creating acess point .................")

    ###### Ubuntu/Manjaro/Neon ####

    os.system("sudo create_ap wlp2s0 wlp2s0 axiom39 34567893")

    ###### Debian Hotspot ######

    # os.system("sudo create_ap wlan0 wlan0 axiom39 34567893")

    ###### Dependencies ######

    # sudo apt install bash util-linux  procps hostapd iproute2 iw dnsmasq iptables


def strength():
    ###### Real-Time signal strength ######
    os.system("watch -n1 iwconfig")


def internal_keyboard(n):
    if n == 1:
        os.system("xinput reattach 15 3")

    elif n == 0:
        os.system("xinput float 15")


def samba(n):
    if n == 1:
        os.system("sudo systemctl start smb")

    elif n == 0:
        os.system("sudo systemctl stop smb")


def main():
    menu()

    n = int(input("\nEnter ypur choice: "))

    if n == 1:
        update()

    elif n == 2:
        hotspot()

    elif n == 3:
        strength()

    elif n == 4:
        internal_keyboard(0)

    elif n == 5:
        internal_keyboard(1)

    elif n == 6:
        samba(1)

    elif n == 7:
        samba(0)

    elif n == 8:
        sys.exit()

    else:
        print("Invalid Input!!")
        main()


main()

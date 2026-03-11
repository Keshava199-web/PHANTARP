import scapy.all as scapy
import re
import os
import ctypes

print(r"""
                  [*------------------------------------------------------------------------------*]
                  [*      ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ █████╗ ██████╗ ██████╗      *]
                  [*      ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗     *]
                  [*      ██████╔╝███████║███████║██╔██╗ ██║   ██║   ███████║██████╔╝██████╔╝     *]
                  [*      ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██╔══██║██╔══██╗██╔═══╝      *]
                  [*      ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██║██║          *]
                  [*      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝          *]
                  [*                     "Every device leaves a trace.."                          *]
                  [*                    "Educational Purpose Only...by SK34Ry                     *]
                  [-------------------------------------------------------------------------------*]
""")

def is_admin():
    try:
        return os.geteuid() == 0                      # Linux/Mac
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin()  # Windows

if not is_admin():
    print("[-] This script must be run as Administrator/root.")
    exit(1)

def get_manufacturer(mac):
    try:
        manuf = scapy.conf.manufdb._get_manuf(mac)
        return manuf if manuf else "Unknown"
    except Exception:
        return "Unknown"

ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

try:
    while True:
        ip_add_range_enter = input("\n[?] Enter the IP address and range (e.g. 192.168.1.0/24): ")
        if ip_add_range_pattern.search(ip_add_range_enter):
            print(f"[+] {ip_add_range_enter} is a valid IP address range")
            break
        else:
            print("[-] Invalid format, please try again.")

    print(f"\n[*] Scanning {ip_add_range_enter} ...\n")

    answered, unanswered = scapy.arping(ip_add_range_enter, timeout=1, verbose=False)

    if answered:
        print(f"[+] Scan complete. {len(answered)} host(s) found:\n")
        print(f"  {'IP Address':<20} {'MAC Address':<22} {'Manufacturer'}")
        print("  " + "-" * 70)
        for sent, received in answered:
            ip    = received.psrc
            mac   = received.hwsrc
            manuf = get_manufacturer(mac)
            print(f"  {ip:<20} {mac:<22} {manuf}")
    else:
        print("[-] No hosts found.")

except KeyboardInterrupt:
    print("\n\n[!] Scan interrupted by user. Exiting ARPEX...\n")
    exit(0)

##PHANTARP [ARP Network Scanner..!]

A fast and lightweight ARP network scanner built with Python and Scapy. 
####  PHANTARP discovers all active hosts on a local network, displaying their IP address, MAC address, and device manufacturer — all from a single command.

### ✨ Features

ARP-based host discovery (fast & reliable on local networks)
Manufacturer/vendor lookup from MAC address using Scapy's built-in database
Input validation for IP range format (CIDR notation)
Cross-platform admin/root privilege detection (Windows & Linux/macOS)
Clean, formatted output table

### 🖥️ Requirements

Python 3.x | [Scapy library](https://scapy.net/)

Install Scapy via pip:
### bash
pip install scapy

Note: On Windows, you may also need Npcap installed for Scapy to send/receive packets.


### 🚀-Usage

⚠️ Must be run as root (Linux/macOS) or Administrator (Windows) — ARP scanning requires raw socket access.

### 🧠 How It Works
| Step |  Description  |
|------|---------------|
|   1    |  Checks if the script is running with admin/root privileges  |
|   2    | Prompts the user for an IP range in CIDR format and validates it  |
|   3    |  Sends ARP requests to all addresses in the given range using Scapy  |
|   4    |  Collects replies and extracts IP and MAC addresses from responding hosts  |
|   5    |  Looks up each MAC address against Scapy's manufacturer database  |
|   6    |  Displays all discovered hosts in a formatted table  |

### ⚙️ How ARP Scanning Works
ARP (Address Resolution Protocol) is used to map IP addresses to MAC addresses on a local network. 
PHANTARP broadcasts ARP requests asking "Who has IP x.x.x.x?" — any active device on the network will respond with its MAC address, revealing its presence.

### ⚠️ Legal Disclaimer
This tool is intended for authorized network auditing and educational purposes only. 
Scanning networks without explicit permission from the network owner may be illegal depending on your jurisdiction. 
Always obtain proper authorization before scanning any network you do not own.

###  🛠️ Built With
####  Python 3 — Core language
####  Scapy — Packet crafting and ARP scanning
####  re[regex] — IP range input validation
####  os / ctypes — Cross-platform privilege detection

### 📝 License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

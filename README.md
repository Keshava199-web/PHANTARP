# PHANTARP  [ARP Network Scanner..!]

![PHANTARP scan output](https://raw.githubusercontent.com/Keshava199-web/PHANTARP/main/PhanArp.png)

> A fast, lightweight ARP network scanner built with Python and Scapy.

PHANTARP discovers all active hosts on your local network — revealing IP addresses, MAC addresses, and device manufacturers — from a single command.

---

## Features

- **ARP-based host discovery** — fast and reliable on local networks
- **Vendor/manufacturer lookup** — resolves MAC addresses using Scapy's built-in OUI database
- **Input validation** — enforces correct CIDR notation before scanning
- **Privilege detection** — cross-platform check for root/Administrator rights (Linux, macOS, Windows)
- **Clean output** — results displayed in a formatted, readable table

---

## Requirements

- Python 3.x
- [Scapy](https://scapy.net/)

```bash
pip install scapy
```

> **Windows users:** [Npcap](https://npcap.com/) is required for Scapy to send and receive raw packets.

---

## Usage

> ⚠️ ARP scanning requires raw socket access. Run as **root** on Linux/macOS or **Administrator** on Windows.

```bash
# Linux / macOS
sudo python phantarp.py

# Windows (run terminal as Administrator)
python phantarp.py
```

When prompted, enter an IP range in CIDR notation:

```
Enter IP range (e.g. 192.168.1.0/24): 192.168.1.0/24
```

---

## How It Works

| Step | Description |
|------|-------------|
| 1 | Verifies the script is running with admin/root privileges |
| 2 | Prompts for an IP range in CIDR format and validates the input |
| 3 | Broadcasts ARP requests to every address in the range via Scapy |
| 4 | Collects replies and extracts IP and MAC addresses from responding hosts |
| 5 | Resolves each MAC address to a manufacturer using Scapy's OUI database |
| 6 | Displays all discovered hosts in a formatted table |

### Why ARP?

ARP (Address Resolution Protocol) maps IP addresses to MAC addresses on a local network. PHANTARP sends broadcast ARP requests asking *"Who has IP x.x.x.x?"* — any active device will respond with its MAC address, revealing its presence on the network.

---

## Built With

| Component | Purpose |
|-----------|---------|
| [Python 3](https://www.python.org/) | Core language |
| [Scapy](https://scapy.net/) | Packet crafting and ARP scanning |
| `re` | IP range input validation |
| `os` / `ctypes` | Cross-platform privilege detection |

---

## Legal Disclaimer

This tool is intended for **authorized network auditing and educational purposes only**. Scanning networks without explicit permission from the network owner may be illegal in your jurisdiction. Always obtain proper authorization before scanning any network you do not own.

---

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

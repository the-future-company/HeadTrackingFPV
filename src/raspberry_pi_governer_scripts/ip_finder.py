import argparse
import re
import socket

import nmap


# Target hostname pattern for Raspberry Pi
target_host_pattern = r""".*(pi\W|raspberry.*?pi|pi.*?raspberry).*"""


# Function to get the local IP range based on the current IP of the device
def get_local_ip_range():
    try:
        # Creating a socket to determine the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # Doesn't need to be reachable; used to get the local network interface IP
            s.connect(('10.254.254.254', 1))
            local_ip = s.getsockname()[0]
        except Exception:
            local_ip = '127.0.0.1'
        finally:
            s.close()

        # Extracting the base of the IP (first three octets) to form the range
        ip_base = '.'.join(local_ip.split('.')[:-1])
        return f"{ip_base}.0-255"
    except Exception as e:
        print(f"Error in getting local IP range: {e}")
        return None


# Function to discover hosts in the specified IP range
def discover_hosts(ip_range):
    nm = nmap.PortScanner()
    nm.scan(ip_range, arguments='-sn')  # -sn for Ping Scan - disable port scan

    for host in nm.all_hosts():
        if 'hostnames' in nm[host]:
            hostnames = [hostname['name'] for hostname in nm[host]['hostnames']]
            for hostname in hostnames:
                if re.search(target_host_pattern, hostname, re.IGNORECASE):
                    print(f"Found Raspberry Pi at IP: {host}, Hostname: {', '.join(hostnames)}")
                    return  # Return after finding the first Raspberry Pi


def main():
    # Setting up argument parser
    parser = argparse.ArgumentParser(
        description="""
        Discover Raspberry Pi devices on the network. This script should be your last reserve. More accurate and quick 
        way is to go to your providers website/app, login and look for devices that are logged into your network. Your 
        raspberry pi should have the name 'pi' or 'raspberrypi'.
        """)
    parser.add_argument('--range', type=str, help='Specify the IP range to scan, e.g., "192.168.1.0-255". If not '
                                                  'provided, the script uses the local network range.')
    args = parser.parse_args()

    # Use the provided IP range or determine it automatically
    ip_range = args.range if args.range else get_local_ip_range()
    if ip_range:
        print(f"Scanning IP range: {ip_range}")
        discover_hosts(ip_range)
    else:
        print("Unable to determine local IP range.")


if __name__ == "__main__":
    main()

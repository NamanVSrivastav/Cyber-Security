import socket
from datetime import datetime

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning target: {target_ip}")
    print(f"Scanning ports from {start_port} to {end_port}")
    start_time = datetime.now()

    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Scan completed in {duration}")

    if open_ports:
        print(f"Open ports on {target_ip}:")
        for port in open_ports:
            print(f"Port {port}: Open")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    port_scanner(target_ip, start_port, end_port)

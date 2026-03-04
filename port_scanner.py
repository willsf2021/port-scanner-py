import socket

# Settings
target = "192.168.3.1"
ports_to_scan = range(1, 1024) # Ports from 1 to 1024

print(f"Start of Scan in {target}")

for port in ports_to_scan:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        
        server.settimeout(0.1)

        result = server.connect_ex((target, port)) 
        
        if result == 0:
            print(f"Porta {port} ABERTA!")

print("End of scan")

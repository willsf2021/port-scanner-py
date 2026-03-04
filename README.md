# port-scanner-py

A simple port scanner built with Python and raw sockets.

## What it does

Receives an IP address, scans the most common ports and prints which ones are open.

## Why I built this

To understand how network ports work at a low level — without relying on external tools like nmap. Built as a hands-on exercise in Python networking and Linux environment.

## Tech

- Python 3
- socket (standard library only)
- Linux / Ubuntu

## Usage

- Open the file 'port_scanner.py'
- You can change as you want the follow variables:
```python
    target = "192.168.3.1"
    ports_to_scan = range(1, 1024)
```
- Run the script
```bash
    python3 port_scanner.py
```

## What I learned

> Basics of Ports and most commons protocols
> Basics of raw sockets in Python
> Each protocol is represented by a differente methodo from sockets (ex: SOCK_DGRAM, SOCK_STREAM)

---

Work in progress.


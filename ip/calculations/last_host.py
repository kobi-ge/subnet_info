def find_last_host(broadcast_ip):
    broadcast_ip[3] -= 1
    return broadcast_ip

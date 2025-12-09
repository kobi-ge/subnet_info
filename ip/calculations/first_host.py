def find_first_host(ip, idx=3):
    if idx == 0 and ip[idx] == 255:
        return "IP is full, no next host exists"
    if ip[idx] == 255:
        return find_first_host(ip, idx-1)
    ip[idx] += 1
    return ip


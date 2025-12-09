def find_broadcast(network_ip, octate, opts):
    network_ip = list(network_ip)
    if octate == 0 and network_ip[octate] == 255:
        return "something is wrong with the numbers"
    if network_ip[octate] + (opts - 1) > 255:
        network_ip[octate - 1] += 1
        network_ip[octate] = (network_ip[octate] + opts - 1) - 256
    else:
        network_ip[octate] += (opts - 1)
    return network_ip

ip = [192, 168, 10, 0]
print(find_broadcast(ip, 3, 512))

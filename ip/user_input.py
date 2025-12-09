def insert_ip():
    first_octate = input("enter the first octate ")
    second_octate = input("enter the second octate ")
    third_octate = input("enter the third octate ")
    last_octate = input("enter the last octate ")
    subnet = input("enter subnet ")
    ip = [int(first_octate), int(second_octate), int(third_octate), int(last_octate)]
    return ip, subnet

def check_ip(ip):
    for octate in range(len(ip)):
        if ip[octate] > 255 or ip[octate] < 0:
            return f"octate in index {octate} is illegal"
    return True

def check_subnet(subnet):
    if 0 > subnet > 32:
        return f"subnet is illegal"
    return True



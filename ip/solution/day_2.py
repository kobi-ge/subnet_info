import sys

def convert_to_word(ip):
    bytes = ip.split('.')
    word = 0
    for byte in bytes:
        word = (word << 8) | int(byte)
    return word

def convert_to_str(word):
    return '.'.join(str((word >> (i * 8)) & 0xFF) for i in range(3, -1, -1))

def convert_size_mask_to_word(num):
    mask = (0xFFFFFFFF & (2**(32) - 2**(32 - num)))
    return mask

def Analysis_ip(ip, subnet_mask): 

    size_sub = bin(subnet_mask).count('1') 
    network = (ip & subnet_mask)  
    host_begin = network | 1 

    host_end = network | (2**(32 - size_sub) - 2 )
    broadcast = network | (2**(32 - size_sub)  - 1)
    next_subnet = ((ip & subnet_mask) + 2**(32 - size_sub))

    return network, host_begin, host_end, broadcast, next_subnet

def display(network, host_begin, host_end, broadcast, next_subnet):
    print('network: ', convert_to_str(network))
    print('host range: ', convert_to_str(host_begin), '-', convert_to_str(host_end), sep='')
    print('broadcast: ', convert_to_str(broadcast))
    print('next subnet: ', convert_to_str(next_subnet))

def main():
    try:
        ip, mask = sys.argv[1:3]

        ip = convert_to_word(ip)

        if mask.isdigit():
            mask = convert_size_mask_to_word(int(mask))
        else:
            mask = convert_to_word(mask)

        values = Analysis_ip(ip, mask)
        display(*values)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

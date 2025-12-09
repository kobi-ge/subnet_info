def find_octate(subnet):
    octate = subnet // 8
    if octate > 3:
        return 3
    return octate


def find_zeroes(ip, subnet):
    ones = subnet % 8
    return 8 - ones

def find_opts(zeroes):
    return 2 ** zeroes


def divide(ip, octate_idx, zeroes, opts):
    octate = ip[octate_idx]
    return octate // opts


def  multiply(divide_result, ip, opts):
    return divide_result * opts




ip = [192,168,10,250]
subnet = 23

octate = find_octate(subnet)
zeroes = find_zeroes(ip, subnet)
opts = find_opts(zeroes)
division = divide(ip, octate, zeroes, opts)
result = multiply(division, ip, opts)
print(f"octate: {octate} \nzeroes: {zeroes} \ndivision: {division} \nresult: {result} ")
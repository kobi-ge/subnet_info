class NetworkCalculator:
    def __init__(self, ip, subnet):
        self.ip = ip
        self.subnet = subnet
        self.target_octate = None
        self.zeroes_count = None
        self.opts = None
        self.division = None
        self.multiply_res = None


    def find_octate(self):
        self.target_octate = self.subnet // 8
        if self.target_octate > 3:
            self.target_octate = 3
            return 3
        return self.target_octate

    def find_zeroes(self):
        ones = self.subnet % 8
        self.zeroes_count = 8 - ones
        return self.zeroes_count 

    def find_opts(self, zeroes):
        self.opts = 2 ** zeroes
        return self.opts

    def divide(self, octate_idx, opts):
        octate = self.ip[octate_idx]
        self.division = octate // opts
        return self.division

    def multiply(self, divide_result, opts):
        self.multiply_res = divide_result * opts
        return self.multiply_res

    def full_ip(self):
        self.ip[self.target_octate] = self.multiply_res
        for i in range(self.target_octate + 1, 4):
            self.ip[i] = 0
        return self.ip

ip = [192,168,10,250]
subnet = 23


def run(ip, subnet):
    network = NetworkCalculator(ip, subnet)
    network.find_octate()
    network.find_zeroes()
    network.find_opts(network.zeroes_count)
    network.divide(network.target_octate, network.opts)
    network.multiply(network.division, network.opts)
    return network.full_ip()











# octate = find_octate(subnet)
# zeroes = find_zeroes(ip, subnet)
# opts = find_opts(zeroes)
# division = divide(ip, octate, zeroes, opts)
# result = multiply(division, ip, opts)
# print(f"octate: {octate} \nzeroes: {zeroes} \ndivision: {division} \nresult: {result} ")
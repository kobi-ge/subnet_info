import user_input
from calculations import network, first_host


def main():
    ip_subnet = user_input.insert_ip()
    ip = ip_subnet[0]
    subnet = ip_subnet[1]
    network_ip = network.run(ip, subnet)
    first_host_ip = first_host.find_first_host(network_ip, )


if __name__ == "__main__":
    main()

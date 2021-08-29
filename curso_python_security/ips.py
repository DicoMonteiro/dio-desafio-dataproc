import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco + 255)


net = '192.168.0.0/24'

rede = ipaddress.ip_network(net)

print(rede)


net2 = '192.168.0.100/16'

rede2 = ipaddress.ip_network(net2, strict=False)

print(rede2)
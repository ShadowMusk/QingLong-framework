import os


def ICMP_Tunnel(choice):
    command = "ptunnel -p {} -lp {} -da {} -dp {} -x {}".format(choice.split()[1], choice.split()[2], choice.split()[3], choice.split()[4], choice.split()[5])
    os.system(command)

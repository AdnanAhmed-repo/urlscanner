import os


def get_nmap(options, ip):
    commands = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results
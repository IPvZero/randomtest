from nornir import InitNornir
from nornir.plugins.functions.text import print_result, print_title
from nornir.plugins.tasks.networking import netmiko_send_command
import getpass
import sys
import os


nr = InitNornir(config_file="config.yaml")


nr.inventory.defaults.username = os.environ["NR_USER"]
nr.inventory.defaults.password = os.environ["NR_PASS"]

def show_output(task):
    task.run(task=netmiko_send_command, command_string = "show ip int brief")

results = nr.run(task=show_output)

print_result(results)


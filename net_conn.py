"""
Function Netmiko Connection
"""

from dotenv import load_dotenv
load_dotenv()
import os

user_lab = os.getenv("USER_LAB")
pass_lab = os.getenv("PASS_LAB")
secret = os.getenv("SEC_LAB")

def netmiko_connection(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': user_lab,
            'password': pass_lab,
             }
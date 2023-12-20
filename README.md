# Disclaimer
I'm not a dev yet, this is NOT fancy code. It does work (for me at least!) though. You can seriously mess up your producition environment with my scripts if you don't know what you're doing. I take no responsibility for that :)</br>

## Clean-up local users in network devices

How to clean-up local users in your network environment that doesn't authenticate on TACACS or some platform that provides security policy management to secure network access for end users and devices.

## Dependencies: Install the requirements to have all dependencies used on this project
$ pip install -r requirements

## How to 
1 - Put only usernames needed stay on devices in line 9 of the code.<br/>
2 - Show all users in devices and check if usernames are in variable list "users".<br/>
2 - Split all usernames, if is not match in variable list "users", then create a new_list with users..<br/>
3 - Send command to remove all usernames in variable new_list, after removed show the usernames in each devices.<br/>

## hosts
List of devices that will be connected to delete local users. I'm using FQDN then, change name for IP addresses if you prefer.

## get_user_priv_lvl.py
A function to get all users and privilege level on devices, can be used before remove users to verify how much user have and after to verify if users on devices match with varibale users variable on line 10 of the file remove_users.py

## create_users.py and config_cmd
Used only for testing, creating a new users on devices using method send_config_from_file("config_cmd)to compare with variable users list on remove_users.py

## remove_users.py
Using line 10 of function "users = ["vanderson", "backup"]" to put all desible users to match. If not match, the function will remove all undesible local users on devices.

## .env
To protect credentials leaking, create a .env file with variables that will be used to connect on devices (USER_LAB/PASS_LAB).

## net_conn.py
A module imported in files ".py" which needed a credentials to connect on devices.



'''
This script is created by Santo K Thomas (santokalayil@gmail.com, +918891960880)
This script is tested working only in windows 10 platform. 
'''

import re
import subprocess
import json

from tools.commands import cmd_show_wlan_profiles

get_output = lambda cmd_list: subprocess.run(cmd_list,capture_output=True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", get_output(cmd_show_wlan_profiles.split())))


def get_full_wify_profile(profile_name):
    wifi_profile = {}
    cmd_list_1 = "netsh wlan show profile".split() + [profile_name]
    if re.search("Security key           : Absent", get_output(cmd_list_1)):
        pass
    else:
        wifi_profile['ssid'] = profile_name
        cmd_list_2 = "netsh wlan show profile".split() + [profile_name] + ["key=clear"]
        password_re = re.search("Key Content            : (.*)\r", get_output(cmd_list_2))
        if password_re == None:
            wifi_profile["password"] = None
        else:
            wifi_profile["password"] = password_re[1] # [0] is the whole content
    return wifi_profile

all_wifi_profile_list = [get_full_wify_profile(profile_name) for profile_name in profile_names]

with open('result.json', 'w') as fp:
    json.dump(all_wifi_profile_list, fp)


import os

# windows commands
cmd_show_wlan_profiles = "netsh wlan show profiles"
profile_name = "CPH1701"  # ssid
cmd_show_wlan_show_profile = f"netsh wlan show profile {profile_name}"

cmd_show_wlan_show_profile_with_password = f"netsh wlan show profile {profile_name} key=clear"
os.system(cmd_show_wlan_show_profile_with_password)



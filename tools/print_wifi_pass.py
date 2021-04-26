import json
with open('result.json') as f:
  wifi_list = json.load(f)
print(100*"=")

for wifi in wifi_list:
    print(wifi)
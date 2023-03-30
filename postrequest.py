import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://icp-member-stage.icashpay.com.tw/app/MemberInfo/UserCodeLogin2022'

headers = {
    'X-ICP-EncKeyID': '219740',
    'X-iCP-Signature': 'dQ5XF5nkMEQa9OGMgRTNVPQVSdFZNMDCfD2KDP+A1Qsn0odhU85yJ4rD0NdDgvidEwCw0cffQzNGlLX9KZId/YxO9XSOM5gSflXp9Vm0nqoUyc6Xj2tVQxTPvs8Geu7+YROOAQIfnxNVOIdKC2X/ZsvyG2feLCe801P9wKjwichws+4xr8BrOQAfjzp6dC5WM9F/EucyHtM2zP79rw+XdH9GCz9wW89TlOGqmA3gsURgTHYqFrT8tJsiB9WLrH75NDMP9oUDqIGtOfvhfrm35jzOM7tMVHM+Z/t0JxjUjsafXCXGsqWuBZMxkDdPSfTDunuN0/OnFb7QnAX6Dj6lBg=='
}

data = {'EncData': 'N5FlapEsxLB7oqXSx8VQGQ+aEfrRM2TXxogQjOYRrRBfCM2tOYZXlrrUsvMmK/sqZVmp+/6VZF0D78WiLsVHHmtP8d/nW3T87lwv6IJ2oEJVyo6M93YozMxXC+W1QgHA'}

response = requests.post(url, headers=headers, data=data, verify=False)

print(response.text)
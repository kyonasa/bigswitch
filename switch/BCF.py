import requests
# import mysql.connector
import re
import json
import time


def getcookie(ip):
    url1="https://"+ip+":8443/api/v1/auth/login"
    p1={"user":"kyonasa","password":"kyonasa"}
    h1={"Content-Type":"application/json"}
    p1=json.dumps(p1)
    r=requests.post(url=url1,data=p1,headers=h1,verify=False)
    d=r.json()
    return d['session_cookie']


def getallswitch(ip,cookie):
    url2="https://"+ip+":8443/api/v1/data/controller/applications/bcf/info/fabric/switch"
    h2={"Content-Type":"application/json","Cookie":"session_cookie="+cookie}
    r2=requests.get(url=url2,headers=h2,verify=False)
    d=r2.json()
    return d



def setswitch(ip,cookie):
    url2="https://"+ip+":8443/api/v1/data/controller/core/switch-config[name=Leaf-1]/interface[name=ethernet11]"
    p1 = {"shutdown":"true"}
    h2={"Content-Type":"application/json","Cookie":"session_cookie="+cookie}
    p1 = json.dumps(p1)
    r2=requests.post(url=url2,data=p1,headers=h2,verify=False)
    d=r2.json()
    return d



ip="10.10.10.1"
switch=setswitch(ip, getcookie(ip))
print (switch)
# for i in range(len(switch)):
#     print(switch[i]['name'])
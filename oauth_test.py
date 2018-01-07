# -*-coding:utf-8 -*-
"""
测试requ
"""
 
import time
import random
import pdb
import requests

if __name__ == "__main__":
    data  = {
        'token':'2170d8ac-f5d5-43ad-9d1c-5c8e9cfc223e',
        'appid':'837ebe47-37dd-4eff-a11d-0f681039e08b',
        'secret':'e0a3c091-c97f-4c2f-a7b9-e915da5016df'
        }
    url = 'http://127.0.0.1:8000/users/oauth2/authorize/'
    req = requests.post(url, data=data)
    print(req.text)
     

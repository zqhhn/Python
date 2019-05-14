# -*- coding: utf-8 -*-
username = input("请输入您的用户名：")
while username =="": 
    username = input("请输入您的用户名:")
    
if username == "admin":
    print("Welcome,",username)
else:
    print("Hello,",username)
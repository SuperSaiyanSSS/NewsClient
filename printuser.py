# -*- coding: utf-8 -*-
import hashlib

with open('user.txt', 'a') as f:
    salt = "addlength"
    name_list = ['root', 'admin']
    password_list = ['12', '123']
    for i, j in zip(name_list, password_list):
        username = i + salt
        username = hashlib.md5(username).hexdigest()
        password = j + salt
        password = hashlib.md5(password).hexdigest()
        f.write(username+"---"+password+'\n')

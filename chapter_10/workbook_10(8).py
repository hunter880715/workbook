# coding:GBK 
# 10-13 ��֤�û������һ�� remember_me.py �汾�����û�Ҫô���������û�����Ҫô���״����иó���
# ����Ӧ�޸����������Ӧ�����������Σ���ǰ�����һ�����иó�����û�����ͬһ���ˡ�
# Ϊ�ˣ��� greet_user() �д�ӡ��ӭ�û���������Ϣǰ����ѯ�����û����Ƿ��ǶԵġ�
# ������ԣ��͵��� get_new_username() ���û�������ȷ���û�����
import json

def get_stored_username():
    """����洢���û������ͻ�ȡ��"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        
def get_new_username():
    """��ʾ�û������û���"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'a') as f_obj:
        json.dump(username, f_obj)
    return username
    
def greet_user():
    """�ʺ��û�����ָ��������"""
    username = get_stored_username()
    if username:
        message = input("Is that right(y/n)?")
        if message =='y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + 
                username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + 
            username + "!")
greet_user()

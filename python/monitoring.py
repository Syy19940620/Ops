#!/usr/bin/python
# -*- coding: UTF-8 -*-

import paramiko
import time

lists = [["1111", 1, "111111", "11111"]]

"""
连接服务器方法
"""


def ssh_client(host, port, username, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, passwd)
    string = "ps -aux|grep java|grep -v grep|awk '{print \"pid:\", $2, \"cpu:\", $3, \"mem:\", $4}'"
    stdin, stdout, stderr = ssh.exec_command(string)

    i = 0
    counts = stdout.readlines()
    for count in counts:
        print(count)
        i = i+1
    print("java进程数量：" + str(i))
    ssh.close()


if __name__ == '__main__':
    while True:
        time.sleep(5)
        for information in lists:
            try:
                print("//////////////////////////////////")
                print("连接服务器："+information[0])
                ssh_client(information[0],information[1],information[2],information[3])
            except RuntimeError:
                print("运行错误")
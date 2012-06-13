#!/usr/bin/python
#process 创建子进程
import subprocess

pingP = subprocess.Popen(args = 'ping -c 4 www.siang.com.cn' , shell = True)

pingP.wait()
print pingP.pid
print pingP.returncode
import os


def getCurPath1():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    return cur_path


def getCurPath2():
    cur_path = os.getcwd()
    return cur_path
os.path.dirname(os.path.abspath(__file__))

print('func1----' + getCurPath1())
print('func2----' + getCurPath2())

os.path.abspath("/etc/sysconfig/selinux")
'/etc/sysconfig/selinux'
os.getcwd()
'/root'
os.path.abspath("path")
'/root/python_modu'


os.path.realpath("/etc/sysconfig/selinux")
'/etc/selinux/config'
os.path.realpath("path")
'/usr/bin/python2.7'
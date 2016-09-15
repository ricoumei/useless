import os
import re

"""
改名工具，只支持正则
"""

def rename(path, old, new):
    path.replace('\\', '/')
    filenames = os.listdir(path)
    for filename in filenames:
        new_name = re.sub(old, new, filename)
        os.rename(os.path.join(path, filename), os.path.join(path, new_name))

if __name__ == '__main__':
    #目标文件路径
    path = input('Path: ')
    #欲修改的字符
    old = input('Old: ')
    #修改后的字符
    new = input('New: ')
    rename(path.replace('\\', '/'), old, new)
    
    
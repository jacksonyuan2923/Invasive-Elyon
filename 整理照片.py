
import os
import shutil
from os import walk, mkdir, remove, rmdir

path = input('请输入图库完整路径：')
wenjian = input('自定义一个新文件夹名称或选择一个已有的文件夹：')

def mop():
    for file in files:
        if file.lower().endswith('.jpg'):
            shutil.copy(os.path.join(filepath, file), os.path.join(path, wenjian, file))
            remove(os.path.join(filepath, file))
            print(file)


for filepath, folder, files in walk(path):
        if os.path.exists(os.path.join(path, wenjian)):
            if wenjian in filepath or 'Screenshots' in filepath:
                continue
            mop()
        else:
            mkdir(os.path.join(path, wenjian))
            if wenjian in filepath or 'Screenshots' in filepath:
                continue
            mop()

        # if wenjian in filepath or 'Screenshots' in filepath:
        #     continue
        # for file in files:
        #     if file.lower().endswith('.jpg'):
        #         shutil.copy(os.path.join(filepath, file), os.path.join(path, wenjian, file))
        #         remove(os.path.join(filepath, file))
        #         print(file)


for filepath, folder, files in walk(path):
    for i in folder:
        if wenjian in i  or 'Screenshots' in i:
            continue
        fullpath = os.path.join(filepath, i)
        if not os.listdir(fullpath):
            rmdir(fullpath)
            print(f"✅ 已删除空文件夹: {fullpath}")
        else:
            print(f"❌ 未删除: {fullpath}（非空: {os.listdir(fullpath)}）")

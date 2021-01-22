import os, shutil

dir_path = 'xxx'

os.chdir(dir_path)
folder_name = os.listdir(dir_path)
# folder_name = [] # 此条件进入else
if folder_name:
    print("成功获取到的所有文件夹名  √")
else:
    print("未获取到的所有文件夹名  ×")
    exit()

num = 0

# 对file_name进行字符串处理的函数
def Deal_file_name(name):
    k = name.index('_')
    return name[0:k]

# print(os.getcwd()) # 获取工作目录
file_name = folder_name[0]

# 开始循环重命名
for file_name in folder_name:
    # 进入文件夹
    file_path = dir_path + file_name
    os.chdir(file_path)
    #print(os.getcwd())

    # 1. 获取文件夹下所有文件名
    old_names = os.listdir(file_path)

    # 2. 分离扩展名
    extend_name = os.path.splitext(old_names[0])    # 分离后是一个文件名与扩展名（包含.）构成的元组（tuple)

    # 3. 将处理后的文件名连同扩展名一起构成新文件名
    new_name = Deal_file_name(file_name) + extend_name[1]

    # 4. 重命名文件
    os.rename(old_names[0], new_name)

    # 6. 将文件移动到上一级目录
    shutil.move(file_path+"\\"+ new_name, dir_path+ "\\" + new_name)

    # 7. 删除空文件夹
    os.chdir(dir_path)
    os.removedirs(file_path)

    num += 1

print("完成重命名的文件的数目：" + str(num))
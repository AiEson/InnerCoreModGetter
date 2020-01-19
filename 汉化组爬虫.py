import urllib.request
from urllib import request
import json

def mkdir(path):
    import os
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print
        path + ' 创建成功'
        return True
    else:
        print
        path + ' 目录已存在'
        return False
# 获取源码
html = request.urlopen("http://www.innercorehhz.cf/alljson.php")
# 打印源码
ym = html.read().decode('utf8')
json = eval(ym)
mkdir("img")
leng = len(json)
print("获取完成，汉化组共" + str(leng) + "个MOD，正在开始下载...")
for i in range(len(json)):
    json2 = eval(str(json[i]))
    id = json2["id"]
    name = json2["name"]
    photo = json2["icon"]
    print("正在下载第" + str(i+1) + "个MOD：" + name + ", ID为：" + str(id) + ", 图片为：" + photo + "  [" + str(i+1) + "/" + str(leng) + "] " + ' {:.2%}'.format((i+1)/leng))
    f = urllib.request.urlopen("http://www.innercorehhz.cf/hhz/download.php?id=" + str(int(id)-5000))
    fpic = urllib.request.urlopen("http://www.innercorehhz.cf/mods/%E5%B7%B2%E9%80%9A%E8%BF%87/icon/" + str(photo))
    with open(str(id), "wb") as code:
        code.write(f.read())
    with open("img/" + str(photo), "wb") as code:
        code.write(fpic.read())
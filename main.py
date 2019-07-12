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
class Mod:
    URL = 'http://icmods.mineprogramming.org/api/'
    lang = "zh"

    def getCount(self):
        return rp(self.URL + "count.php")
    def getAllMod(self):
        return rp(self.URL + "list.php?count=" + self.getCount() + "&start=0&sort=popular")
def rp(url):
    response = request.urlopen(url)
    res = response.read().decode('utf-8')
    return res
listMOD = []
mod = Mod();
allModInfo = mod.getAllMod()
with open(str("所有MOD信息.json"), "wb") as code:
    code.write(str(allModInfo).encode())
js = json.loads(allModInfo)
for jb in js:
    listMOD.append(jb)
modNumb = str(len(listMOD))
print("官网共" + modNumb + "个MOD，正在开始下载...")
mkdir("img")
numb = 0
for a in listMOD:
    numb+=1;
    f = urllib.request.urlopen("https://icmods.mineprogramming.org/api/download?id=" + str(a["id"]))
    ficon = urllib.request.urlopen("https://icmods.mineprogramming.org/api/img/" + str(a["icon"]))
    print("正在下载MOD：" + a["title"] + " ID为：" + str(a["id"]) + " 图片为：" + str(a["icon"]) + "  [" + str(numb) + "/" + modNumb + "] " + ' {:.2%}'.format(numb/int(modNumb)))
    with open(str(a["id"]), "wb") as code:
        code.write(f.read())
    with open('img/' + str(a["icon"]), "wb") as code:
        code.write(ficon.read())
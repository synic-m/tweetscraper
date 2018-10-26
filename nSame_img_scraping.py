import requests
from bs4 import BeautifulSoup
import re
import os.path



#取得からurl https~の探索***********************************************
target_url = 'https://twitter.com/_zith/media'#twitter_url
r = requests.get(target_url)

soup = BeautifulSoup(r.text,'lxml')
imgs= soup.find_all("img",src=re.compile('^https://pbs.twimg.com/media/'))
#***********************************************************************


os.chdir('picture')

#file → open →　https://の名前を取得 +.jpeg →write/bynary　→　fileとして生成contentそのページの中身
try:
    for img in imgs:
        print(img['src'])
        imgName = str(img['src'])
        imgName = imgName[28:]
        print("imgName" + imgName)
        r = requests.get(img['src'])
        try:
            if os.path.exists(imgName) == False:
                with open(str(imgName),'ab') as file:#パス指定pictur/にimgNameでファイル保存
                    file.write(r.content)
                print("mkfl")
            else:
                print("alredy there")
        except Exception as e:
            print(e)
            #print(r.content)  #study
#例題処理*****************************************************************************
except Exception as e:
    print(e)


#*************************************************************************************
print("fin")


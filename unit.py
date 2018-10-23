import requests
from bs4 import BeautifulSoup

#url取得
target_url = ''#twitter_url
r = requests.get(target_url)


soup = BeautifulSoup(r.text,'lxml')
#ｌｘｍｌでデータを全部引っ張った
main_datas = soup.find_all("p", attrs={"class":"TweetTextSize"})
#全データからｐタグのクラスtweettextsizeのやつだけ表示
#print('%s' %(main_data))
#debug的に表示

#data = [main_data.string for main_data in main_datas]
mDatas = main_datas
data = []
for mData in mDatas:
    data.append(mData.string)
str_data =('')
for x in data:
    if x  != None:
        str_data += x
        str_data += '\n'

print(str_data)
print('*********************************************')
dl_file = "fm.txt"
#path指定して書き込み場所を選択

try:
    #file開く→格納
    file = open(dl_file,'a')
    data = file.write(str_data)
except Exception as e:
    #errorが出た場合実行したままエラー表記
    print(e)
finally:
   file.close()

print('fin')


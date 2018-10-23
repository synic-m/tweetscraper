import requests
from bs4 import BeautifulSoup

#url取得
target_url = input()

r = requests.get(target_url)

soup = BeautifulSoup(r.text,'lxml')
#ｌｘｍｌでデータを全部引っ張った
main_datas = soup.find("p", attrs={"class":"TweetTextSize"})
#全データからｐタグのクラスtweettextsizeのやつだけ表示
#print('%s' %(main_data))
#debug的に表示
#data = [main_data.string for main_data in main_datas]
mDatas = main_datas
data = []
#listを作って
for mData in mDatas:
    data.append(mData.string)
    #forで.appendしていく
str_data =('')
#*************dataの整形************************************
for x in data:
    if x  != None:
    #loopの条件None　→　loopしない and 前の配列要素と同じならloopしない
        str_data += x
        str_data += '\n'
        #改行も入れる　x + '\n'
#*********************************************************

print(str_data)
print('*********************************************')
dl_file = "fm.txt"
    #path指定して書き込み場所を選択

try:
    #file開く→格納
    file = open(dl_file,'a')
    data = file.write(str_data)
    key = input('続ける＞＞＞１')
except Exception as e:
    #errorが出た場合実行したままエラー表記
    print(e)
finally:
    file.close()
    
print('fin')


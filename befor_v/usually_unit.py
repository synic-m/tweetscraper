import requests
from bs4 import BeautifulSoup

#url取得
target_url = ''#ここにurl
key = 1
str_data_ar = 'nope'
while(key == 1):

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
    #listを作って
    for mData in mDatas:
        data.append(mData.string)
        #forで.appendしていく
    str_data =('')
    
#*************dataの整形************************************
    for x in data:
        if x  != None :
            if str_data_ar != x:#xの処理部分が？？？？？？？？？？？？？？？？？ってかんじ
                print(x)#debug
    #loopの条件None　→　loopしない and 前の配列要素と同じならloopしない
                str_data_ar = x
                str_data += x
                str_data += '\n'
            else:
                print("error")
            #改行も入れる　x + '\n'
#*********************************************************

    print(str_data)
    print('*********************************************')
    dl_file = "txts/aoba.txt"
    #path指定して書き込み場所を選択

    try:#with使えばよかったか
        #file開く→格納
        file = open(dl_file,'a')
        data = file.write(str_data)
    except Exception as e:
        #errorが出た場合実行したままエラー表記
        print(e)
    finally:
        file.close()
    
print('fin')


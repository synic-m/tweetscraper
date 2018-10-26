import requests
from bs4 import BeautifulSoup

target_url = ''#twitter_url
r = requests.get(target_url)

soup = BeautifulSoup(r.text,'lxml')

main_data = soup.find("p", attrs={"class":"TweetTextSize"})

print('%s' %(main_data))

dl_file = "fm.txt"
try:
    file = open(dl_file,'w')
    data = file.write(main_data)
except Exception as e:
    print(e)
    print('error')
finally:
   file.close()

print('fin')

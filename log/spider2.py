import requests
from bs4 import BeautifulSoup
import json
import time
import random
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def spider(ip_param):
    url = "http://ip.taobao.com/service/getIpInfo.php?ip={}".format(ip_param)
    try:
        wb_data = requests.get(url)
    except Exception:
        time.sleep(random.random()*5)
        wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    text_json = json.loads(soup.text)
    if text_json['code'] == 0:  # parse search result from url
        print(text_json)
        country = text_json['data']['country']
        region = text_json['data']['region']
        city = text_json['data']['city']
        isp = text_json['data']['isp']

        final_dict = {
            "country": country,
            'region': region,
            'city': city,
            'isp': isp
        }

        final_list = [country, region, city, isp]
        return final_list
    else:
        return ['', '', '', '']

if __name__ == '__main__':
    # Do the reading
    file1 = open('123.csv', 'rb')
    reader = csv.reader(file1)
    new_rows_list = []
    for row in reader:
        ip = row[1]
        temp_list = spider(ip)
        new_row = [row[0], row[1], temp_list]
        new_rows_list.append(new_row)
    file1.close()  # <---IMPORTANT
    new_rows_list[0][2] = 'location'
    # Do the writing
    file2 = open('123.csv', 'wb')
    writer = csv.writer(file2)
    writer.writerows(new_rows_list)
    file2.close()


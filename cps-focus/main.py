import requests
from bs4 import BeautifulSoup
import json
def get_data(req_url):
    """获取数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Language': 'zh-Hans-CN, zh-Hans;q=0.5'
    }
    resp = requests.get(req_url, headers=headers)
    resp.encoding = 'utf8'  
    if resp.status_code == 200:
        return resp.text
    else:
        return None

def parse_data(resp_html):
    """解析数据,并返回列表"""
    soup = BeautifulSoup(resp_html, features='html.parser')
   # print(soup.prettify())
    focus_table = soup.find("div", attrs={'id': 'focus'})
   # print(focus_table)
    focus_list = focus_table.find_all('li')
   # print(focus_list)
    res_list = []
    for focus in focus_list:
        title = focus.find('img').get('alt')
        img = focus.find('img').get('src')
        res_item = {
            '标题': title,
            '图片': img,
        }
        res_list.append(res_item)
    return res_list


def save_data(res_list):
    """保存数据"""
    with open('focus.json', 'w', encoding='utf-8') as f:
        res_list_json = json.dumps(res_list, ensure_ascii=False)
        f.write(res_list_json)
        print(res_list_json)


if __name__ == '__main__':
    req_url = 'http://www.cps.com.cn/'
    # 获取数据
    resp_html = get_data(req_url)
    # 解析数据
    res_list = parse_data(resp_html)
    #print(res_list)
    # 保存数据
    save_data(res_list)
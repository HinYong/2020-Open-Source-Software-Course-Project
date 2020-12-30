import requests
from bs4 import BeautifulSoup
import os


def get_data():
    for i in range(1, 108):  # 因为该网站有107页数据
        print("正在下载第%s页数据" % i)
        url = 'http://college.gaokao.com/schlist/p%s' % i  # 爬取高考网的信息
        res = requests.get(url)
        html = res.text
        content = BeautifulSoup(html, "html.parser")  # 解析html
        college_list = content.find('div', attrs={'class': 'scores_List'}).find_all('dl')
        items = map(parse_item, college_list)
        save_to_csv(items)
    print("数据下载完毕")


def parse_item(item):
    college_name = item.find('strong')['title']
    college_attr = item.find_all('li')
    college_site = college_attr[0].text[6:]
    college_title = college_attr[1].text[5:]
    college_type = college_attr[2].text[5:]
    college_belong = college_attr[3].text[5:]
    college_nature = college_attr[4].text[5:]
    college_website = college_attr[5].text[5:]
    result = {
        'college_name': college_name,
        'college_site': college_site,
        'college_title': college_title,
        'college_type': college_type,
        'college_belong': college_belong,
        'college_nature': college_nature,
        'college_website': college_website
    }
    return result


# 将爬取的数据保存到csv文件中
def save_to_csv(data):
    if not os.path.exists(r'college_data.csv'):
        with open('college_data.csv', 'a+', encoding='utf-8') as f:
            f.write('name,site,title,type,belong,nature,website\n')  # 列名
            for d in data:
                try:
                    # 格式化赋值
                    row = '{},{},{},{},{},{},{}'.format(d['college_name'],
                                                        d['college_site'],
                                                        d['college_title'],
                                                        d['college_type'],
                                                        d['college_belong'],
                                                        d['college_nature'],
                                                        d['college_website'])
                    f.write(row)
                    f.write('\n')
                except:
                    continue
    else:
        with open('college_data.csv', 'a+', encoding='utf-8') as f:
            for d in data:
                try:
                    row = '{},{},{},{},{},{},{}'.format(d['college_name'],
                                                        d['college_site'],
                                                        d['college_title'],
                                                        d['college_type'],
                                                        d['college_belong'],
                                                        d['college_nature'],
                                                        d['college_website'])
                    f.write(row)
                    f.write('\n')
                except:
                    continue


if __name__ == '__main__':
    get_data()

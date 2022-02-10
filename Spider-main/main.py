import logging
import random
import time
from tqdm import tqdm
from lxml import etree
import random
from xlutils.copy import copy
import xlwt, xlrd
from constant import *
from spyder import GetCompanyInfo
from write_to_excel import WriteToExcel
import requests
import re
import requests
from bs4 import BeautifulSoup
import xlutils
from constant import *
from os import error
from urllib.parse import quote
import regex as re
# Import ssl to make the program ignore the error of ssl
# certificate's validation
import ssl
import urllib.request

# 搜索企业文件名称
enterprise_search_file = r'./enterprise_search.txt'


class QCC(object):
    def __init__(self):
        self._headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }

    def GetCookie(self):
        url = 'https://www.qcc.com/web/search?key=测试'
        response = requests.get(url, headers=self._headers, allow_redirects=False)
        response.encoding = 'utf8'
        result = re.findall(r'div>您的请求ID是: <strong>\n(.*?)</strong></div>', response.text)
        if result:
            return result[0]

    def Search(self, search_keyword, index):
        url = 'https://www.qcc.com/web/search?key={}'.format(search_keyword)
        headers = self._headers
        headers['cookie'] = 'acw_tc={}'.format(self.GetCookie())
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        html = etree.HTML(response.text)
        com_url = html.xpath('//a[@class="title copy-value"]/@href')
        for url in com_url:
            company_info = GetCompanyInfo(url)
            WriteToExcel(company_info, search_keyword, index)
            return

    def Run(self):
        index = 1
        f = open(enterprise_search_file, encoding='utf-8')
        enterprise_list = f.readlines()
        print('开始对文件进行重复检查......')
        _enterprise_list = self.remove_repeat(enterprise_list)
        f.close()
        print('去除重复后企业总数============={}'.format(len(_enterprise_list)))
        for i in tqdm(range(len(_enterprise_list))):
            self.Search(search_keyword=_enterprise_list[i], index=index)
            index += 1
            time.sleep(random.randint(90, 160))  # 间隔一段时间

    # 去除重复的名称
    def remove_repeat(self, list):
        list2 = []
        for i in list:
            name = i.replace('\n', '').replace(" ", "").replace('“', '').replace('”', '') \
                .replace('"', '').replace(')', '）').replace('(', '（').strip()
            if '' != name and not name.isspace() and name not in list2:
                list2.append(name)
            elif '' != name and not name.isspace():
                print('存在重复企业名称==========={}'.format(name))
        # print(list2)
        return list2


if __name__ == '__main__':
    t = QCC()
    t.Run()

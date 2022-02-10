# This file stores constants of regex and browser header,
# Once the html structure of the target website is changed
# we should update the regex.

# regex
import random

REGEX_ARTIFICIAL_PERSON = r'<span class="val"><span class="max-130"><span><a href=".*" target="_blank">(.*)</a></span></span>'

REGEX_COMPANY_TYPE = r'</td> <td>(.*)</td> <td class="tb">营业期限'

REGEX_ADDRESS = r'<a class="copy-value" data-v-.*>(.?)\</a>'

REGEX_GENERAL_MANAGER = r'</td> <td class="left"><div class="td-coy"><span class="headimg"><span class="app-auto-logo" style="width:40px;height:40px;"><span style="font-size:18px;line-height:39px;width:40px;height:40px;border-radius:4px;background-color:#E79177;">.*</span></span></span> <span class="cont"><span class="name"><a href=".*" target="_blank">(.*)</a></span>.*</span> <span class="foot"><a class="war-link"><i aria-label="icon.*" class="anticon anticon-icon-icon_guanlianqiye aicon aicon-guanlianqiye"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false"><use xlink:href=".*"></use></svg></i> <span>关联.*家企业 &gt;</span></a></span> </div></td><td><span>.*董事.*</span></td><td class="filter-blur"><div>.*</div></td><td class="filter-blur"><div>.*</div></td></tr> <tr> <td class="tx">'

REGEX_SUPERVISOR = r'<em>姓名: <a href=".*" target="_blank">(.*?)</a>; 证件号码: .*; 职位.*监事.*</em></span>'

REGEX_FINACIAL_MANAGER = r'<em>现</em>财务负责人姓名:<em>(.*)\,.*</em>财务负责人固定电话'

REGEX_CREDIT_CODE = r'''统一社会信用代码：
                  <span class="val"><div class="app-copy-box copy-hover-item" data-v-.*><span class="copy-value" data-v-.*>(.*)</span> <span class="app-copy copy-button-item"'''

REGEX_ESTABLISH_TIME = r'class="tb">成立日期 <i aria-label=".*" class=".*"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false"><use xlink:href=".*"></use></svg></i></td> <td width="20%">(.*)</td></tr> <tr><'

# string macros
STRING_ADDRESS = '地址'
STRING_NO_ADDRESS = '没有找到地址'
STRING_ARTIFICIAL_PERSON = '法人'
STRING_NO_ARTIFICIAL_PERSON = '没有找到法人'
STRING_COMPANY_TYPE = '企业类型'
STRING_NO_COMPANY_TYPE = '没有找到企业类型'
STRING_GENERAL_MANAGER = '董事'
STRING_NO_GENERAL_MANAGER = '没有找到董事'
STRING_SUPERVISOR = '监事'
STRING_NO_SUPERVISOR = '没有找到监事'
STRING_FINACIAL_MANAGER = '财务负责人'
STRING_NO_FINACIAL_MANAGER = '没有找到财务负责人'
STRING_CREDIT_CODE = '统一信用代码'
STRING_NO_CREDIT_CODE = '没有找到统一信用代码'
STRING_ESTABLISH_TIME = '成立日期'
STRING_NO_ESTABLISH_TIME = '没有找到成立日期'

# headers

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

cookies_local = [
    '_uab_collina=161403891084798829821415; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201614038910755%2C%22updated%22%3A%201614038910990%2C%22info%22%3A%201614038910758%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.google.com%22%7D; qcc_did=02216800-87c4-42b8-b128-d1e12ec0a2a7; QCCSESSID=ac518f2a0061b3468b276f1ead; acw_tc=088432be16444691644371338ed956596db6ce87e2e495a47c540ebf11; zg_did=%7B%22did%22%3A%20%22177cc37471e602-0def9206ec376c-5c3f1746-190140-177cc37471f48c%22%7D; zg_294c2ba1ecc244809c552f8f6fd2a440=%7B%22sid%22%3A%201644469391904%2C%22updated%22%3A%201644470295466%2C%22info%22%3A%201644469391909%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%7D'
]

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
]


def get_headers():
    return {
        'Host': "www.qcc.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "close",
        'User-Agent': random_user_agent(),
        # 'cookie': getGenerateCookie()
        'Cookie': random_cookie()
    }


def random_user_agent():
    return random.choice(user_agent)


def random_cookie():
    return random.choice(cookies_local)

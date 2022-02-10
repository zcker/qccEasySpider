# qccEasySpider

由于需要企查查的爬虫，在网上找了很久，要不是年久失修，要不就是功能太复杂我根本用不到，这个版本只爬取出公司名，法人和地址，在首页上的简单的应用也可以爬

## 操作

在dist目录下的exe文件可以直接运行，使用pyinstaller编译 在enterprise_search文档中写入公司名并运行写入info.xls
![1.png](https://s2.loli.net/2022/02/10/BbOzMYowu98LdXI.png)

## 修改

使用两种匹配模式，一种将HTML下载下来操作，是原来的，但是HTML对于正则不好用 所以我增加了使用requests+bs4的方法，写的很简陋，能用就行

## 结构

Spider-main  
├─ constant.py 常量，有正则有requests请求解析  
├─ dist 放生成exe的地方  
│ ├─ enterprise_search.txt  
│ ├─ info.xls  
│ ├─ main.exe  
│ └─ test.txt  
├─ enterprise_search.txt 读取搜索  
├─ img.ico  
├─ info.xls 输出  
├─ main.py 主函数  
├─ main.spec   
├─ spyder.py 爬取数据  
├─ test.txt  
└─ write_to_excel.py 输出到Excel

## 致谢

在https://github.com/HerrZCD/spider 基础上加以修改

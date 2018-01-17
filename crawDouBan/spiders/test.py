import urllib.parse
print(urllib.parse.unquote("%E6%B5%8B%E8%AF%95abc"))
a = str('\n'
          '        \n'
          '  \n'
          '  [挪] 尤·奈斯博 / 林立仁 / 湖南文艺出版社 / 2017-8 / 45.00\n'
          '\n'
          '      ')
s = a.replace('\n',"").strip()

aaa=a.split('/')
aaa.__len__()
ss= '%E5%B0%8F%E8%AF%B4'
print()
print(s)
o="<200 https://book.douban.com/tag/%E9%B2%81%E8%BF%85?type=R>"
os=o.split("/")
type1=os[os.__len__()-1].split("?")
type2=type1[0]
# print(urllib.parse.unquote(type2))
# title = '外语'
# for i in range(50).__reversed__():
#     url = 'https://book.douban.com/tag/' + title + "?start="+str(i*20)+"&type=R"
#     print(url)
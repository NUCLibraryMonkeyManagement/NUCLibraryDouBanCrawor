from scrapy import cmdline

name='douban_movie -o douban.csv'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
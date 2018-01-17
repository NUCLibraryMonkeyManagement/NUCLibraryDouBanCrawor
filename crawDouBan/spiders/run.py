from scrapy import cmdline

name='demo -o demo1.csv'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
import requests
from scrapy.selector import Selector
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="ipproxy", charset="utf8")
cursor = conn.cursor()

class GetIP(object):
    def delete_ip(self, ip):
        #从数据库中删除无效的ip
        delete_sql = """
            delete from httpbin where ip='{0}'
        """.format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True

    def judge_ip(self, ip, port):
        #判断ip是否可用
        http_url = 'https://book.douban.com/tag'
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http":proxy_url,
            }
            print(proxy_dict)
            response = requests.get(http_url, proxies=proxy_dict)
            print("baidu"+response.status_code)
        except Exception as e:
            print ("invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print ("effective ip")
                return True
            else:
                print  ("invalid ip and port")
                self.delete_ip(ip)
                return False


    def get_random_ip(self):
        #从数据库中随机获取一个可用的ip
        random_sql = """
              SELECT ip, port FROM httpbin WHERE anonymity=3 AND https='yes'
            ORDER BY RAND()
            LIMIT 1
            """
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            judge_re = self.judge_ip(ip, port)
            print(judge_re)
            print(ip_info)
            if judge_re:
                return "http://{0}:{1}".format(ip, port)
            else:
                return self.get_random_ip()


# if __name__ == "__main__":
#     get_ip = GetIP()
#     get_ip.get_random_ip()
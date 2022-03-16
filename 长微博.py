
import csv
import re
import requests
import time

# 伪装头部，防止被系统检测到是爬虫
headers = {
    'Host': 'm.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.138 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# 创建/打开一个csv文件
f = open('#神舟十二号发射圆满成.csv', 'w+', encoding='utf-8', newline='')
# 基于文件对象构建csv写入对象
csv_writer = csv.writer(f)
# 构建csv列表头
csv_writer.writerow(["用户名", "微博文本", "发布时间"])

# 爬取宇航员在太空吃什么#前50页热门微博
for i in range(50):
    # i从零开始输出要加1
    page = str(i + 1)
    # 构造url
    url = "https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%A5%9E%E8%88%9F%E5%8D%81%E4%BA%8C%E5%8F%B7%E5%8F%91%E5%B0%84%E5%9C%86%E6%BB%A1%E6%88%90%E5%8A%9F%23&extparam=%23%E7%A5%9E%E8%88%9F%E5%8D%81%E4%BA%8C%E5%8F%B7%E5%8F%91%E5%B0%84%E5%9C%86%E6%BB%A1%E6%88%90%E5%8A%9F%23&luicode=10000011&lfid=231522type%3D1%26t%3D10%26q%3D%23%E7%A5%9E%E8%88%9F%E5%8D%81%E4%BA%8C%E5%8F%91%E5%B0%84%E5%AF%B9%E4%B8%AD%E5%9B%BD%E8%88%AA%E5%A4%A9%E6%9C%89%E4%BD%95%E9%87%8D%E5%A4%A7%E6%84%8F%E4%B9%89%23&page_type=searchall"\
          "&page=" + str(page) + " "
    response = requests.get(url, headers=headers)
    weibo_data = response.json()

    for mblog_data in weibo_data['data']['cards']:
        try:
            # 获取微博用户名
            user_id = mblog_data['mblog']['user']['screen_name']
            # 获取微博文本内容
            content_data = mblog_data['mblog']['text']
            # 获取该微博字数
            textlength_data = mblog_data['mblog']['textLength']
            # 获取该条微博id
            weibo_id = mblog_data['mblog']['id']
            # 获取微博发布时间
            date = mblog_data['mblog']['created_at']

            # 判断当微博字数大于140时为长微博
            if textlength_data > 140:
                # 构造长微博详情页JSON数据的URL
                weibo_detail_url = "https://m.weibo.cn/statuses/extend?id=" + str(weibo_id)
                response = requests.get(weibo_detail_url, headers=headers)
                weibo_detail_data = response.json()
                # 获取长微博完整文本
                long_text = weibo_detail_data['data']['longTextContent']
                # 过滤网页字符
                p = re.compile('</?\\w+[^>]*>')
                long_text_data = p.sub('', long_text)
                # 写入CSV文件
                csv_writer.writerow([user_id, long_text_data, date])
                # 显示爬取结果
                print(user_id, long_text_data, date)
                # 非长微博时else正常爬取
            else:
                p = re.compile('</?\\w+[^>]*>')
                content_data = p.sub('', content_data)
                # 将数据写入到csv文件中
                csv_writer.writerow([user_id, content_data, date])
                # 显示爬取结果
                print(user_id, content_data, date)

        except:
            print("发生了一点问题")
    # 停顿3s
    time.sleep(3)

# 关闭csv文件
f.close()
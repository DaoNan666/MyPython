import requests
import time
import csv
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363 '
}
url = 'https://www.zhihu.com/api/v4/questions/57230324/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bsettings.table_of_content.enabled%3B&limit=5&offset=0&platform=desktop&sort_by=default'
sign_end = "False"
while sign_end == "False":
    html = requests.get(url, headers=headers)
    time.sleep(3)
    zhihu_data = html.json()
    sign_end = str(zhihu_data['paging']['is_end'])
    for answers_data in zhihu_data['data']:
        answer_name = answers_data['author']['name']
        answer_content = answers_data['content']
        r = re.compile('</?\\w+[^>]*>')  # html标签
        answer_content = r.sub('', answer_content)
        print(answer_name)
        print(answer_content)

        with open('你高中时最美好的一个瞬间是什么？.csv', 'a', newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([answer_name, answer_content])
    url = zhihu_data['paging']['next']
else:
    print("已爬取全部答案")
import collections  # 词频统计
import jieba  # 结巴分词
import wordcloud  # 词云生成
import matplotlib.pyplot as plt  # 图像展示
import numpy as np   # 数据处理
from PIL import Image  # 图像处理

# 文件路径
path_txt = 'D:/桌面/barrages.txt'
# 打开txt文件
text = open(path_txt, encoding="utf-8").read()

# 文本分词，精确模式
seg_list_exact = jieba.cut(text, cut_all=False)

object_list = []

# 自定义去除词
remove_words = [u'的', u'给', u'和', u'并', u'是', u'你', u'人', u'不', u'去', u'都', u'才', u'又', u'那',
                u'从', u'过', u'中', u'做', u'了', u'但', u'们', u'在', u'也', u'很', u'让', u'他', u'被',
                u'啥', u'我', u'有', u'等', u'对', u'及', u'年', u'后', u'万', u'把', u'时', u'来', u'为',
                u'啊', u'能', u'或', u'会', u'说', u'这', u'要', u'就', u'还', u'而', u'着', u'到', u'好',
                u'最', u'多', u'上', u'想', u'看','，','。','？','”','！','|','）','“','（','一个','吧','里',
                '现在','没有','就是','一下','那个','还是','所以','起来','那么','这么','可以','因为','其实','之后',
                '时候','写','问','，']

# 循环读出每个分词，将不在去除词中的分词添加到列表
for word in seg_list_exact:
    if word not in remove_words:
        object_list.append(word)

# 对分词进行词频统计
word_counts = collections.Counter(object_list)
# 获取前100最高频的词
word_counts_top100 = word_counts.most_common(100)
print(word_counts_top100)  # 输出检查

mask = np.array(Image.open(r'D:\桌面\Picture\xc_2.jpg'))

# 词云设置
wc = wordcloud.WordCloud(
    # 设置字体格式防止乱码
    font_path='D:/Python/字体/simsun.ttf',
    # 设置背景颜色
    background_color="white",
    # 设置最多显示词数
    max_words=150,
    # 设置字体最大值
    max_font_size=300,
    mask=mask
)
# 生成词云
wc.generate_from_frequencies(word_counts)
# 获取背景图颜色方案
image_colors = wordcloud.ImageColorGenerator(mask)
# 将背景图颜色方案给词云
wc.recolor(color_func=image_colors)
# 显示词云
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 图像显示
plt.show()
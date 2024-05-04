###############################################################
# import python libraries
###############################################################
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np
import streamlit as st
import pandas as pd

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Text Analysis -  HUMA5630-Digital Humanities - project-2024-group-3",
    page_icon="⛰️", 
    layout="wide",
    initial_sidebar_state="expanded", 
)
st.caption("HUMA5630 Digital Humanities - Group 3")
###############################################################
# Background Image
###############################################################
# 设置页面背景图层
st.markdown(
    """
    <style>
    .header-container {
        background-image: url(https://img95.699pic.com/photo/40195/1356.jpg_wh300.jpg);
        background-size: cover;
        background-repeat: no-repeat;
        padding: 20px;
        color: white;
        text-align: center;
    }
    .header-container h1 {
        font-size: 40px;
        color: white;
        margin-bottom: 10px;
    }
    .header-container p {
        font-size: 20px;
        color: white;
        text-align: center;
        display: inline-block;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# 显示标题文字和副标题
st.markdown('<div class="header-container"><h1>About This Text</h1>', unsafe_allow_html=True)
###############################################################
# page content
###############################################################

st.markdown("")
st.markdown("The 'Classic of Mountains and Seas' is a renowned ancient Chinese text that delves into the rich tapestry of mythical geography, creatures, and cultures. Compiled over centuries, it stands as a testament to the profound imagination and curiosity of ancient Chinese scholars. Within its pages lie a mesmerizing blend of folklore, cosmology, and geography, offering readers a window into the imaginative worldviews of ancient China.")
st.markdown("The book has more than 38,000 words in total and is divided into eighteen sections; it describes over 550 mountains and 300 channels.")
st.markdown("---")


###############################################################
# Data --WordCloud
###############################################################
word_frequencies = {
    '曰': 551,
    '名曰': 309,
    '東': 211,
    '之山': 183,
    '流注': 179,
    '其狀': 174,
    '山': 125,
    '西': 115,
    '鳥': 109,
    '獸': 104,
    '草木': 101,
    '于': 92,
    '北': 92,
    '水出': 90,
    '南': 84,
    '黃': 81,
    '三百里': 74,
    '人面': 74,
    '水': 64,
    '其下': 64,
    '其陽': 63,
    '注于': 62,
    '東南': 61,
    '北流': 59,
    '食': 58,
    '其上': 58,
    '皆': 55,
    '二百里': 51,
    '穀': 50,
    '其木多': 50,
    '其音': 49,
    '出': 44,
    '狀': 43,
    '蛇': 41,
    '金玉': 39,
    '里': 39,
    '草': 39,
    '大荒': 39,
    '金玉其': 38,
    '五百里': 37,
    '西南': 36,
    '之國': 36,
    '至于': 35,
    '二十里': 35,
    '有人': 35,
    '玉': 34,
    '西北': 34,
    '之中': 34,
    '木': 32,
    '赤': 32,
    '之首': 32,
    '于河': 31,
    '有山': 31,
    '見則': 30,
    '出于': 30,
    '三百': 29,
    '五十里': 29,
    '出焉': 28,
    '其獸': 28,
    '尾': 27,
    '爰': 27,
    '七十里': 26,
    '杻': 26,
    '其祠': 26,
    '陰多': 25,
    '多玉': 25,
    '白': 24,
    '東北': 24,
    '四百里': 23,
    '瘞': 23,
    '天下': 23,
    '喙': 23,
    '彘': 22,
    '首': 22,
    '三十里': 22,
    '之水出': 22,
    '臺': 22,
    '流沙': 22,
    '長': 21,
    '山上': 21,
    '崑': 21,
    '崙': 21,
    '牛': 20,
    '赤水': 20,
    '下多': 20,
    '其鳴': 20,
    '其草': 20,
    '居': 20,
    '海': 19,
    '糈': 19,
    '琈': 19,
    '國': 19,
    '白玉': 18,
    '三百五十里': 18,
    '殺': 18,
    '毛': 18,
    '身': 17,
    '有神': 17,
    '生': 17,
    '其東': 17
}



# 加载云朵形状的图片
cloud_mask = np.array(Image.open('./images/shanfeng.png'))

# 创建词云对象并配置相关参数
wordcloud = WordCloud(font_path='./data/NotoSansTCBlack.ttf', background_color='white', mask=cloud_mask)

# 生成词云图
wordcloud.generate_from_frequencies(word_frequencies)

# 根据图片颜色生成词云图的颜色
image_colors = ImageColorGenerator(cloud_mask)
wordcloud.recolor(color_func=image_colors)

# 显示词云图
st.title("Word Cloud")
st.markdown("As a geographical chronicle, there are many high-frequency words which are descriptive, such as \"name as\", as well as east, south, and west which describe geographical directions.")
fig, ax = plt.subplots(figsize=(80, 50), dpi=300)  # Adjust figsize and dpi for clarity
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

##############################################################
# Data --TextCategory


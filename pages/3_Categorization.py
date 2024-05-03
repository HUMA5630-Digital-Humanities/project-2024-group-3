###############################################################
# import python libraries
###############################################################
import streamlit as st
import pandas as pd
import plotly.express as px

###############################################################
# page info 
###############################################################

st.set_page_config(
    page_title="Categorization of Mythical Creatures -  HUMA5630-Digital Humanities - project-2024-group-3",
    page_icon="⛰️", 
    layout="wide",
    initial_sidebar_state="expanded", 
)

###############################################################

# background image
# Reference: https://discuss.streamlit.io/t/background-image-is-not-getting-dispalyed/53325/2

###############################################################
import base64
def get_image_data(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        encoded_image_data = base64.b64encode(image_data).decode('utf-8')
    return encoded_image_data

# Specify the path to your local image file
image_path = './images/backgroundimage.jpeg'

# Get the base64-encoded image data
image_data = get_image_data(image_path)

# FYI, you can customize the style of text
customStyleTitle = '<h1 style="font-family: serif; color:#684905; font-size: 50px;">Let\'s Explore Different Types of Mythical Creatures in the Classic of Mountains and Rivers!</h1>'
st.markdown(customStyleTitle, unsafe_allow_html=True)

# Set the background image
background_image = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url(data:image/jpeg;base64,{image_data});
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
}}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


###############################################################
# page content
###############################################################

st.title("Let's Explore Different Types of Mythical Creatures in the Classic of Mountains and Rivers!")

###############################################################
# Data
###############################################################
filepath = './data/mythical_creatures.xlsx'
data = pd.read_excel(filepath, sheet_name='Sheet1')

###############################################################
# Count
###############################################################
st.markdown("---")
st.markdown("## Total number of mythical creatures in the book of 《山海百靈》")

creaturesnum = len(data)
st.metric(label="No. of mythical creatures", value=creaturesnum)
st.write(f'There are a total of {creaturesnum} mythical creatures in this book')

###############################################################
# Chart
###############################################################
st.markdown("## Chart")

# Count the occurrences of each language
categories_counts = data['篇章'].value_counts()

# Create a DataFrame from the counts
df_categories = pd.DataFrame({'篇章': categories_counts.index, 'Count': categories_counts.values})

# Create a pie chart using Plotly Express
fig = px.pie(df_categories, values='Count', names='篇章', title='Distribution of Mythical Creatures')

# Display the pie chart in Streamlit
st.plotly_chart(fig)


st.markdown("---")

###############################################################
# Categorization
###############################################################
st.markdown("## Categorization")

# 读取Excel文件
filepath = './data/mythical_creatures.xlsx'
df = pd.read_excel(filepath, sheet_name='Sheet1')

# 按篇章分组
grouped = df.groupby('篇章')

# 获取所有篇章
chapters = df['篇章'].unique()

# 创建一个下拉菜单，用于选择篇章
selected_chapter = st.selectbox('选择篇章', chapters)

st.markdown("#")

# 根据选择的篇章显示对应的異獸
selected_df = grouped.get_group(selected_chapter)
for index, row in selected_df.iterrows():
    # use column layout for better layout
    colcount = st.columns([3, 7]) 
    count = 200
    with colcount[0]: 
        st.subheader(row['名字'])
        image_path = f'./images/creatures_images/{index+1}.png'  # 根据索引值构建图片文件路径
        st.image(image_path, width=150)
        st.write( row['形容'])
    with colcount[1]:
        st.write('原文：', row['原文'])
        st.write('譯釋：', row['譯釋'])
    st.write('---')
import streamlit as st
import numpy as np
import pandas as pd
import PIL
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!!'
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く1')
expander1.write('問い合わせ内容を書く1-2')
expander1.write('問い合わせ内容を書く1-3')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容を書く3')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0, 100, 50)

# 'あなたの趣味:', text
# 'コンディション', condition

# st.write('Display Image')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('ema.jpg')
#     st.image(img, caption='ema', use_column_width=True)
# チェックボックスはIF分を使うことでチェックを入れる（True）と表示される.IF分は:と４マス開ける


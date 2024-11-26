import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')

st.write('Interactive Widgets')

#left_colmn, right_column = st.beta_columns(2)
#left_columns.button('右カラムに文字を表示')

text =  st.text_input('あなたの趣味を教えて下さい。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text
'コンディション:', condition

if st.checkbox('Show Image'):
    img = Image.open('カツオイラスト1.jpg')
    st.image(img, caption='Katsuo',use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns= ['lat', 'lon']
)

st.dataframe(df.style.highlight_max(axis=0))



#st.map(df)
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('キャッシュフローモデリング')
st.caption('これはテストアプリです')

col1, col2 = st.columns(2)

with col1:
    

    st.subheader('自己紹介')
    st.text('よければチャンネル登録よろしくお願いします。')

    st.write('Interactive Widgets')

    #left_colmn, right_column = st.beta_columns(2)
    #left_columns.button('右カラムに文字を表示')

    text =  st.text_input('あなたの趣味を教えて下さい。')
    condition = st.slider('あなたの今の調子は？', 0, 100, 50)

    'あなたの趣味:', text
    'コンディション:', condition

    #画像
    if st.checkbox('Show Image'):
        img = Image.open('カツオイラスト1.jpg')
        st.image(img, caption='Katsuo',width=200)
        
    with st.form(key='profile_form'):       
        #テキストボックス
        name = st.text_input('名前')
        address = st.text_input('e_mail_address') 
        
        #セレクトボックス
        request_category = st.radio(
            '問い合わせ内容',
            ('ご質問','仕事のご依頼')
        )
        
        #問い合わせ内容
        contact = st.text_area('問い合わせ内容')
        
        
        #ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        
        if submit_btn:
            st.text(f'ようこそ！{name}さん！')
            st.text(f'問い合わせ内容：{request_category}')
            
            print(name)
            print(address)
            print(request_category)
            print(contact)
    
with col2:
    #データ分析関連    
    df = pd.read_excel('損益シミュレーションモデル.xlsx',sheet_name='CF')
    st.dataframe(df)




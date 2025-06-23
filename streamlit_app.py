import streamlit as st

name = st.text_input("名前を入力してください")
st.write("こんにちは", name)

#uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")
#import pandas as pd
#if uploaded_file is not None:
#    #df = pd.read_csv(path, sep=",", encoding = 'utf-8') 
#    df = pd.read_csv(
#        uploaded_file,
#        #sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
#        sep=",",
#        engine='python',
#        na_values='-',
#        header=None)
#
#st.markdown('### アクセスログ（先頭5件）')
#st.write(df.head(5))

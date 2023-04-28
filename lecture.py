# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from utils import p_lans
from PIL import Image

# Data VIZ
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("Hello World")

    # text
    st.text('This is so {}'.format("good"))

    # Header
    st.header('This is Header')

    # subheader
    st.subheader('This is subHeader')

    # Markdown
    st.markdown('## This is Markdown')

    # 색상이 들어간 텍스트 feature
    st.success('성공')
    st.warning('경고')
    st.info('정보와 관련된 탭')
    st.error('에러 메세지')
    st.exception('예외처리')

    # st.write()
    st.write('일반텍스트')
    st.write(1 + 2)
    st.write(dir(str))

    st.title(':sunglasses:')

    # help
    st.help(range)
    st.help(st.title)

    # 데이터 불러오기
    iris = pd.read_csv('data/iris.csv')

    st.title("IRIS 테이블")
    st.dataframe(iris, 200, 100)  # Height, Width

    st.title('table()')
    st.write(iris)

    myCode = """
    def hello():
        print("hi")
    """
    st.code(myCode, language="Python")

    # 위젯, button 기능활용
    name = "Kwon"
    if st.button('Submit'):
        st.write(f"name : {name.upper()}")

    # RadioButton
    s_state = st.radio('Status', ('활성화', '비활성화'))
    if s_state == '활성화':
        st.success('활성화 상태')
    else:
        st.error('비활성화 상태')

    # check Box
    if st.checkbox('show/hide'):
        st.text('무언가를 보여줘!!')

    # Select Box

    choice = st.selectbox('프로그래밍 언어', p_lans)
    st.write(f'{choice} 언어를 선택함')

    # multiple selection
    lans = ('영어', '일본어', '중국어', '독일어')
    myChoice = st.multiselect('언어 선택', lans, default='중국어')
    # pandas['문자열컬럼'].isin(myChoice)
    st.write("선택", myChoice)

    # Slider
    age = st.slider('나이', 1, 120)
    st.write(age)

    # 이미지 가져오기
    img = Image.open("data/image_01.jpg")
    st.image(img)

    url = "data:image/jpeg;base64,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"
    st.image(url)

    # 비디오 출력
    with open('data/secret_of_success.mp4', 'rb') as rb:
        video_file = rb.read()
        st.video(video_file, start_time=1)

    # 오디오 출력
    with open('data/song.mp3', 'rb') as rb:
        audio_file = rb.read()
        st.audio(audio_file, format="audio/mp3")

    fig = px.scatter(data_frame=iris,
                     x='sepal_length',
                     y='sepal_width')
    st.plotly_chart(fig)

    choice = st.selectbox('프로그래밍 언어', iris['species'].unique())
    # st.title(choice)

    result = iris[iris['species'] == choice].reset_index(drop=True)
    # st.dataframe(result)

    col1, col2 = st.columns([0.5, 0.5], gap='large')
    with col1:
        fig2, ax = plt.subplots()
        # ax.scatter(x=iris['petal_length'], y=iris['sepal_width'])
        sns.scatterplot(result, x='petal_length',
                        y='sepal_width')
        st.pyplot(fig2)

    with col2:
        fig3, ax = plt.subplots()
        ax.scatter(x=result['sepal_length'], y=result['sepal_width'])
        st.pyplot(fig3)


if __name__ == '__main__':
    main()
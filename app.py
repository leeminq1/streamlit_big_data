import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from st_pages import Page, show_pages, add_page_title,add_indentation


# Optional -- adds the title and icon to the current page
# add_page_title()
add_indentation()
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("app.py", "Comment", "🔥"),
        Page("./pages/age_salary.py", "연령별 임금 및 근로시간", "📣"),
    ]
)

# st.rerun()


#### session state ####
if "font" not in st.session_state:
    st.session_state.font = ''



def unique(list):
    x = np.array(list)
    return np.unique(x)

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/customFonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)



def main_text():
    st.header("통계청 데이터 기반 시각화")
    st.markdown("**자료갱신일:** 2023-12-26")
    st.text('Streamlit 시각화 공부를 위해 통계청 데이터 기반 시각화 r2')


def data_index_btn():
    data_list = ['연령별 임금 및 근로시간', '연령별 임금 및 근로시간2']
    clicked_buttons = [False] * len(data_list)  # 각 버튼의 클릭 여부를 저장하는 리스트

    for i, data in enumerate(data_list):
        clicked_buttons[i] = st.button(f'{data}')

    # 각 버튼의 클릭 여부를 확인하여 이벤트 처리
    for i, data in enumerate(data_list):
        if clicked_buttons[i]:
            # 페이지 이동을 위한 URL 설정
            if data == '연령별 임금 및 근로시간':
                page_url = '/pages/age_salary.py'
                st.switch_page(page_url) ### page 이동 ###

            elif data == '연령별 임금 및 근로시간2':
                page_url = ''




def main():

    ### loading 시 main page로 이동 ###


    fontRegistered()
    fontNames = [f.name for f in fm.fontManager.ttflist]
    default_font_index = fontNames.index("Malgun Gothic") if "Malgun Gothic" in fontNames else 0
    #### session state에 값이 없으면 default_font_index로 설정하고, 값이 잇으면 session state에서 fontNames에서 선택한 font의 index를 찾아서 표시함
    fontname = st.selectbox("폰트 선택", fontNames, index=fontNames.index(st.session_state.font) if st.session_state.font!='' else default_font_index)

    ### font 이름이 변경 되었을 때 감지 ###
    if st.session_state.font != fontname:
        if "font" in st.session_state:
            st.session_state.font = fontname


    main_text()
    data_index_btn()






if __name__ == '__main__':
    main()

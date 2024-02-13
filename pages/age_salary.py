import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


#### session state ####
## font ##
if "font" not in st.session_state:
    st.session_state.font = ''

## dataFrame ##
### 전체 근로자 ###
if 'df_age_salary' not in st.session_state:
    df_age_salary_path = './data/연령별_임금_및_근로시간_전체근로자.csv'
    df_age_salary = pd.read_csv(df_age_salary_path, encoding='utf-8-sig')
    st.session_state.df_age_salary = df_age_salary

### 정규 근로자 ###
if 'df_age_full_time' not in st.session_state:
    df_age_full_time_path = './data/연령별_임금_및_근로시간_정규근로자.csv'
    df_age_full_time = pd.read_csv(df_age_full_time_path, encoding='utf-8-sig')
    st.session_state.df_age_full_time = df_age_full_time

### 비정규 근로자 ###
if 'df_age_not_full_time' not in st.session_state:
    df_age_not_full_time_path = './data/연령별_임금_및_근로시간_비정규근로자.csv'
    df_age_not_full_time = pd.read_csv(df_age_not_full_time_path, encoding='utf-8-sig')
    st.session_state.df_age_not_full_time = df_age_not_full_time



### graph ###
def draw_graph(select_cols,new_df):
    plt.rcParams['font.family'] = st.session_state.font

    fig, axes = plt.subplots(nrows=len(select_cols), ncols=1)
    fig.patch.set_facecolor('xkcd:white')
    fig.set_size_inches(9, 7);
    plt.subplots_adjust(hspace=0.6)

    for idx, col in enumerate(select_cols):

        ### 총 근로 시간 그래프
        sns.barplot(x='나이구분', y='값', data=new_df.loc[new_df['고용형태'] == f'{col}'], hue='날짜', ax=axes[idx],
                    palette='RdBu', width=0.6)  # 색상 지정
        axes[idx].set(title=f'{col}', ylabel=f'{col}', xlabel='연령대')
        axes[idx].grid()

        # 각 막대에 값을 표시하는 로직
        for p in axes[idx].patches:
            height = p.get_height()
            axes[idx].annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2., height),
                               ha='center', va='center', fontsize=9, color='black', xytext=(0, 5),
                               textcoords='offset points')
        # 범례 위치 조정
        max_value = new_df.loc[new_df['고용형태'] == f'{col}', '값'].max() * 1.5
        axes[idx].set_ylim(idx, max_value)
        axes[idx].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    st.pyplot(fig)

def multi_select_btn():
    col1, col2 = st.columns([2,1])

    # 라벨을 숨기기 위해 빈 텍스트 상자를 만듭니다.
    with col1:
        select_cols = st.multiselect('항목 선택',
            options=st.session_state.df_age_salary['고용형태'].unique(),
            max_selections=3, placeholder='통계자료를 선택해 주세요',label_visibility="collapsed")

    # 버튼을 아래로 정렬하여 배치합니다.
    with col2:
        select_btn = st.button('시각화', key="visualization_button")

    if select_btn:
        ### graph 생성 ##
        st.subheader('전체근로자')
        new_df = st.session_state.df_age_salary
        draw_graph(select_cols,new_df)

        st.subheader('정규근로자')
        new_df = st.session_state.df_age_full_time
        draw_graph(select_cols,new_df)

        st.subheader('비정규근로자')
        new_df = st.session_state.df_age_not_full_time
        draw_graph(select_cols,new_df)





def main():

    # 페이지 제목 설정
    st.title('📣연령별 임금 및 근로시간')


    multi_select_btn()




if __name__ == "__main__":
    main()
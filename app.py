import streamlit as st
import random
import time

st.set_page_config(page_title="로또 생성기", page_icon="🎰")
st.title("💰 대표님의 로또 1등 기원 머신")

st.markdown("---")
if st.button("🚀 이번 주 대박 번호 뽑기", use_container_width=True):
    with st.spinner("우주의 기운을 모으는 중..."):
        time.sleep(1) # 긴장감을 위한 1초 대기
        
        # 6개 번호 추출
        lotto_numbers = random.sample(range(1, 46), 6)
        lotto_numbers.sort()
        
        # 예쁘게 보여주기
        st.success(f"✨ 이번 주 행운의 번호: {lotto_numbers}")
        st.balloons()

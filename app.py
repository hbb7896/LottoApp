import streamlit as st
import random
import time

st.set_page_config(page_title="로또 5게임 생성기", page_icon="🎰")
st.title("💰 대표님의 로또 1등 기원 머신")

st.markdown("---")
# 버튼 이름도 5게임으로 변경!
if st.button("🚀 이번 주 대박 번호 뽑기 (5게임)", use_container_width=True):
    with st.spinner("우주의 기운을 5배로 모으는 중..."):
        time.sleep(1) # 긴장감 조성
        
        st.subheader("🎉 1등 당첨을 미리 축하드립니다!")
        
        # 5번 반복해서 뽑기
        for i in range(1, 6):
            lotto_numbers = random.sample(range(1, 46), 6)
            lotto_numbers.sort() # 오름차순 정렬
            
            # 1게임, 2게임... 보기 좋게 출력
            st.success(f"✨ [{i}게임] 행운의 번호:  {lotto_numbers}")
            
        st.balloons() # 풍선 축하!

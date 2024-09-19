import streamlit as st

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 0

# 페이지 설정을 가장 먼저 호출
st.set_page_config(layout="centered")

# 페이지 0
if st.session_state.page == 0:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("관리자 모드", key="admin_mode_0"):
            st.session_state.page = 3
        if st.button("신규 등록", key="user_mode_0"):
            st.session_state.page = 4

    with col2:
        st.markdown("<h2 style='text-align: center;'>지문을 인식해 주세요.</h2>", unsafe_allow_html=True)

    st.write(" ")

# --------------------------------------------------------------------------

# 페이지 1
elif st.session_state.page == 1:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("관리자 모드", key="admin_mode_1"):
            st.session_state.page = 3

    name = st.text_input("이름을 입력하세요:")

    with col2:
        st.write(f"안녕하세요, {name}님!")

    st.write(" ")

# --------------------------------------------------------------------------

# 페이지 2
elif st.session_state.page == 2:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("관리자 모드", key="admin_mode_2"):
            st.session_state.page = 3

    with col2:
        st.write(f"사용자를 찾을 수 없습니다.")

    st.write(" ")

# --------------------------------------------------------------------------

# 페이지 3 (관리자 모드)
elif st.session_state.page == 3:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("사용자 모드", key="user_mode_3"):
            st.session_state.page = 0

    with col2:
        st.markdown("<h2 style='text-align: center;'>지문을 인식해 주세요.</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("신규 등록", key="new_registration"):
            st.session_state.page = 4

        uploaded_file = st.file_uploader("파일 업로드", label_visibility="collapsed")
        if uploaded_file is not None:
            st.image(uploaded_file, use_column_width=False)
        else:
            st.markdown("<div style='border: 1px solid black; width: 100%; height: 300px;'></div>", unsafe_allow_html=True)

    with col3:
        st.button("파일 업로드", key="file_upload_3")

    st.write(" ")
    
    col_center = st.columns([1, 3, 1])[2]
    with col_center:
        if st.button("다음", key="next_3"):
            st.session_state.page = 6

# --------------------------------------------------------------------------

# 페이지 4
elif st.session_state.page == 4:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("사용자 모드", key="user_mode_4"):
            st.session_state.page = 0

    with col2:
        st.markdown("<h2 style='text-align: center;'>신규 등록</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.button("지문을 입력하세요.", key="input_fingerprint")

        uploaded_file = st.file_uploader("파일 업로드", label_visibility="collapsed")
        if uploaded_file is not None:
            st.image(uploaded_file, use_column_width=True)
        else:
            st.markdown("<div style='border: 1px solid black; width: 100%; height: 300px;'></div>", unsafe_allow_html=True)

    with col3:
        st.button("파일 업로드", key="file_upload_4")

    st.write(" ")

    col_center = st.columns([1, 3, 1])[2]
    with col_center:
        if st.button("다음", key="next_4"):
            st.session_state.page = 5

# --------------------------------------------------------------------------

# 페이지 5
elif st.session_state.page == 5:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("사용자 모드", key="user_mode_5"):
            st.session_state.page = 0

    with col2:
        st.markdown("<h2 style='text-align: center;'>신규 등록</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.button("인식 되었습니다! 이름을 입력해 주세요.", key="recognition_success")

    st.write(" ")

    col_center = st.columns([1, 3, 1])[2]
    with col_center:
        if st.button("완료", key="finish"):
            st.session_state.page = 3

# --------------------------------------------------------------------------

# 페이지 6
elif st.session_state.page == 6:
    col1, col2, col3 = st.columns([2, 4, 2])

    with col1:
        if st.button("사용자 모드", key="user_mode_6"):
            st.session_state.page = 0

    with col2:
        st.markdown("<h2 style='text-align: center;'>검색 중..</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.write("<div style='width: 100px; height: 200px; border: 2px solid black;'></div>", unsafe_allow_html=True)

    st.write(" ")

    col_center = st.columns([1, 3, 1])[2]
    with col_center:
        if st.button("다음", key="next_6"):
            st.session_state.page = 7

# --------------------------------------------------------------------------

# 페이지 7
elif st.session_state.page == 7:
    col1, col2, col3 = st.columns([2, 4, 2])

    with col1:
        if st.button("사용자 모드", key="user_mode_7"):
            st.session_state.page = 0

    with col2:
        st.markdown("<h2 style='text-align: center;'>검색 중..</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.write("<div style='width: 100px; height: 200px; border: 2px solid black;'></div>", unsafe_allow_html=True)

    st.write(" ")

    col_center = st.columns([1, 3, 1])[2]
    with col_center:
        if st.button("완료", key="finish_7"):
            st.session_state.page = 0

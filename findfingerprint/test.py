import streamlit as st
from PIL import Image
import os
import time
from fingerprint_recognition import find_best_match  # 유사도 계산 모듈 임포트

def app():
    # Initialize session state if not already done
    if 'page' not in st.session_state:
        st.session_state.page = 0

    # Helper function to handle button logic
    def navigate(page_num):
        st.session_state.page = page_num

    # Function to create top bar with navigation button
    def top_bar():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            img = Image.open('C:/archive/titleBig.png')
            st.image(img)

        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            if st.session_state.page == 3:
                if st.button("사용자 모드"):
                    navigate(0)
            # else:
            #     if st.button("관리자 모드"):
            #         navigate(3)

    # Function to render the centered title
    def render_title(title):
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>{title}</h2>", unsafe_allow_html=True)

    # Main layout for different pages
    if st.session_state.page == 0:
        top_bar()
        render_title("&nbsp;&nbsp;&nbsp;&nbsp;지문을 인식해 주세요.")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            img = Image.open('C:/archive/testing_fingerprint.png')
            st.image(img)

        st.write(" ")

        col1, col2, col3 = st.columns([2.15, 1, 2])
        with col2:
            if st.button("지문 업로드"):
                navigate(8)

        st.write(" ")

        col_center = st.columns([1, 3, 1])[2]
        with col_center:
            if st.button("다음"):
                navigate(6)

    elif st.session_state.page == 1:
        top_bar()
        st.write(" ")

        # 데이터셋 경로 설정
        dataset_path = 'C:/archive/dataset_fingerprint'  # 적절한 경로로 수정하세요
        if os.path.exists(dataset_path):
            all_files = os.listdir(dataset_path)  # 데이터셋의 모든 지문 목록 가져오기

            # 유사도 검사 결과에서 best_match와 best_similarity 가져오기
            best_match = st.session_state.get('best_match', None)  # 세션 상태에서 best_match 가져오기

            # # 디버깅 메시지 출력
            # st.write(f"Best match from session: {best_match}")
            
            # best_match가 None이 아닐 경우에만 처리
            if best_match is not None and best_match in all_files:  # best_match가 존재하고 데이터셋에 있는지 확인
                name = best_match[:9]  # best_match를 name으로 설정
                
                col1, col2, col3 = st.columns([1, 3, 1])
                with col2:
                    render_title(f"Welcome, {name}! ")  # 유사도 점수도 함께 표시
            else:
                render_title("유사한 지문을 찾을 수 없습니다.")
        else:
            render_title("지정된 데이터셋 경로가 존재하지 않습니다.")

        
    elif st.session_state.page == 2:
        top_bar()
        render_title("사용자를 찾을 수 없습니다.")
        st.write(" ")

    elif st.session_state.page == 3:
        top_bar()
        render_title("&nbsp;&nbsp;&nbsp;&nbsp;지문을 인식해 주세요.")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("신규 등록"):
                navigate(4)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.markdown("<div style='border: 1px solid white; width: 100%; height: 300px;'></div>", unsafe_allow_html=True)

        st.write(" ")

        col1, col2, col3 = st.columns([2.15, 1, 2])
        with col2:
            if st.button("지문 업로드"):
                navigate(9)

        st.write(" ")

        col_center = st.columns([1, 3, 1])[2]
        with col_center:
            if st.button("다음"):
                navigate(6)

    elif st.session_state.page == 4:
        top_bar()
        render_title("신규 등록")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.write("지문을 입력하세요.")
            uploaded_file = st.file_uploader("지문 업로드", label_visibility="collapsed")
            if uploaded_file is not None:
                st.image(uploaded_file, use_column_width=True)
            else:
                st.markdown("<div style='border: 1px solid white; width: 100%; height: 300px;'></div>", unsafe_allow_html=True)

        st.write(" ")
        col_center = st.columns([1, 3, 1])[2]
        with col_center:
            if st.button("다음"):
                navigate(5)

    elif st.session_state.page == 5:
        top_bar()
        render_title("신규 등록")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.button("인식 되었습니다! 이름을 입력해 주세요.")

        st.write(" ")
        col_center = st.columns([1, 3, 1])[2]
        with col_center:
            if st.button("완료"):
                navigate(3)

    elif st.session_state.page == 6 or st.session_state.page == 7:
        top_bar()
        render_title("6, 다음 페이지 7")

        # best_match_list와 other_files 변수를 session_state에 저장
        best_match_list = st.session_state.get('best_match_list', [])
        other_files = st.session_state.get('other_files', [])

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.write("<div style='width: 100px; height: 200px; border: 2px solid white;'></div>", unsafe_allow_html=True)

        st.write(" ")
        col_center = st.columns([1, 3, 1])[2]
        with col_center:
            st.write("유사한 지문:")
            col_left, col_right = st.columns(2)

            with col_left:
                for file in best_match_list:
                    st.markdown(f"- {file}")  # best_match 리스트 출력

            with col_right:
                for file in other_files:
                    st.markdown(f"- {file}")  # 나머지 지문 리스트 출력


            if st.session_state.page == 6 and st.button("다음"):
                navigate(7)
            elif st.session_state.page == 7 and st.button("완료"):
                navigate(0)

    elif st.session_state.page == 8:
        top_bar()
        render_title("지문을 업로드 해주세요. 8")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            uploaded_file = st.file_uploader("지문 업로드", label_visibility="collapsed")
            if uploaded_file is not None:
                # 임시 지문로 저장
                input_image_path = "temp_image.jpg"
                with open(input_image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # 데이터셋 경로 설정 (사용자에 맞게 조정)
                dataset_path = 'C:/archive/dataset_fingerprint'  # 경로 수정
                best_match, best_similarity = find_best_match(input_image_path, dataset_path)
                st.write(f'Best match: {best_match} with similarity: {best_similarity:.4f}')

                # 세션 상태에 저장
                st.session_state.best_match = best_match
                st.session_state.best_similarity = best_similarity
                
                # # 디버깅 메시지
                # st.write(f"Best match saved to session: {st.session_state.best_match}")

                # with st.spinner('Wait for it...'):
                #     time.sleep(2)  # 예시로 시간 지연
                #     st.success('Done!') 

                # 유사한 이미지 미리보기
                best_match_path = os.path.join(dataset_path, best_match)
                st.image(best_match_path, use_column_width=True)

                # best_match_list와 other_files 변수 업데이트
                all_files = os.listdir(dataset_path)
                best_match_list = [best_match] if best_match else []
                other_files = [f for f in all_files if f != best_match]
                best_similarity_list = [best_similarity] if best_similarity else []

                # 세션 상태에 저장
                st.session_state.best_match_list = best_match_list
                st.session_state.other_files = other_files
                st.session_state.best_similarity_list = best_similarity_list
                
            else:
                st.markdown("<div style='border: 1px solid white; width: 100%; height: 300px;'></div>", unsafe_allow_html=True)

        st.write(" ")
        col_center = st.columns([1, 3, 1])[2]
        with col_center:
            if st.button("완료"):
                navigate(1)


    elif st.session_state.page == 9:
        render_title("지문을 업로드 해주세요.9")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            uploaded_file = st.file_uploader("지문 업로드", label_visibility="collapsed")
            if uploaded_file is not None:
                st.image(uploaded_file, use_column_width=False)
                # 업로드된 지문을 임시 저장
                input_image_path = "temp_image.jpg"
                with open(input_image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # 데이터셋 경로 설정
                dataset_path = 'C:/archive/dataset_fingerprint'  # 경로 수정
                all_files = os.listdir(dataset_path)

                # 유사도 검사
                best_match, best_similarity = find_best_match(input_image_path, dataset_path)

                # best_match 지문 리스트와 나머지 지문 리스트 분리
                best_match_list = [best_match] if best_match else []
                other_files = [f for f in all_files if f != best_match]

                # 세션 상태에 저장
                st.session_state.best_match_list = best_match_list
                st.session_state.other_files = other_files

                with st.spinner('Wait for it...'):
                    time.sleep(5)  # 예시로 시간 지연
                    st.success('Done!') 

            else:
                st.markdown("<div style='border: 1px solid white; width: 100%; height: 300px;'></div>", unsafe_allow_html=True)

        st.write(" ")
        col_center = st.columns([1, 3, 1])[2]
        with col_center:
            if st.button("완료"):
                navigate(6)

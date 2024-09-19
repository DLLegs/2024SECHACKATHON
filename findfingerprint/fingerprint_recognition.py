import cv2
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim

def preprocess_image(image_path):
    """이미지를 로드하고 전처리합니다."""
    print(f'Trying to load image: {image_path}')  # 경로 출력
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 흑백으로 로드
    img = cv2.resize(img, (90, 90))  # 크기를 90x90으로 조정
    img = img.astype(np.float32) / 255.0  # 정규화
    return img

def calculate_similarity(img1, img2):
    """두 이미지 간의 유사도를 계산합니다."""
    # SSIM 사용하여 유사도 계산
    return ssim(img1, img2, data_range=1.0)

def find_best_match(input_image_path, dataset_path):
    """입력된 이미지와 데이터셋의 이미지 간의 유사도를 계산하여 가장 높은 유사도를 가진 이미지를 찾습니다."""
    input_image = preprocess_image(input_image_path)
    
    best_match = None
    best_similarity = -1  # 초기 유사도는 -1로 설정 (유사도는 0~1 범위)


    for filename in os.listdir(dataset_path):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.BMP'):  # 이미지 파일 형식
            dataset_image_path = os.path.join(dataset_path, filename)
            dataset_image = preprocess_image(dataset_image_path)
            
            similarity = calculate_similarity(input_image, dataset_image)
            print(f'Comparing with {filename}: Similarity = {similarity:.4f}')
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = filename

    return best_match, best_similarity

# 사용 예시
input_image_path = 'C:'  # 입력 지문 이미지 경로
dataset_path = 'C:'  # 지문 데이터셋 경로

try:
    best_match, best_similarity = find_best_match(input_image_path, dataset_path)
    print(f'Best match: {best_match} with similarity: {best_similarity:.4f}')

except ValueError as e:
    print(e)

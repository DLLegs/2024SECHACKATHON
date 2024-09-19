import cv2
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim
from lightphe import LightPHE

cs = LightPHE(algorithm_name = "Paillier", key_file = "private.txt")

algorithms = [
  "RSA",
  "ElGamal",
  "Exponential-ElGamal",
  "Paillier",
  "Damgard-Jurik",
  "Okamoto-Uchiyama",
  "Benaloh",
  "Naccache-Stern",
  "Goldwasser-Micali",
  "EllipticCurve-ElGamal"
]

cs = LightPHE(algorithm_name = algorithms[3]) #Paillier 알고리즘을 사용하겠다
cs.export_keys(target_file = "public.txt", public = True) #공개키 백업 생성
cs.export_keys(target_file = "private.txt", public = False) #비밀키 백업 생성


def preprocess_image(image_path):
    """이미지를 로드하고 전처리합니다."""
    print(f'Trying to load image: {image_path}')  # 경로 출력
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 흑백으로 로드
    img = cv2.resize(img, (90, 90))  # 크기를 90x90으로 조정
    img = img.astype(np.float32) / 255.0  # 정규화
    return img

def encrypt_image(image, cs):
    """이미지를 암호화합니다."""
    encrypted_image = []
    for row in image:
        encrypted_row = [cs.encrypt_pixel(int(pixel * 255)) for pixel in row]  # 0-1 범위 값을 0-255로 변환 후 암호화
        encrypted_image.append(encrypted_row)
    return np.array(encrypted_image)

def decrypt_image(encrypted_image, cs):
    """암호화된 이미지를 복호화합니다."""
    decrypted_image = []
    for row in encrypted_image:
        decrypted_row = [cs.decrypt_pixel(pixel) / 255.0 for pixel in row]  # 복호화 후 0-1 범위로 다시 변환
        decrypted_image.append(decrypted_row)
    return np.array(decrypted_image)


def calculate_similarity(img1, img2):
    """두 이미지 간의 유사도를 계산합니다."""
    # SSIM 사용하여 유사도 계산
    return ssim(img1, img2, data_range=1.0)

def find_best_match(input_image_path, dataset_path):
    """입력된 이미지와 데이터셋의 이미지 간의 유사도를 계산하여 가장 높은 유사도를 가진 이미지를 찾습니다."""
    input_image = preprocess_image(input_image_path)
    encrypted_input_image = encrypt_image(input_image, cs)  # 입력 이미지 암호화

    best_match = None
    best_similarity = -1  # 초기 유사도는 -1로 설정 (유사도는 0~1 범위)

    for filename in os.listdir(dataset_path):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.BMP'):  # 이미지 파일 형식
            dataset_image_path = os.path.join(dataset_path, filename)
            dataset_image = preprocess_image(dataset_image_path)
            encrypted_dataset_image = encrypt_image(dataset_image, cs)  # 데이터셋 이미지 암호화
            decrypted_dataset_image = decrypt_image(encrypted_dataset_image, cs) # 복호화된 이미지를 유사도 계산에 사용(이 부분 오류)

            similarity = calculate_similarity(input_image, dataset_image)
            print(f'Comparing with {filename}: Similarity = {similarity:.4f}')
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = filename

    return best_match, best_similarity

# 사용 예시
input_image_path = 'D:'  # 입력 지문 이미지 경로
dataset_path = 'D:'  # 지문 데이터셋 경로

try:
    best_match, best_similarity = find_best_match(input_image_path, dataset_path)
    print(f'Best match: {best_match} with similarity: {best_similarity:.4f}')

except ValueError as e:
    print(e)


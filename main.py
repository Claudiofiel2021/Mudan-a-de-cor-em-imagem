
import cv2

# Carregar imagem
img = cv2.imread('lena.jpg')

# Converter para níveis de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


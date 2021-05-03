import cv2

#Carregar algum dado pre-treinado sobre rostos frontais do opencv ( haar cascade algoritmo )
rostosTreinados = cv2.CascadeClassifier('../opencv/haarcascade_frontalface_default.xml')

#Escolher uma imagem para ser usada como fonte
img = cv2.imread('../Image/Eu.jpg')

cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()
from cv2 import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import math
import csv

# print(img)  #ver a matriz

diretorio = 'banco_imagens'

arquivos = os.listdir(diretorio)

template_l = cv2.imread('nariz_0099_dir.jpg', 0)
template_r = cv2.imread('nariz_0099_esq.jpg', 0)

w, h = template_l.shape[::-1]

w2, h2 = template_r.shape[::-1]

dif_v = 200
dif_h = 800

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

resultados = {}

for a in arquivos:
    ct = 0
    if a.lower().endswith('.jpg') or a.lower().endswith('.png') or a.lower().endswith('.jpeg'):
        imgC = diretorio+'/'+a
        print(imgC)

        #img = cv2.imread(a,0)
        img = cv2.imread(imgC, 0)

        altura = img.shape[0]  # altura da imagem - eixo y - vertical
        largura = img.shape[1]  # largura da imagem - eixo x - horizontal

        img2 = img.copy()
        
        #print(imgC)

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching esquerda
        res_l = cv2.matchTemplate(img, template_l, method)
        min_val_l, max_val_l, min_loc_l, max_loc_l = cv2.minMaxLoc(res_l)

        # Apply template Matching direita
        res_r = cv2.matchTemplate(img, template_r, method)
        min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(res_r)

        # max_val apresenta maximo valor de similaridade, min_val o minimo valor...

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left_l = min_loc_l
            top_left_r = min_loc_r
        else:
            top_left_l = max_loc_l
            top_left_r = max_loc_r

        bottom_right_l = (top_left_l[0] + w, top_left_l[1] + h)
        bottom_right_r = (top_left_r[0] + w2, top_left_r[1] + h2)

       # print(bottom_right, bottom_right2)

        dist_left_meio = math.fabs((largura/2) - bottom_right_l[0])
        dist_rigth_meio = math.fabs(top_left_r[0] - (largura/2))

        #print(bottom_right_l[0], largura/2, dist_left_meio)
        #print(bottom_right_r[0], largura/2, dist_rigth_meio)

        # print(top_left_l, bottom_right_l, top_left_r, bottom_right_r, meth)  # Ana

        # print(top_left[1], top_left2[1]) #coordenada y do retangulo

        modulo_dif_y = math.fabs(top_left_l[1] - top_left_r[1])

        if modulo_dif_y <= dif_v and top_left_l[1] >= altura/2 and top_left_r[1] >= altura/2 and dist_left_meio <= dif_h and dist_rigth_meio <= dif_h:
            ct += 1

            #vermelho = (0, 0, 255)
            # print(ct)

            cv2.rectangle(img, top_left_l, bottom_right_l, 255, 2)
            cv2.rectangle(img, top_left_r, bottom_right_r, 255, 2)

            plt.subplot(121), plt.imshow(res_l, cmap='gray')
            # plt.subplot(121),plt.imshow(res)
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(img, cmap='gray')
            # plt.subplot(122),plt.imshow(img)
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth + ' figura: ' + a)

            plt.show()
    #print(imgC, ct)
    resultados[a] = ct
print(resultados)
# plt.show()

with open('resultados.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(["arquivo", "qtde indicacoes"])
    for f in resultados:
        print(f, resultados[f])
        writer.writerow([f, resultados[f]])

print('Finalizado')
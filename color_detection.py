#Caso tenha qualquer problema com as bibliotecas,
#utilize o comando py -m pip install nome_biblioteca no CMD

import cv2
import numpy as np
import pandas as pd

img_path = 'cores.jpg'
img = cv2.imread(img_path)
img=cv2.resize(img,(700,500))

clicked = False
r = g = b = xpos = ypos = 0

#Lendo o arquivo csv com as cores
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#função para calcular a distância mínima de todas as cores e obter a cor que mais combina
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

#função para obter as coordenadas x, y do clique duplo do mouse
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
cv2.namedWindow('color detection')
cv2.setMouseCallback('color detection',draw_function)

while(1):

    cv2.imshow("color detection",img)
    if (clicked):
   
        #cv2.rectangle(imagem, ponto inicial, ponto final, cor, espessura) -1 preenche todo o retângulo 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Criação de string de texto para exibição (nome da cor e valores RGB)
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()
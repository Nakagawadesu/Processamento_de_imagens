
import os
import cv2
import numpy as np


def negative_effect(input_dir, P1, P2):


            color_image = cv2.imread(input_dir)

            if color_image is not None:
            
                X_limit = x_limit(P1,P2)
                Y_limit = y_limit(P1,P2)
                x = X_limit[0]  
                y = Y_limit[0]  
                width =   X_limit[1] - X_limit[0] 
                height =  Y_limit[1] - Y_limit[0]  


                region = color_image[y:y+height, x:x+width]


                negative_region = 255 - region

                color_image[y:y+height, x:x+width] = negative_region

                cv2.imshow('Modified Image', color_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

def x_limit(P1 , P2):
    x_limit=[]
    if(P1[0] > P2[0]):
        x_limit = [P2[0],P1[0]]
    else:
        x_limit = [P1[0],P2[0]]
    return x_limit
def y_limit(P1,P2):
    y_limit=[]
    if(P1[1] > P2[1]):
        y_limit = [P2[1],P1[1]]
    else:
        y_limit = [P1[1],P2[1]]
    return y_limit
input_directory = "/home/matheus/Desktop/Proessamento de imagens/images/lena.png"
negative_effect(input_directory ,  [0,0] , [100,100])
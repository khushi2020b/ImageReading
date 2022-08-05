import cv2 as cv
import pandas as pd
import sys

index = ["Color_Name", "Color", "Hex", "R", "G", "B"]
colors = pd.read_csv("colors.csv", names = index, header = None)
#len(colors)
colors.head()
image = cv.imread("colorpic.jpg")

def getColorName(R, G, B):
    minimum = 10000
    for x in range(0, len(colors)):
        d = abs(R - int(colors.loc[x, 'R'])) + abs(G - int(colors.loc[x,'G'])) + abs(B - int(colors.loc[x, 'B']))
        if d <= minimum :
            minimum = d
            color_name = colors.loc[x, "Color"]
    return color_name

#getColorName(114, 160, 193)

R = G = B = xpos = ypos = 0
click = False
def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global R, G, B, xpos, ypos, click
        click = True
        xpos = x
        ypos = y
        B, G, R = image[y, x]
        B = int(B)
        G = int(G)
        R = int(R)
        print("draw function")

cv.namedWindow("imageRBG")
cv.setMouseCallback("imageRBG", draw)

while True:
    cv.imshow("imageRBG", image)
    if click == True:
        if R + G + B >= 500:
            cv.rectangle(image, (20,20), (300, 75), (250, 250, 250), -1)
        else:
            cv.rectangle(image, (20,20), (300, 75), (0, 0, 0), -1)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(image,getColorName(R, G, B),(50,50), font, 1,(B, G, R),2,cv.LINE_AA)
        print(getColorName(R, G, B))
        print(R, G, B)
        click = False
    if cv.waitKey(20) & 0xFF == 27 :
        break

cv.destroyAllWindows()
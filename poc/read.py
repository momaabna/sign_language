import cv2
from time import sleep

import os

file_path = 'poc/readfile.txt'
time = 0.3
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 300, 300)
replace_dict = {'أ':'ا', 'إ':'ا', 'آ':'ا', 'ؤ':'و', 'ئ':'ي', 'ى':'ي', ' ':'-','\n':'--','\t':'--','،':'-'}

with open(file_path, 'r') as f:
    text = f.read()
    text = text.replace(' ', '-')
    for key in replace_dict:
        text = text.replace(key, replace_dict[key])
    text ='-'+text+'-'
    for i in range(len(text)):
        print(text[i])
        if os.path.exists('poc/Chars/{}.jpg'.format(text[i])):
            img = cv2.imread('poc/Chars/{}.jpg'.format(text[i]))
            cv2.imshow('image', img)
        else:
            img = cv2.imread('poc/Chars/{}.jpg'.format('-'))
            cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        sleep(time)
cv2.destroyAllWindows()


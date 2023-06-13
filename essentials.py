import cv2 as cv

img=cv.imread('Videos/tree.jpg')
cv.imshow('Image', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny=cv.Canny(img,125,175) 
cv.imshow('Canny', canny)

dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated', dilated)

erode=cv.erode(dilated,(7,7),iterations=3 )
cv.imshow('eroded', erode)

resized=cv.resize(img,(300,300),interpolation=cv.INTER_LINEAR)
cv.imshow('resized', resized)

crop=img[50:200,200:400]
cv.imshow('crop', crop)


cv.waitKey(0)
cv.destroyAllWindows()
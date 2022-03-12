import cv2
img1=cv2.imread('1-500x250-3.jpg')
img2=cv2.imread('2-500x250-2.jpg')
newImg=cv2.addWeighted(img1,0.8,img2,0.2,0)
cv2.imwrite('newimg.jpg',newImg)
# cv2.destroyAllWindows()
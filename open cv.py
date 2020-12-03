import cv2,time
#load image
'''img=cv2.imread("C:/Users/ELCOT/Desktop/RAJESH/Photo.jpg",0)
img1=cv2.imread("C:/Users/ELCOT/Desktop/RAJESH/Photo.jpg",1)
print(type(img1))
print(img)
print(img.shape)
cv2.imshow("Rajesh picture",img1)
cv2.waitKey(2000)
cv2.destroyAllWindows()'''

#Resize
'''img=cv2.imread("C:/Users/ELCOT/Desktop/RAJESH/Photo.jpg",0)
resized_img=cv2.resize(img,(350,400))
cv2.imshow("resized image of rajesh",resized_img)
cv2.waitKey(4000)
cv2.destroyAllWindows()'''

#face detection using cascade classifier
'''img=cv2.imread("C:/Users/ELCOT/Desktop/RAJESH/Photo.jpg",0)
cascade=cv2.CascadeClassifier("C:/Users/ELCOT/Desktop/RAJESH/Photo.jpg")
convert_into_grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=cascade.detectMultiScale(convert_into_grayscale,scaleFactor=1.05,minNeighbors=5)
print(faces)
#print(type(faces))'''

#video capture
'''video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    convert_to_grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",convert_to_grayscale)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()'''

#color conversion
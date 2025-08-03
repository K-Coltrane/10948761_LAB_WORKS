import cv2

#Loading image
image = cv2.imread('photo.jpeg')
if image is None:
    print("Error: Image not found.")
    exit

#Converting image to grayscale
gray_image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Displaying both the original and grayscale images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)

#Save the grayscale images
cv2.imwrite('photo_gray.jpeg', gray_image)
print("Grayscale image saved as 'photo_gray.jpeg'.")

cv2.waitKey(0)
cv2.destroyAllWindows()
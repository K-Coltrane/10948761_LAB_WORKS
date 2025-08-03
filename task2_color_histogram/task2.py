import cv2
import matplotlib.pyplot as plt

# Loading image
image = cv2.imread("photo.jpeg")
if image is None:
    print(("Error image not found"))
    exit()

# Converting image to grayscale
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.imwrite("photo_gray.jpg", gray)
print("Grayscale image saved as 'photo_gray.jpg'.")

#Convert to HSV
hsv =cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv)
cv2.imwrite("photo_hsv.jpg", hsv)
print("HSV image saved as 'photo_hsv.jpg'.")

#Converting image to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB Image", lab)        
cv2.imwrite("photo_lab.jpg", lab)
print("LAB image saved as 'photo_lab.jpg'.")

# Plotting Histogram
plt.figure(figsize=(6, 4))
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.hist(gray.ravel(), bins=256, range=[0, 256], color='gray')
plt.grid(True)
plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
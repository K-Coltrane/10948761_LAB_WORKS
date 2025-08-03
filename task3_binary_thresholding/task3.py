pixel_value = 180
threshold = 150

new_value = 255 if pixel_value >= threshold else 0

print(f"Original pixel value: {pixel_value}")
print(f"Threshold value: {threshold}")
print(f"New pixel value after binary thresholding: {new_value}")

#The answer is 255

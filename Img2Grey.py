import cv2

# Read an image
image = cv2.imread('gigachad.jpeg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('gray_chad.jpg', gray_image)

# Display the image
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Giga Chad Colored', image)
cv2.waitKey(0)
#cv2.destroyAllWindows()

from PIL import Image, ImageFilter
import cv2

# Opening the image
image = Image.open('gigachad.jpeg')

# Resize the image
resized_img = image.resize((200, 200))

# Apply a filter
blurred_img = image.filter(ImageFilter.BLUR)

# Saving the images
resized_img.save('minigigachad.jpg')
blurred_img.save('blurredgigachad.jpg') 

# Showing the images
cv2.imshow('Mini Giga Chad', resized_img)
cv2.imshow('Blurred Giga Chad.jpg', blurred_img)
cv2.waitKey(0)
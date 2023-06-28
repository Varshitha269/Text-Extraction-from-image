import cv2
import pytesseract
from google.colab.patches import cv2_imshow
from google.colab import files
image_files=files.upload()
for imageFilename in image_files:
  image = cv2.imread(imageFilename)
  text=pytesseract.image_to_string(image)
  print(text)
  cv2_imshow(image)

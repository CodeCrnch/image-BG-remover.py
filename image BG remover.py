from rembg import remove
from PIL import Image

image_input = "pic_with_BG.jpeg"
image_output = "pic_without_BG.png"

input = Image.open(image_input)
output = remove(input)
output.save(image_output)
print("BG removed!")

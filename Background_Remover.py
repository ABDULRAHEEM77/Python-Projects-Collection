from rembg import remove
from PIL import Image

input_path = "sgame.png"
output_path = "sgame_no_bg.png"

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)

print("Background removed successfully!")

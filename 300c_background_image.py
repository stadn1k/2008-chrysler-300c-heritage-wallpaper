from PIL import Image, ImageOps, ImageDraw, ImageFont


#filename = '300c.jpg'

img = Image.new('RGB', (300, 200), (160, 180, 210))
img.save(f"300c_r160_g180_b210.jpg")


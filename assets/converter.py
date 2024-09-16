from PIL import Image

# Открыть WebP файл
webp_image = Image.open("img/Rainfall.webp")

# Сохранить как PNG
webp_image.save("img/Rainfall.png", "PNG")

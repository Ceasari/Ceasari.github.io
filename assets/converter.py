from PIL import Image

# Открыть WebP файл
webp_image = Image.open("img/PLC.webp")

# Сохранить как PNG
webp_image.save("img/PLC.png", "PNG")

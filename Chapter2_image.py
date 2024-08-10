from PIL import Image
from PIL import ImageFilter

# Memuat gambar
image = Image.open('/workspaces/multimedia-python/telur_balado (26).jpg')

# Menyimpan gambar
image.save('result_Crop.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('/workspaces/multimedia-python/telur_balado (26).jpg')

resized_image = cropped_image.resize((200, 200))
resized_image.save('/workspaces/multimedia-python/telur_balado (26).jpg')


filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('/workspaces/multimedia-python/telur_balado (26).jpg')
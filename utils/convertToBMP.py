from PIL import Image 

for i in range (1,6506):
    fnm = 'frame{:05d}'.format(i)
    im_1 = Image.open(fnm+".png")
    new_image = im_1.resize((160, 128))
    new_image.save(fnm+'.bmp', 'BMP')
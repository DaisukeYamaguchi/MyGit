import os
from PIL import Image, ImageFilter

files = os.listdir('./training/5')

for i in range(len(files)):
  img = Image.open('./training/5/' + files[i])
  img = img.filter(ImageFilter.GaussianBlur(1.5))
  img.save('./training/5_amb/' + files[i])



with open('small_mnist_5_training.csv', 'w', encoding = 'sjis') as f:
  waste = f.write('x:image,y:image')
  waste = f.write('\n')
  for i in range(1500):
    waste = f.write('./training/5_amb/' + files[i] + ',./training/5/' + files[i])
    waste = f.write('\n')

with open('small_mnist_5_test.csv', 'w', encoding = 'sjis') as f:
  waste = f.write('x:image,y:image')
  waste = f.write('\n')
  for i in range(1500, 2000):
    waste = f.write('./training/5_amb/' + files[i] + ',./training/5/' + files[i])
    waste = f.write('\n')


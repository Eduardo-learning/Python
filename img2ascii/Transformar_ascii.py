from PIL import Image

im = Image.open("index.jpeg")

test = open('test.txt', 'r+')

#print(im.size[0])
im = im.resize((int(im.size[0]/6),int(im.size[1]/6)))
im = im.convert('L')
im = im.rotate(90)
print('lala', im.size)

#for i in range(im.size[1]):
#    print(i)

print(im.size[0])
print(im.size[1])
#print([i for i in range(im.size[0])])


for i in range(im.size[0]):
    print('line: ', i)
    for j in range(im.size[1]):
        #print(im.getpixel((i,j)))
        print('letter: ', i)
        if 0 <= im.getpixel((i,j)) <= 50:
            pixel = '@'
            test.write(pixel)
        if 51 <= im.getpixel((i,j)) <= 100:
            pixel = '#'
            test.write(pixel)
        if 101 <= im.getpixel((i,j)) <= 150:
            pixel = '+'
            test.write(pixel)
        if 151 <= im.getpixel((i,j)) <= 200:
            pixel = '-'
            test.write(pixel)
        if 201 <= im.getpixel((i,j)) <= 255:
            pixel = '.'
            test.write(pixel)
    test.write('\n')

test.close()


#x = 5
#box = (im.size[0]/x, im.size[0]/x, im.size[1]/x, im.size[1]/x)
#box = (330, 330, 400, 400)
#region = im.crop(box)

#im = im.rotate(45)

        

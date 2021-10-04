from PIL import Image
import cv2
import time

def convert(img, size=(50,50)):
    chars = ' .,:;+*%#@'
    # chars = chars[::-1]
    scale = {c:i for c,i in zip(chars, range(0,len(chars) * 10,10))}
    img = Image.fromarray(img)
    img.thumbnail(size)
    data = [[] for _ in range(img.height)]
    for x in range(img.width):
        for y in range(img.height):
            avg = img.getpixel((x,y))[0]
            avg /= 2.55
            for i in range(0,len(chars) * 10,10):
                if avg < i:
                    i -= 1
                    break
            i //= 10
            char = chars[i]
            data[y].append(char)
    value = ''
    for line in data:
        value += ' '.join(line)
        value += '\n'
    return value


def extract_frames(video):
    vid = cv2.VideoCapture(video)
    success, img = vid.read()
    data = [img]
    while success:
        data.append(img)
        success, img = vid.read()
    return data


frames = extract_frames('badapple.mp4')

print("NOTE TO SELF: START MUSIC HERE")
time.sleep(1)

last = time.time_ns()
for frame in frames:
    while time.time_ns() < last + 33333333.33333333:
        pass
    last = time.time_ns()
    print('\x1b[2J', end='')
    img = convert(frame, (90,90))
    print(img)

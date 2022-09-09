import os
import shutil

import cv2
import matplotlib.pyplot as plt


output_dir = './output'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.mkdir(output_dir)

input_imgs = os.path.join('./input_data', 'imgs')

tracking_file = '/home/phillip/Documents/youtube/computer_vision/object_tracking_sort/code/sort/output/example.txt'

with open(tracking_file, 'r') as f:
    lines = [l[:-1] for l in f.readlines() if len(l) > 2]
    f.close()

frame_nmr_ = -1
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255),
          (0, 0, 0)]
for line in lines:
    # 1, 1, 347.60, 287.94, 26.38, 18.69, 1, -1, -1, -1
    frame_nmr, instance_nmr, x, y, w, h, _, _, _, _ = [float(e) for e in line.split(',')]

    if int(frame_nmr) == frame_nmr_:
        pass
    else:
        if frame_nmr_ != -1:
            cv2.imwrite(os.path.join(output_dir, '{}.jpg'.format(str(int(frame_nmr - 1)).zfill(6))), img)
        img = cv2.imread(os.path.join(input_imgs, '{}.jpg'.format(str(int(frame_nmr - 1)).zfill(6))))
        frame_nmr_ = int(frame_nmr)

    img = cv2.rectangle(img, (int(x), int(y)), (int(x + w), int(y + h)), colors[int(instance_nmr) % len(colors)], 2)

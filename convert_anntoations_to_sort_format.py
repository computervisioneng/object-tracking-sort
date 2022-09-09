import os
import shutil

import cv2


input_anns = os.path.join('./input_lane_crossing', 'anns')
input_imgs = os.path.join('./input_lane_crossing', 'imgs')

image = None

dir_name = 'example'
example_dir = './' + dir_name
det_dir = os.path.join(example_dir, 'det')
for dir_ in [example_dir, det_dir]:
    if os.path.exists(dir_):
        shutil.rmtree(dir_)
    os.mkdir(dir_)

output_file = os.path.join(det_dir, 'det.txt')

with open(output_file, 'w') as fw:
    # 2,-1,463.468,431.511,62.509,178.632,0.988998,-1,-1,-1
    for file in sorted(os.listdir(input_anns)):
        if image is None:
            image = cv2.imread(os.path.join(input_imgs, file[:-4] + '.jpg'))
            H, W, _ = image.shape
        frame_nmr = int(file[:-4])
        with open(os.path.join(input_anns, file), 'r') as f:
            lines = [l[:-1] for l in f.readlines() if len(l) > 2]
            f.close()

        for line in lines:
            class_nmr, xc, yc, w, h, conf = [float(e) for e in line.split(' ')]
            x = xc - (w / 2)
            y = yc - (h / 2)
            fw.write('{},-1,{},{},{},{},{},-1,-1,-1\n'.format(int(frame_nmr + 1), x * W, y * H, w * W, h * H, conf))

    fw.close()

if os.path.exists('sort/data/train/' + dir_name):
    shutil.rmtree('sort/data/train/' + dir_name)
shutil.move(example_dir, 'sort/data/train')

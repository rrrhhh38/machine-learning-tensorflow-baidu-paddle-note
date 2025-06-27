import os
from sklearn.model_selection import train_test_split

files = [f[:-4] for f in os.listdir('D:/labelimg_dataset/images') if f.endswith('.jpg')]
train, val = train_test_split(files, test_size=0.2, random_state=42)

with open('D:/labelimg_dataset/train.txt', 'w') as f:
    f.write('\n'.join([f"images/{name}.jpg labels/{name}.txt" for name in train]))

with open('D:/labelimg_dataset/val.txt', 'w') as f:
    f.write('\n'.join([f"images/{name}.jpg labels/{name}.txt" for name in val]))

# 生成类别文件
with open('D:/labelimg_dataset/label_list.txt', 'w') as f:
    f.write('woman\ndog\ncar\ntruck\nman')
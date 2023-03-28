import os
import shutil
import random


def split_data(train_dir, val_dir, val_ratio=0.2):
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    # 获取所有图片文件
    img_files = [f for f in os.listdir(train_dir) if f.endswith('.png')]
    random.shuffle(img_files)

    # 计算验证集的大小
    val_size = int(len(img_files) * val_ratio)

    # 移动随机选择的图片及其对应的标签文件到验证集文件夹
    for i in range(val_size):
        img_name = img_files[i]
        label_name = os.path.splitext(img_name)[0] + '.txt'
        shutil.move(os.path.join(train_dir, img_name), os.path.join(val_dir, img_name))
        shutil.move(os.path.join(train_dir, label_name), os.path.join(val_dir, label_name))


if __name__ == "__main__":
    train_dir = "train_with_rotate"
    val_dir = "val_with_rotate"
    val_ratio = 0.2
    split_data(train_dir, val_dir, val_ratio)

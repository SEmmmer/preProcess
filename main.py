import cv2
import numpy as np
import os


def split_image(addr: str):
    pic_path = addr  # 分割的图片的位置
    origin_file_name = addr.split("/")[-1].split(".")[0]
    pic_target = './result/'  # 分割后的图片保存的文件夹
    if not os.path.exists(pic_target):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(pic_target)
    # 要分割后的尺寸
    cut_width = 512
    cut_length = 640
    # 读取要分割的图片，以及其尺寸等数据
    picture = cv2.imread(pic_path)
    (width, length, depth) = picture.shape
    # 预处理生成0矩阵
    pic = np.zeros((cut_width, cut_length, depth))
    # 计算可以划分的横纵的个数
    num_width = int(width / cut_width)
    num_length = int(length / cut_length)
    # for循环迭代生成
    for i in range(0, num_width):
        for j in range(0, num_length):
            pic = picture[i * cut_width: (i + 1) * cut_width, j * cut_length: (j + 1) * cut_length, :]
            result_path = pic_target + '{}_{}_{}.png'.format(origin_file_name, i + 1, j + 1)
            cv2.imwrite(result_path, pic)

    print(pic_path + " done!!!")


if __name__ == '__main__':
    for num in range(278, 291):
        split_image("./pngs/" + str(num) + ".png")

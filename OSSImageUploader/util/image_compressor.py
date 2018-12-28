# -*- coding: utf-8 -*-

from PIL import Image


def compress_image(file, max_width = 0, quality = 75):
    '''
    压缩图片（直接操作图片）
    :param file: 文件名（路径）
    :param max_width: 最大宽度
    :param quality: 图片质量
    '''
    path = file
    img = Image.open(path)
    w, h = img.size
    print(w, h)
    target_w = w
    target_h = h
    if w > max_width:
        target_w = int(max_width)
        target_h = int(h / w * max_width)
    # 压缩并保存
    img.resize((target_w, target_h)).save(path, quality=quality)

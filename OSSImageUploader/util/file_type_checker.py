# -*- coding: utf-8 -*-

import struct


def type_list():
    '''
    支持的文件类型：这里只支持了三种图片格式
    :return: 文件格式对象（key为十六进制字节）
    '''
    return {
        'FFD8FF': 'JPEG',
        '89504E47': 'PNG',
        '47494638': 'GIF'
    }


def bytes2hex(bytes):
    '''
    字节转换为十六进制串
    :param bytes: 整数字符串组成的元祖，表示多个字节 
    :return: utf-8编码的16进制字符串（大写）
    '''
    num = len(bytes)
    hex_str = u''
    # 遍历每个字节串
    for i in range(num):
        # 转成utf-8字符串（直接变成了十六进制）
        t = u'%x' % bytes[i]
        if len(t) % 2:
            # 先加"0"
            hex_str += u'0'
        hex_str += t
    # 返回大写版本
    return hex_str.upper()


def file_type(file_path):
    '''
    获取文件类型
    :param file_path: 文件名（路径）
    :return: 文件类型字符串
    '''
    # 使用二进制方式读取文件
    byte_file = open(file_path, 'rb')
    # 支持的文件类型
    designed_type = type_list()
    # 目标文件类型
    target_type = 'unknown'

    # 依次使用类型的字节串匹配文件的头n个字节
    for hcode in designed_type.keys():
        # 字节串长度（十六进制除以2是字节数）
        num_of_bytes = int(len(hcode) / 2)
        byte_file.seek(0) # 从文件开头开始读取
        # 读取num_of_bytes个字节数据（十六进制）
        buffer = byte_file.read(num_of_bytes)
        # 从中解包出对应字节的数据（转换成整数字符串组成的元祖）
        hbytes = struct.unpack_from("B"*num_of_bytes, buffer)
        # 转换为十六进制
        f_hcode = bytes2hex(hbytes)
        # 比较
        if f_hcode == hcode:
            # 相同，返回对应的value（类型）
            target_type = designed_type[hcode]
            break
    # 关闭文件
    byte_file.close()

    return target_type

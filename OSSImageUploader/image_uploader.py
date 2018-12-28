# -*- coding: utf-8 -*-

import oss2
import os
import time
from util.file_type_checker import file_type, type_list
from util.image_compressor import compress_image


class ImageUploader(object):

    def __init__(self, server, bucket, accesskey, secret):
        # 配置
        auth = oss2.Auth(accesskey, secret)
        self.__bucket = oss2.Bucket(auth, server, bucket)

    @staticmethod
    def _is_image_type(file):
        '''
        查看是否为图片类型
        :param file: 文件路径
        :return: 判断结果
        '''
        target_type = file_type(file)
        enabled_types = type_list().values()
        return target_type in enabled_types

    def upload_image_to_oss(
            self,
            file,
            compress=False,
            max_width=0,
            quality=75
    ):
        '''
        上传图片到OSS中
        :param file: 文件路径
        :param compress: 是否需要压缩
        :param max_width: 图片最大宽度
        :return: 访问地址
        '''

        # 1.查看是否为图片
        if not self._is_image_type(file) :
            print('错误：只支持图片文件...')
            return

        # 2.检查并压缩图片
        if compress:
            compress_image(file, max_width, quality)

        # 3,开始上传

        # 获取文件名
        file_name = os.path.basename(file)
        # 时间戳
        now = int(time.time())
        # 文件名
        key = str(now) + '-' + file_name
        print(key)

        result_url = ''

        try:
            # 上传
            result = self.__bucket.put_object_from_file(key, file)
            if result.status == 200:
                # 成功，获取response
                response = result.resp.response
                result_url = response.url
                print(result_url)
        except oss2.exceptions.NoSuchKey as e:
            print('错误：{0} 未找到：http_status = {1}, request_id = {2}'.format(key, e.status, e.request_id))
        except oss2.exceptions.Conflict as e:
            print('错误：{0} 上传冲突：http_status = {1}, message = {2}'.format(key, e.status, e.message))
        finally:
            return result_url

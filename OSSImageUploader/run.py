# -*- coding: utf-8 -*-

from settings import *
from image_uploader import ImageUploader

if __name__ == '__main__':
    print('start...')
    uploader = ImageUploader(
        OSS_SERVER,
        OSS_BUCKET_NAME,
        OSS_ACCESS_KEY,
        OSS_SECRET
    )
    url = uploader.upload_image_to_oss('./img/1.jpg')
    print('url = ', url)
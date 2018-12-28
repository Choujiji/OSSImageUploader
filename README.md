# OSSImageUploader
简单的上传图片到阿里云OSS的图床功能

> 开发环境 pycharm,
> python版本：3.6.3
> 依赖：PIL、OSS2（阿里云OSS SDK）

只支持最基本功能：
- 支持jpg、png图片上传，
- 支持图片压缩并设置压缩质量
- 支持设置图片最大宽度（压缩情况下）
- 运行一次一张图片。。。

**使用前，需要在settings.py文件中，设置服务器名、accessKey、secret和bucket名。**
#### OSS服务器
OSS_SERVER = 'http://oss-xxx.aliyuncs.com'

#### Bucket名
OSS_BUCKET_NAME = 'my-bucket'

#### AccessKey
OSS_ACCESS_KEY = 'Snej97enkLLM'

#### Secret
OSS_SECRET = 'SUNN00xhsdkl23UYIE'

**在run.py中设置需要上传的图片路径。。。**
url = uploader.upload_image_to_oss('./img/1.jpg')


由于是python菜鸟，只是为了方便博客中上传图片而编写（这样就不用给iPic交钱了，😝）。
> 未来需要实现的功能：
> 1. 编写GUI，图形化操作（选择图片、设置功能）
> 2. 打包成可执行文件

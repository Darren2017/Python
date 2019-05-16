#-*-coding:utf-8-*-
from qiniu import Auth, put_file, etag
import qiniu.config
from qiniu import BucketManager


access_key = 'YCdnGHp2tRa7V0KDisHqXehlny0eVNM5vQow1cQV'
secret_key = 'ZGgkaNPunh6Y32FcsAtvhOd61rnlcKeeXPZ-qIlr'
url = 'pchz6zd8k.bkt.clouddn.com'
bucket_name = 'tets'
q = qiniu.Auth(access_key, secret_key)
bucket = BucketManager(q)

# def qiniu_upload(key, localfile):
#     token = q.upload_token(bucket_name, key, 3600)

#     ret, info = qiniu.put_file(token, key, localfile)

#     if ret:
#         return '{0}{1}'.format(url, ret['key'])
#     else:
#         raise UploadError('上传失败，请重试')


key = '/24634763457456.jpg'
# localfile = '/Users/darren/Downloads/摄影原图/test.md'

# res = qiniu_upload(key, localfile)
# print(res)

ret, info = bucket.delete(bucket_name, key)
print(info)
assert ret == {}
#-*-coding:utf-8-*-
from qiniu import Auth, put_file, etag
import qiniu.config
from qiniu import BucketManager
import os
import requests
import time
import json


access_key = 'YCdnGHp2tRa7V0KDisHqXehlny0eVNM5vQow1cQV'
secret_key = 'ZGgkaNPunh6Y32FcsAtvhOd61rnlcKeeXPZ-qIlr'
url = 'pdygcd0fr.bkt.clouddn.com'
bucket_name = 'box-map'
q = qiniu.Auth(access_key, secret_key)

def qiniu_upload(key, localfile):
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = qiniu.put_file(token, key, localfile)

    if ret:
        return '{0}{1}'.format(url, ret['key'])
    else:
        raise UploadError('上传失败，请重试')


# key = '/24634763457456.jpg'
# localfile = '/Users/darren/Downloads/摄影原图/test.md'

# res = qiniu_upload(key, localfile)
# print(res)

tt = 'https://ccnubox.muxixyz.com/api/plat/'


Pos = '/Users/darren/Downloads/西区照片'
# for(dirpath, dirnames, files)in os.walk(Pos):
#     for filename in files:
#         localfile = os.path.join(dirpath, filename)
#         key = time.time()
#         res = qiniu_upload(key, localfile)
#         i = res.find('com')
#         res = res[:i+3] + '/' + res[i+3:]
#         list = []
#         list.append(res)
#         print (list)
#         print(filename.split('.')[0])
#         data = json.dumps({'name': filename.split('.')[0],
#                 'url': list
#         })
#         response = requests.post(tt, data = data)
#         print(response.status_code)

# localfile = '/Users/darren/Downloads/西区照片/中国工商银行（满江红）.jpg'
# key = time.time()
# res = qiniu_upload(key, localfile)
# i = res.find('com')
# res = res[:i+3] + '/' + res[i+3:]
# list = []
# list.append(res)
# print (list)
# data = json.dumps({
#     "name": '西区照片/中国工商银行（满江红)',
#     "url": list
# })
# response = requests.post(tt, data = data)
# print(response.status_code)
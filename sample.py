# -*- coding: utf-8 -*-
# tencent youtu request output format:
# {
# 	"errorcode":0,
# 	"errormsg":"OK",
# 	"items":
#         [
#             {
#                "itemcoord":{"x":10,"y":4,"width":316,"height":61},
#                "itemstring":"至致全国体育迷:",
#                "coords"[],
#                "words"[
#                     {"character":"至","confidence":0.9771012663841248},
#                     ....
#                     {"character":":","confidence":0.7994066476821899}
#                  ],
#                "candword":[]
#             },
#             {
#                "itemcoord":{"x":7,"y":74,"width":423,"height":69},
#                "itemstring":"让我們共为奥运加油",
#                "coords":[],
#                "words":[
#                     {"character":"让","confidence":0.9785435795783997},
#                     .....
#                     {"character":"油","confidence":0.6906964778900147}
#                    ],
#                "candword":[]
#             }
#                 ],
# 	"session_id":"",
# 	"angle":0.0
# }

import time
import TencentYoutuyun
import json
# pip install requests
# please get these values from http://open.youtu.qq.com
appid = '10117921'
secret_id = 'AKIDdHpDPOTjdKp8NRTIwNhEbmlqnY7V4CXg'
secret_key = '60iNsFQPUt9C3iAjM4qTuAMOOWZQ5cP5'
userid = ''

#choose a end_point
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT 
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = ''


#for TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT end_point
#get four-character idioms
#retlivegetfour = youtu.livegetfour(session_id)
#print retlivegetfour

#four-character live detect without face compare
#retlivedetectfour = youtu.livedetectfour('1122', 'xxx.mp4', session_id)
#print retlivedetectfour

#four-character live detect with face compare
#retlivedetectfour= youtu.livedetectfour('1122',  'xxx.mp4',  session_id,   'xxx.jpg', True)
#print retlivedetectfour

#four-character idcard live detect
#retidcardlivedetectfour = youtu.idcardlivedetectfour('123456789987654321',  '张三',  '1122', 'xxx.mp4', session_id )
#print retidcardlivedetectfour

#idcard face compare: use local image compare with id card image 
#retidcardfacecompare = youtu.idcardfacecompare('123456789987654321', '张三', 'xxx.jpg', 0, session_id)
#print retidcardfacecompare

#idcard face compare :use url image compare with id card image
#retidcardfacecompare = youtu.idcardfacecompare('123456789987654321', '张三', 'http://xxx.png', 1, session_id)
#print retidcardfacecompare

# face compare : use two local image to compare 
#retfacecompare = youtu.FaceCompare('xxx.jpg', 'xxx.jpg')
#print retfacecompare

# face compare : use two url image to compare 
#retfacecompare = youtu.FaceCompare('http://xxx.png', 'http://xxx.png', 1)
#print retfacecompare

#id card ocr: use local id card image
#retidcardocr = youtu.idcardocr('xxx.jpg', data_type = 0, card_type = 0)
#print retidcardocr

#id card ocr: use url id card image
#retidcardocr = youtu.idcardocr('http://xxx.jpg', data_type = 1, card_type = 0)
#print retidcardocr

#driver license ocr: use local image
#retdriverlicenseocr = youtu.driverlicenseocr('ocr_xsz_01.jpg', data_type = 0, proc_type = 0)
#print retdriverlicenseocr

#business card ocr: use local image
#retbcocr = youtu.bcocr('ocr_card_01.jpg', data_type = 0)
#print retbcocr

#general ocr: use local image
num = 1
imgname = str(num) + '.jpg'
# imgname = 'timg.jpg'
# retgeneralocr = youtu.generalocr(imgname, data_type = 0)
result = youtu.generalocr(imgname, data_type = 0)
print (type(result), result)

for line in result["items"]:
    print (line["itemstring"])


#
# while True:
# 	# if num <= 4:
# 		imgname = str(num) + '.jpg'
# 		num += 1
#         retgeneralocr = youtu.generalocr(imgname, data_type = 0)
#         # print(retgeneralocr)
#     else:
#         break

#id card validate: validate the idcard is correct
#retvalidateidcard = youtu.ValidateIdcard('123456789987654321', '张三', session_id)
#print retvalidateidcard

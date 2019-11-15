#coding=utf8
import itchat,time
from itchat.content import *
import requests


KEY = "bd004c485c024e0da3d3cf7d5efc7e72"

def get_response(msg):
    apiUrl = "http://www.tuling123.com/openapi/api"
    data = {
        'key':KEY,
        'info':msg,
        'userid':'wechat',
    }
    try:
        res = requests.post(apiUrl,data=data).json()
        return res.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received ' + msg['Text']
    Reply = get_response(msg['Text'])
    return Reply or defaultReply


itchat.auto_login()
#向文件助手发送消息
itchat.send('Hello ！！！！',toUserName='filehelper')

itchat.run()

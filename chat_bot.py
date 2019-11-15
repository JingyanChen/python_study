
import json

import requests

#coding=utf8
import itchat,time
from itchat.content import *
import requests

#思知机器人API

def get_sizhi_response(msg):

    apiUrl = 'https://api.ownthink.com/bot'

    apiKey = '31775623505ba955fb9dfb11cbdc31c2'#这里填写你自己申请的机器人apiKey

    data = {

        "spoken": msg,

        "appid": apiKey,

        "userid": 'fireworks'#随便起的

    }

    # 必须是json

    headers = {'content-type': 'application/json'}

 

    try:

        req = requests.post(apiUrl, headers = headers, data = json.dumps(data))

        return req.json()

    except:

        return

 

#处理思知机器人返回的json消息

def sizhi_msg(msg):

    #设置一个默认回复。

    return_msg = '我是个笨笨的机器人，我CPU好像挂了~_~![自动回复]'

    replyjson = get_sizhi_response(msg)

    if replyjson['message'] == 'success':

        return_msg = replyjson['data']['info']['text'].replace('小思','伦家~').replace('思知机器人','伦家~');

        print("小研自动回复："+return_msg)

    # a or b --》 如果a不为空就返回a，否则返回b

    return return_msg



@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received ' + msg['Text']
    Reply = "小研自动回答道: " + sizhi_msg(msg['Text'])
    return Reply or defaultReply


itchat.auto_login()
#向文件助手发送消息
itchat.send('Hello ！！！！',toUserName='filehelper')

itchat.run()

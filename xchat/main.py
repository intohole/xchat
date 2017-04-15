#coding-utf-8




import itchat

itchat.auto_login(enableCmdQR=True)


from collections import defaultdict
from b2 import consle2


_chats = defaultdict(list)

@itchat.msg_register(TEXT)
def simple_reply(msg):

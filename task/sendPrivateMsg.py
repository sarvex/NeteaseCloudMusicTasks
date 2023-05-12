import random


def start(user, task={}):
    if len(task['id']) > 0:
        user_id = random.choice(task['id'])

        msg = random.choice(task['msg']) if len(task['msg']) > 0 else '你好'
        music = user.music

        resp = music.msg_send(msg, [user_id])
        if resp['code'] == 200:
            user.taskInfo(task['taskName'], '发送成功')
        else:
            user.taskInfo(task['taskName'], user.errMsg(resp))

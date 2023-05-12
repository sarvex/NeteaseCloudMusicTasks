import time
import random


def start(user, task={}):
    music = user.music

    if len(task['id']) > 0:
        playlist_id = random.choice(task['id'])
    else:
        playlists = music.personalized_playlist(limit=10)
        playlist_ids = [playlist["id"] for playlist in playlists]
        playlist_id = random.choice(playlist_ids)

    event_msg = random.choice(task['msg']) if len(task['msg']) > 0 else '每日分享'
    result = music.share_resource(
        type='playlist', msg=event_msg, id=playlist_id)
    if result['code'] == 200:
        if task['delete']:
            time.sleep(0.5)
            event_id = result['id']
            delete_result = music.event_delete(event_id)
            user.taskInfo(task['taskName'], '发布成功，已删除动态')
        else:
            user.taskInfo(task['taskName'], '发布成功')
    else:
        user.taskInfo(task['taskName'], user.errMsg(result))

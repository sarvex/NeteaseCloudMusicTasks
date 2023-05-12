# -*- coding: utf-8 -*-
import requests


def getKey(data):
    config = data['config']
    return None if len(config['KEY']) == 0 else (config['module'], config['KEY'])


def push(title, mdmsg, mdmsg_compat, textmsg, config):
    msg = mdmsg
    key = config['KEY']
    if len(key) == 0:
        return

    if key.startswith('SCT'):
        url = f'https://sctapi.ftqq.com/{key}.send'
    else:
        url = f'https://sc.ftqq.com/{key}.send'

    requests.post(url, data={"text": title, "desp": msg})

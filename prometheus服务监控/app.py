# coding: utf-8
from flask import Flask, request
import json
import requests
import traceback

app = Flask(__name__)


def utc_s(utc):
    if utc == "":
        return ""
    origin_date_str = utc.strip().split('+')[0].split('.')[0].replace('Z', '').split('T')
    d = origin_date_str[0]
    time = origin_date_str[1].split(':')
    h = int(time[0]) + 8
    if h > 24:
        h = h - 24
    m, s = time[1], time[2]
    return '{} {}:{}:{}'.format(d, h, m, s)


def message_handler(message):
    alerts = message["alerts"]
    alert_message = []

    for i in range(len(alerts)):
        alert = alerts[i]

        status = alert.get("status", "")
        labels = alert.get("labels", {})
        annotations = alert.get("annotations", {})
        start_time = utc_s(alert.get("startsAt", ""))
        end_time = utc_s(alert.get("endsAt", ""))
        alert_name = labels.get("alertname", "")
        instance = labels.get("instance", "")
        description = annotations.get("description", "")
        title = status == 'resolved' and '解除' or ''

        message = "服务器告警 " + title + '\n' \
                  + "*******************" + '\n' \
                  + "状态: " + status + '\n' \
                  + "报警名称: " + alert_name + '\n' \
                  + "报警实例: " + instance + '\n' \
                  + "报警描述: " + description + '\n' \
                  + "开始时间: " + start_time + '\n' \
                  + "结束时间: " + end_time + '\n'
        alert_message.append(message)

@app.route('/message', methods=['POST'])
def gitlab_alert():
    url = "飞书webhook或者其他地址"

    json_data = json.loads(request.get_data(as_text=True))
    try:
        alert_messages = message_handler(json_data)
        for message in alert_messages:
            requests.post(url=url, json={"msg_type": "text", "content": {"text": message}})
    except Exception:
        requests.post(url=url, json={"msg_type": "text", "content": {"text": "警报接口报错 请及时查看 {}".format(traceback.format_exc())}})


@app.route('/critical_message', methods=['POST'])
def critical_alert():
    url = "飞书webhook或者其他地址"

    json_data = json.loads(request.get_data(as_text=True))
    try:
        alert_messages = message_handler(json_data)
        for message in alert_messages:
            requests.post(url=url, json={"msg_type": "text", "content": {"text": message}})
    except Exception:
        requests.post(url=url, json={"msg_type": "text", "content": {"text": "警报接口报错 请及时查看 {}".format(traceback.format_exc())}})

    return 'ok'


@app.route('/normal_message', methods=['POST'])
def normal_alert():
    url = "飞书webhook或者其他地址"

    json_data = json.loads(request.get_data(as_text=True))
    try:
        alert_messages = message_handler(json_data)
        for message in alert_messages:
            requests.post(url=url, json={"msg_type": "text", "content": {"text": message}})
    except Exception:
        requests.post(url=url, json={"msg_type": "text", "content": {"text": "警报接口报错 请及时查看 {}".format(traceback.format_exc())}})

    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

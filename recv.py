import json

import Utils


def main(uicontrol, jobcontrol):
    msgq = Utils.MsgQueue('q')

    def callback(ch, method, properties, body):
        datas = json.loads(body)
        for data in datas:
            uicontrol.showTableInfo(data)
            jobcontrol.addJob(data, uicontrol)

    msgq.channel.basic_consume(
        queue='q',
        on_message_callback=callback,
        auto_ack=True)
    msgq.channel.start_consuming()

import Utils

msgq = Utils.MsgQueue('q')
data = [
    ["销售", "前程无忧", "2024-02-19", "11:47"],
    ["IT", "前程无忧", "2024-02-19", "08:46"],
]
msgq.send(data)
msgq.connection.close()

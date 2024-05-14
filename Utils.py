import asyncio
import json
import queue
import tkinter

import pika
import pyppeteer


class MyBrowser:
    async def init(self):
        browser = await pyppeteer.launch(
            {
                'handleSIGINT': False,
                'handleSIGTERM': False,
                'handleSIGHUP': False,
                'headless': False,
                'args': ['--start-maximized']
            }
        )
        pages = await browser.pages()
        self.page = pages[0]
        width, height = self.screen_size()
        await self.page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                              '{ webdriver:{ get: () => false } }) }')
        await self.page.setViewport(viewport={'width': width, 'height': height})

    async def openPage(self, url):
        await self.page.goto(url, options={'timeout': 5 * 1000})

    async def waitUrlChange(self, url):
        while self.page.url == url:
            await asyncio.sleep(1)
        await asyncio.sleep(1)

    async def elementClick(self, xpath):
        element = await self.page.xpath(xpath)
        await element[0].click()
        await asyncio.sleep(2)

    async def testSleep(self):
        await asyncio.sleep(100000)

    async def elementInput(self, xpath, text):
        element = await self.page.xpath(xpath)
        await element[0].type(text)
        await asyncio.sleep(1)

    def screen_size(self):
        # 使用tkinter获取屏幕大小
        tk = tkinter.Tk()
        width = tk.winfo_screenwidth()
        height = tk.winfo_screenheight()
        tk.quit()
        return width, height


class ThQueue:
    def __init__(self):
        self.q = queue.Queue()

    def putInfo(self, info):
        self.q.put(info)

    def getInfo(self):
        return self.q.get()


class MsgQueue:
    def __init__(self, queuename):
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials,
                                               heartbeat=60)
        self.queuename = queuename
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queuename)

    def send(self, data):
        data = json.dumps(data)
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queuename,
            body=data
        )

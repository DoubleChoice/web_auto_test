import datetime
import json
import threading
import time

import requests
import webdriver_manager.chrome
from PyQt6.QtWidgets import QTableWidgetItem, QListWidgetItem
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import Utils
import 前程无忧
import 智联招聘
from pynput.mouse import Listener, Controller


class MyBrowser:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        try:
            self.browser = webdriver.Chrome(options=chrome_options)
        except:
            self.browser = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install(),
                                            options=chrome_options)

        self.pageControl = PageControl(self.browser)
        self.elementControl = ElementControl(self.browser)
        self.scrollControl = ScrollControl(self.browser)

    def testSleep(self):
        time.sleep(100000000)


class PageControl:
    def __init__(self, browser):
        self.browser = browser

    def openPage(self, url):
        self.browser.get(url)
        self.browser.maximize_window()
        time.sleep(3)

    def waitUrlChange(self, url):
        while self.browser.current_url == url:
            time.sleep(1)
        time.sleep(3)

    def quit(self):
        self.browser.quit()

    def getHandle(self):
        handles = self.browser.window_handles
        return handles

    def handleControl(self, index):
        self.browser.switch_to.window(self.getHandle()[index])

    def close(self):
        self.browser.close()


class ElementControl:
    def __init__(self, browser):
        self.browser = browser

    def elementInput(self, xpath, text):
        self.browser.find_element(By.XPATH, xpath).send_keys(text)
        time.sleep(2)

    def elementClick(self, xpath, sec):
        self.browser.find_element(By.XPATH, xpath).click()
        time.sleep(sec)

    def elementHover(self, xpath):
        ActionChains(self.browser).move_to_element(self.browser.find_element(By.XPATH, xpath)).perform()
        time.sleep(2)


class ScrollControl:
    def __init__(self, browser):
        self.browser = browser

    def scrollDown(self):
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)

    def scrollUP(self):
        self.browser.execute_script('window.scrollTo(0,0)')

    def scrollTo(self, x, y):
        self.browser.execute_script('window.scrollTo(%s,%s)' % (x, y))


class UIControl:
    def __init__(self, ui):
        self.ui = ui

    def showTableInfo(self, data):
        print(data)
        self.data = data
        self.ui.tableWidgetToDo.setRowCount(self.ui.tableWidgetToDo.rowCount() + 1)
        currowindex = self.ui.tableWidgetToDo.rowCount() - 1
        self.ui.tableWidgetToDo.setItem(currowindex, 0, QTableWidgetItem(data[0]))
        self.ui.tableWidgetToDo.setItem(currowindex, 1, QTableWidgetItem(data[1]))
        self.ui.tableWidgetToDo.setItem(currowindex, 2, QTableWidgetItem(data[2] + ' ' + data[3]))
        self.ui.tableWidgetToDo.setItem(currowindex, 3, QTableWidgetItem('未完成'))

    def changeTableByIndex(self, info, t):
        for row in range(self.ui.tableWidgetToDo.rowCount()):
            item = self.ui.tableWidgetToDo.item(row, 0)
            print(item.text())
            if item.text() == info:
                self.ui.tableWidgetToDo.setItem(row, 3, QTableWidgetItem(t))
                break

    def onItemChanged(self, currentItem: QListWidgetItem, previousItem: QListWidgetItem):
        if currentItem.text() == '服务':
            self.showServePage()
        elif currentItem.text() == '岗位信息':
            self.showJobInfo()
        elif currentItem.text() == '获取简历':
            self.showResumeInfo()

    def showServePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.servePage)

    def showJobInfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.jobPage)

    def showResumeInfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.resumePage)


class JobControl:
    def __init__(self, ui):
        self.scheduler = BlockingScheduler()
        self.ui = ui

    def addJob(self, args, uicontrol):
        time = args[3].split(':')
        self.hour = time[0]
        self.min = time[1]
        date = args[2].split('-')
        self.year = date[0]
        self.month = date[1]
        self.day = date[2]
        self.scheduler.add_job(self.startPage, 'date',
                               run_date=datetime.datetime(int(self.year), int(self.month), int(self.day),
                                                          int(self.hour), int(self.min), 00), args=[args, uicontrol])
        threading.Thread(target=self.scheduler.start, args=()).start()

    def startPage(self, info, uicontrol):
        tQueue = Utils.ThQueue()
        if info[1] == '前程无忧':
            threading.Thread(target=前程无忧.main, args=(info, tQueue,)).start()
        elif info[1] == '智联招聘':
            threading.Thread(target=智联招聘.main, args=(info, tQueue,)).start()
        resInfo = tQueue.getInfo()
        if resInfo[1] == '发生错误':
            threading.Thread(target=self.reStart, args=(info, tQueue)).start()
        uicontrol.changeTableByIndex(resInfo[0][0], resInfo[1])
        json.dumps(resInfo)
        requests.post(url='http://127.0.0.1:5000/api', json=resInfo)

    def reStart(self, info, tQueue):
        mouse = Controller()
        prex, prey = mouse.position
        time.sleep(5)
        nowx, nowy = mouse.position
        while nowx != prex and nowy != prey:
            time.sleep(5)
            prex = nowx
            prey = nowy
            nowx, nowy = mouse.position
        if info[1] == '前程无忧':
            前程无忧.main(info, tQueue)
        elif info[1] == '智联招聘':
            智联招聘.main(info, tQueue)

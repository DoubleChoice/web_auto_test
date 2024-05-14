import MyUtils


def main(data, tQueue):
    try:
        url = 'https://ehire.51job.com/Revision/login?returl=Revision%2Fnavigate%3Frt%3D1706681295676&erd=1'
        browser = MyUtils.MyBrowser()
        browser.pageControl.openPage(url)
        browser.pageControl.waitUrlChange(url)
        # 职位管理
        browser.elementControl.elementClick('/html/body/div/div[1]/div[2]/div/div[1]/ul/li[2]', 3)
        # 新增职位
        browser.elementControl.elementClick(
            '/html/body/div/div[1]/div[2]/div/div[2]/section/div/div/div[1]/div[1]/div[2]/button/span', 5)
        # 职位名称
        browser.elementControl.elementInput(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/section/div/div/div[2]/form/div[6]/div/div/div[1]/div[1]/input',
            '销售')
        # 职位描述
        browser.elementControl.elementInput(
            '/html/body/div/div[1]/div[2]/div/div[2]/section/div/div/div[2]/form/div[8]/div/div[1]/div/textarea',
            '负责公司门店等销售业务')
        # 学历
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/section/div/div/div[2]/form/div[14]/div/div[1]/div/input', 1)
        # 本科
        browser.elementControl.elementClick('/html/body/div[3]/div[1]/div[1]/ul/li[2]', 1)
        # 薪资范围
        browser.elementControl.elementInput(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/section/div/div/div[2]/form/section[1]/form/div[1]/div/div[2]/div[3]/div/div[1]/input',
            '6000')
        browser.elementControl.elementInput(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/section/div/div/div[2]/form/section[1]/form/div[1]/div/div[2]/div[4]/div/div[1]/input',
            '8000')
        # 发薪日
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/section/div/div/div[2]/form/section[1]/form/div[2]/div/div/div/input',
            1)
        # 日期
        browser.elementControl.elementClick('/html/body/div[4]/div[1]/div[1]/ul/li[16]', 1)
        # 加速器
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[1]/div[2]/div/div[2]/section/div/div/div[2]/div[3]/main/div[2]/div[1]/div[2]/div[2]/span',
            1)
        # 保存
        browser.elementControl.elementClick('//*[@id="sensor_new_save"]', 1)
        # 确定
        browser.elementControl.elementClick('/html/body/div[5]/div/div[3]/button', 1)
        tQueue.putInfo([data, '完成'])
    except:
        tQueue.putInfo([data, '发生错误'])
        browser.testSleep()

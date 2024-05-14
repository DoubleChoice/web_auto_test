import MyUtils


def main(data, tQueue):
    try:
        url = 'https://passport.zhaopin.com/org/login?validateCampus='
        browser = MyUtils.MyBrowser()
        browser.pageControl.openPage(url)
        browser.pageControl.waitUrlChange(url)
        # 职位中心
        browser.elementControl.elementClick('/html/body/div[1]/div[1]/div[4]/div[2]/a/span', 1)
        # 发布职位
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/button/div', 3)
        # 性质
        browser.pageControl.handleControl(-1)
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[1]/div/div[2]/div[1]/div[1]/button/div',
            1)
        # 名称
        browser.elementControl.elementInput(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[3]/div[2]/div/div[1]/input',
            '金融销售')
        # 描述
        browser.elementControl.elementInput(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[4]/div[2]/div[1]/div[1]/div/div[4]',
            '负责公司销售业务xxxxxxxxxxxxx')
        # 类别
        browser.elementControl.elementHover(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[5]/div[2]/div/div')
        # 学历
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[8]/div[1]/div[1]/div[2]/div/div[1]/input',
            1)
        # 滚动条
        browser.scrollControl.scrollDown()
        # 本科
        browser.elementControl.elementClick('/html/body/div[9]/div/div/div/div[1]/div/div/a[6]/div', 1)
        # 工作经验
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[8]/div/div[2]/div/div/div[1]/input',
            1)
        browser.elementControl.elementClick('/html/body/div[10]/div/div/div/div/div/div/a[3]/div', 1)
        # 薪资
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[9]/div/div[2]/div/div[1]/input',
            1)
        browser.elementControl.elementClick('/html/body/div[11]/div/div/div/div[1]/div/div/a[9]/div/div', 1)
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[9]/div[2]/div/div/div[1]/input',
            1)
        browser.elementControl.elementClick('/html/body/div[12]/div/div/div/div[1]/div/div/a[7]/div', 1)
        # 关键词
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[11]/div[1]/div[2]/div[1]/div/div/div',
            1)
        browser.elementControl.elementClick('/html/body/div[2]/div/div/div[2]/div/div[1]/div/ul/li[3]/ul/li[4]', 1)

        # 确认
        browser.elementControl.elementClick('/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/button[2]/span', 1)
        # 查看效果
        browser.elementControl.elementClick(
            '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form/div[17]/div[2]/button[2]/div', 1)
        tQueue.putInfo([data, '完成'])
    except:
        tQueue.putInfo([data, '发生错误'])
        while True:
            pass

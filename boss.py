import asyncio

import Utils


def screen_size():
    # 使用tkinter获取屏幕大小
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def main():
    url = 'https://www.zhipin.com/web/user/?intent=1&ka=header-boss'
    browser = Utils.MyBrowser()
    await browser.init()
    await browser.openPage(url)
    await browser.waitUrlChange(url)
    # 职位管理
    await browser.elementClick('/html/body/div[2]/div[1]/div[1]/dl[1]/dt/a/text()')
    # 发布职位
    await browser.elementClick('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div')
    # 招聘类型
    await browser.elementClick('/html/body/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div')
    # 职位名称
    await browser.elementInput('/html/body/div[1]/div/div/div/div[2]/div[4]/div[2]/span/input', '销售')
    await browser.elementInput('/html/body/div[1]/div/div/div/div[2]/div[5]/div[2]/div/textarea',
                               '负责公司的电话销售工作xxxxxxxxxxxxxxxxxxxxx')
    # 经验
    await browser.elementClick('/html/body/div[1]/div/div/div/div[2]/div[8]/div[2]/div[1]/div[1]/div')
    await browser.elementClick('/html/body/div[1]/div/div/div/div[2]/div[8]/div[2]/div[1]/div[2]/ul[2]/li[3]')
    # 学历
    await browser.elementClick('/html/body/div[1]/div/div/div/div[2]/div[8]/div[2]/div[2]/div[1]/div')
    await browser.elementClick('/html/body/div[1]/div/div/div/div[2]/div[8]/div[2]/div[2]/div[2]/ul[2]/li[6]')
    # 薪资范围
    await browser.elementClick('/html/body/div[1]/div/div/div/div[2]/div[9]/div[2]/div/span')
    # 最低薪资
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/span')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/ul[2]/li[8]')
    # 最高薪资
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/ul[2]/li[2]')
    # N薪
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/span/div/div[1]/div/span')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/span/div/div[2]/ul[2]/li[2]')
    # 底薪
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div/label/span[1]/input')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/span')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul[2]/li[21]')
    # 社保
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/span')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/ul[2]/li[3]')
    # 提成
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[4]/div/div[1]/div[2]/div/div[1]/div')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[4]/div/div[1]/div[2]/div/div[2]/ul[2]/li[3]')
    # 奖金
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[5]/div/div[2]/div[1]/span/div[1]')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[5]/div/div[2]/div[1]/span/div[2]/span[8]')
    await browser.elementClick('/html/body/div[3]/div[2]/div[2]/div/div[5]/div/div[2]/div[1]/span/div[2]/span[4]')
    # 确定
    await browser.elementClick('/html/body/div[3]/div[2]/div[3]/div/span[2]/text()')
    # 关键词
    await browser.elementClick('/html/body/div[1]/div/div/div/div[2]/div[10]/div[2]/div/div/i')
    # ToC
    await browser.elementClick('/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/ul/li[1]')
    await browser.elementClick('/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/ul/li[3]')
    await browser.elementClick('/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[2]/div[3]/ul/li[4]')
    await browser.elementClick('/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[2]/div[5]/ul/li[8]')
    await browser.testSleep()


asyncio.get_event_loop().run_until_complete(main())

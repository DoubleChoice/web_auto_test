import MyUtils

url = 'https://passport.58.com/login/?path=https%3A%2F%2Fnc.58.com%2Fsearchjob.shtml%3Fspm%3Du-2few7p4vh988mb62t1.2hb8qj4p13vhwqfjjkg.ad_zcm.ac_r21197072.cr_r742201085729.cd_r9887724151222522138&source=58-homepage-pc&PGTID=0d202409-0029-dbc7-bda2-141ea48f97f1&ClickID=65'
browser = MyUtils.MyBrowser()
browser.pageControl.openPage(url)
browser.pageControl.waiturlChange(url)

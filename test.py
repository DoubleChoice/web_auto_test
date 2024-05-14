import time

from pynput.mouse import Controller

mouse = Controller()
prex, prey = mouse.position
time.sleep(3)
nowx, nowy = mouse.position
while nowx != prex and nowy != prey:
    time.sleep(3)
    print(prex,prey,nowx,nowy)
    prex = nowx
    prey = nowy
    nowx, nowy = mouse.position
print("启动")
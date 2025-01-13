# 90분 동안 아무런 조작이 없으면 런타임이 종료되기 때문에 1시간마다 코랩을 열어주는 코드

import time
import datetime
import webbrowser

for i in range(12):
    browse = webbrowser.get("chrome")
    browse.open(
        "https://colab.research.google.com/drive/1cmyhNX5IOTQMMl_bKatHvIf2Zu5g3uhP#scrollTo=3EP14ocW5K6q"
    )
    print(i, datetime.datetime.today())
    time.sleep(60 * 60)

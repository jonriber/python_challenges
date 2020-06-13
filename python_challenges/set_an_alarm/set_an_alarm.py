# I´m supposed to create an alarm function
# It should have a time to set the alarm, a sound to play and a message
# main function should have 3 entry paramethers

import time #módulo para lidar com variaveis de tempo
import sched #módulo para lidar com eventos agendados
import winsound as ws #módulo para tocar sons no windows


def set_alarm(time_alarm,sound,message):
    s = sched.scheduler(time.time,time.sleep) #instancia de sched em s
    s.enterabs(time_alarm, 1,print,argument=(message,))
    s.enterabs(time_alarm, 1, ws.PlaySound, argument= (sound,ws.SND_FILENAME))
    print('Alarm set for',time.asctime(time.localtime(time_alarm)))
    s.run()

if __name__ == '__main__':
    pass
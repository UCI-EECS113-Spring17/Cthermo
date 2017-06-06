
# coding: utf-8

# In[1]:

from pynq import Overlay
Overlay("base.bit").download()

from pynq.iop import Pmod_PWM
from pynq.iop import PMODA

pwm = Pmod_PWM(PMODA, 0)

period=20000
duty=2
duty2 = 12
current =7 
pwm.generate(period,current)

while (1):
    num = input()
    if (num == "0"):
        current=current+1
        pwm.generate(period,current)
    if(num == "1"):
        current=current-1
        pwm.generate(period,current)
    if(num == "2"):
        break
pwm.stop()



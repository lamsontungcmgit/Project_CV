import sys
import uselect
from mqtt import *
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from aiot_lcd1602 import LCD1602
import time
from wifi import __wifi__
from aiot_hcsr04 import HCSR04
from machine import RTC
import ntptime
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
import music
from homebit3_ir_receiver import *

def read_terminal_input():
  spoll=uselect.poll()        # Set up an input polling object.
  spoll.register(sys.stdin, uselect.POLLIN)    # Register polling object.

  input = ''
  if spoll.poll(0):
    input = sys.stdin.read(1)

    while spoll.poll(0):
      input = input + sys.stdin.read(1)

  spoll.unregister(sys.stdin)
  return input

# Mô tả hàm này...
def Gi_E1_BB_8Dng_n_C3_B3i():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  l_E1_BB_87nh_AI = read_terminal_input()
  if l_E1_BB_87nh_AI == 'A':
    mqtt.publish('nutnhan1', '1')
  if l_E1_BB_87nh_AI == 'B':
    mqtt.publish('nutnhan1', '0')

aiot_lcd1602 = LCD1602()

# Mô tả hàm này...
def _C4_91o_kho_E1_BA_A3ng_c_C3_A1ch():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  if aiot_ultrasonic.distance_cm() < 5:
    display.set_all('#000000')
  else:
    if aiot_ultrasonic.distance_cm() < 50:
      display.set_all('#ffffff')
      mqtt.publish('nutnhan1', '1')
      aiot_lcd1602.clear()
      aiot_lcd1602.move_to(0, 0)
      aiot_lcd1602.putstr('LED ON')
      time.sleep_ms(5000)
      mqtt.publish('nutnhan1', '0')
    else:
      display.set_all('#000000')

def on_mqtt_message_receive_callback__nutnhan1_(th_C3_B4ng_tin):
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, status, j, k
  if th_C3_B4ng_tin == '1':
    aiot_lcd1602.clear()
    aiot_lcd1602.move_to(0, 0)
    aiot_lcd1602.putstr('LED ON')
  else:
    aiot_lcd1602.clear()
    aiot_lcd1602.move_to(0, 0)
    aiot_lcd1602.putstr('LED OFF')

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

# Mô tả hàm này...
def G_E1_BB_ADi_nhi_E1_BB_87t__C4_91_E1_BB_99_v_C3_A0__C4_91_E1_BB_99__E1_BA_A9m():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  Cycle = (Cycle if isinstance(Cycle, (int, float)) else 0) + 1
  if Cycle == 20:
    Cycle = 0
    aiot_dht20.read_dht20()
    mqtt.publish('cambien1', (aiot_dht20.dht20_temperature()))
    mqtt.publish('cambien2', (aiot_dht20.dht20_humidity()))

# Mô tả hàm này...
def B_E1_BA_ADt__C4_91_C3_A8n_l_C3_BAc_17h():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  if ('%0*d' % (2, RTC().datetime()[4])) == '17' and ('%0*d' % (2, RTC().datetime()[5])) == '0' and ('%0*d' % (2, RTC().datetime()[6])) == '0':
    mqtt.publish('nutnhan1', '1')

# Mô tả hàm này...
def Nh_E1_BA_ADn_di_C3_AAn_khu_C3_B4n_m_E1_BA_B7t():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  if enable_ai == 1:
    if check_FaceID() == 1:
      music.play(['C4:1'], wait=True)
      enable_ai = 0
      display.show(Image("88888:88888:88888:88888:88888"))
      mqtt.publish('nutnhan2', '1')
      display.clear()
    else:
      display.show(Image("88888:80008:88888:80008:80008"))
      time.sleep_ms(500)

# Mô tả hàm này...
def check_FaceID():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  Face_IDreturn = read_terminal_input()
  if Face_IDreturn == 'True':
    return 1
  return 0

# Mô tả hàm này...
def changeSignal():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  if signal == (IR_REMOTE_0):
    return 0
  if signal == (IR_REMOTE_1):
    return 1
  if signal == (IR_REMOTE_2):
    return 2
  if signal == (IR_REMOTE_3):
    return 3
  if signal == (IR_REMOTE_4):
    return 4
  if signal == (IR_REMOTE_5):
    return 5
  if signal == (IR_REMOTE_6):
    return 6
  if signal == (IR_REMOTE_7):
    return 7
  if signal == (IR_REMOTE_8):
    return 8
  if signal == (IR_REMOTE_9):
    return 9
  if signal == (IR_REMOTE_A):
    return 11
  if signal == (IR_REMOTE_C):
    return 10
  if signal == (IR_REMOTE_B):
    return 12
  return 13

homebit3_ir_rx = IR_RX(Pin(pin1.pin, Pin.IN)); homebit3_ir_rx.start();

def on_ir_receive_callback(t_C3_ADn_hi_E1_BB_87u, addr, ext):
  global l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k
  signal = t_C3_ADn_hi_E1_BB_87u
  number = changeSignal()
  if incorrect_number > 5:
    if number == 12:
      music.play(['G3:0.25'], wait=True)
      if enable_ai == 0:
        enable_ai = 1
      else:
        enable_ai = 0
        display.clear()
  else:
    if number == 12:
      if open2 == 0:
        music.play(['G3:0.25'], wait=True)
        if status > 0:
          music.play(['D3:1'], wait=True)
          status = 0
          input2 = []
          display.show(Image("80008:08080:00800:08080:80008"))
          time.sleep_ms(250)
        if enable_ai == 0:
          enable_ai = 1
        else:
          enable_ai = 0
          display.clear()
    else:
      if enable_ai == 0:
        if number == 11:
          music.play(['G3:0.25'], wait=True)
          if open2 == 0:
            if status > 0:
              music.play(['D3:1'], wait=True)
              status = 0
              input2 = []
              display.show(Image("80008:08080:00800:08080:80008"))
              time.sleep_ms(250)
            open2 = 1
            display.show(Image("88888:80008:80008:80008:88888"))
          else:
            input2 = []
            open2 = 0
            display.show(Image("88888:80000:88888:80000:88888"))
            time.sleep_ms(500)
            display.clear()
        else:
          if open2 == 1 and number < 10:
            music.play(['G3:0.25'], wait=True)
            display.scroll(number)
            if len(input2) < 3:
              input2.append(number)
            elif len(input2) == 3:
              input2.append(number)
              if checkPassword() == 1:
                music.play(['C4:1'], wait=True)
                input2 = []
                open2 = 0
                display.show(Image("88888:88888:88888:88888:88888"))
                mqtt.publish('nutnhan2', '1')
                display.clear()
              else:
                music.play(['D3:1'], wait=True)
                input2 = []
                incorrect_number = (incorrect_number if isinstance(incorrect_number, (int, float)) else 0) + 1
                if incorrect_number > 5:
                  open2 = 0
                  display.show(Image("80008:08080:00800:08080:80008"))
                  time.sleep_ms(250)
                  display.show(Image("88888:80000:88888:80000:88888"))
                  time.sleep_ms(250)
                  display.clear()
                else:
                  display.show(Image("80008:08080:00800:08080:80008"))
                  time.sleep_ms(500)
                  display.show(Image("88888:80008:80008:80008:88888"))
          elif open2 == 0:
            if number == 10:
              if status == 0:
                music.play(['G3:0.25'], wait=True)
                status = 1
                display.show(Image("88888:80000:80000:80000:88888"))
            elif number < 10 and status > 0:
              music.play(['G3:0.25'], wait=True)
              display.scroll(number)
              if len(input2) < 3:
                input2.append(number)
              elif len(input2) == 3:
                input2.append(number)
                if status == 1:
                  if checkPassword() == 1:
                    input2 = []
                    status = 2
                    display.show(Image("88888:88800:88000:88800:88888"))
                  else:
                    music.play(['D3:1'], wait=True)
                    input2 = []
                    status = 0
                    display.show(Image("80008:08080:00800:08080:80008"))
                    time.sleep_ms(250)
                    display.show(Image("88888:80000:88888:80000:88888"))
                    time.sleep_ms(250)
                    display.clear()
                elif status == 2:
                  for j in range(4):
                    new_password[int(j - 1)] = input2[int(j - 1)]
                  input2 = []
                  status = 3
                  display.show(Image("88888:88880:88800:88880:88888"))
                elif status == 3:
                  if checkNewPassword() == 1:
                    for k in range(4):
                      password[int(k - 1)] = input2[int(k - 1)]
                    music.play(['C4:1'], wait=True)
                    input2 = []
                    status = 0
                    display.show(Image("88888:88888:88888:88888:88888"))
                    time.sleep_ms(500)
                    display.clear()
                  else:
                    music.play(['D3:1'], wait=True)
                    input2 = []
                    status = 0
                    display.show(Image("80008:08080:00800:08080:80008"))
                    time.sleep_ms(250)
                    display.show(Image("88888:80000:88888:80000:88888"))
                    time.sleep_ms(250)
                    display.clear()
  homebit3_ir_rx.clear_code()

homebit3_ir_rx.on_received(on_ir_receive_callback)

# Mô tả hàm này...
def checkPassword():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  for i in range(4):
    if input2[int(i - 1)] != password[int(i - 1)]:
      return 0
  return 1

# Mô tả hàm này...
def checkNewPassword():
  global t_C3_ADn_hi_E1_BB_87u, l_E1_BB_87nh_AI, Cycle, Face_IDreturn, signal, i, number, enable_ai, incorrect_number, input2, password, new_password, open2, th_C3_B4ng_tin, status, j, k, homebit3_ir_rx, aiot_ultrasonic, aiot_dht20, aiot_lcd1602
  for i in range(4):
    if input2[int(i - 1)] != new_password[int(i - 1)]:
      return 0
  return 1

if True:
  display.show(Image.HEART)
  mqtt.connect_wifi('Vu', '88888888')
  __wifi__.connect_wifi('Vu', '88888888')
  aiot_ultrasonic = HCSR04(trigger_pin=pin3.pin, echo_pin=pin6.pin)
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='todiuquang123', password='YOUR_ADAFRUIT_IO_KEY')
  ntptime.settime()
  (year, month, mday, week_of_year, hour, minute, second, milisecond) = RTC().datetime()
  RTC().init((year, month, mday, week_of_year, hour+7, minute, second, milisecond))
  Cycle = 0
  display.scroll('ok')
  mqtt.on_receive_message('nutnhan1', on_mqtt_message_receive_callback__nutnhan1_)
  open2 = 0
  status = 0
  signal = 0
  number = 0
  incorrect_number = 0
  enable_ai = 0
  input2 = []
  password = [0] * 4
  new_password = [0] * 4

while True:
  _C4_91o_kho_E1_BA_A3ng_c_C3_A1ch()
  Gi_E1_BB_8Dng_n_C3_B3i()
  Nh_E1_BA_ADn_di_C3_AAn_khu_C3_B4n_m_E1_BA_B7t()
  G_E1_BB_ADi_nhi_E1_BB_87t__C4_91_E1_BB_99_v_C3_A0__C4_91_E1_BB_99__E1_BA_A9m()
  B_E1_BA_ADt__C4_91_C3_A8n_l_C3_BAc_17h()
  mqtt.check_message()
  time.sleep_ms(1000)


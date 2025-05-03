#!/usr/bin/env python3

from evdev import InputDevice, ecodes
import subprocess
from time import sleep

# Настройки
TOUCHBAR_DEVICE = '/dev/input/event2'
X_MAX = 23044  # Максимальное значение координаты X
DEAD_ZONE = 200  # Минимальная дистанция свайпа
STEP = 1  # Шаг изменения в %
kbd_status = False
screen_brightness = 50 # По дефолту

def change_volume(percent):
    """Изменение громкости"""
    cmd = f"pactl set-sink-volume @DEFAULT_SINK@ {percent}%"
    # print(f"[VOLUME] {cmd}")
    subprocess.run(cmd, shell=True)

# def change_brightness(percent):
#     """Плавное изменение яркости экрана до заданного процента"""
#     global screen_brightness
#     iteration = 1   
#     while screen_brightness != percent:
#         if screen_brightness > percent:
#             screen_brightness -= iteration  # Уменьшаем яркость
#         else:
#             screen_brightness += 1  # Увеличиваем яркость
#         iteration += 5
#         cmd = f"brightnessctl -d apple-panel-bl set {screen_brightness}%"
#         subprocess.run(cmd, shell=True)

def change_brightness(percent):
    """Плавное изменение яркости экрана до заданного процента"""
    cmd = f"brightnessctl -d apple-panel-bl set {percent}%"
    subprocess.run(cmd, shell=True)


def change_kbd_brightness(percent):
    """Изменение яркости экрана"""
    global kbd_status
    if percent < 20:
        if kbd_status == False:
            while percent > 1:
                cmd = f"brightnessctl -d kbd_backlight set {percent}%"
                subprocess.run(cmd, shell=True)
                percent /= 1.5
                sleep(0.1)
            kbd_status = True    
            cmd = f"brightnessctl -d kbd_backlight set 0%"
            subprocess.run(cmd, shell=True)
    else:
        cmd = f"brightnessctl -d kbd_backlight set {percent}%"
        subprocess.run(cmd, shell=True)
        kbd_status = False

def main():
    try:
        dev = InputDevice(TOUCHBAR_DEVICE)
        print(f"Слушаем события Touch Bar... (Ctrl+C для выхода)")

        start_x = 0
        touch_active = False

        for event in dev.read_loop():
            # Обработка касания
            if event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOUCH:
                touch_active = event.value
                if touch_active:
                    start_x = 0  # Сброс при новом касании

            # Обработка движения
            elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X:
                if touch_active:
                    if start_x == 0:  # Фиксируем начальную позицию
                        start_x = event.value
                    else:
                        delta = event.value - start_x
                        if abs(delta) > DEAD_ZONE:  # Фильтр случайных касаний
                            zone = "left" if start_x < X_MAX/2 else "right"
                            direction = "+" if delta > 0 else "-"
                            
                            if zone == "left": # ecodes.ABS_Y:
                                percent = int(event.value/(X_MAX/2)*100)
                                change_volume(percent)
                            else:
                                percent = int(abs((X_MAX/2)-event.value)/(X_MAX/2)*100)
                                change_brightness(percent)
                                # change_kbd_brightness(100-percent)
                            start_x = 0  # Сброс после обработки
        print(event)
    except KeyboardInterrupt:
        print("\nЗавершение работы")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

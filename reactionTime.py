#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyautogui
import time
import webbrowser

# Abre la página del juego
webbrowser.open('https://www.humanbenchmark.com/tests/reactiontime', new=2)
time.sleep(3)  # Tiempo para que la página se cargue

# Ajustes específicos para la resolución 1366x768
width, height = pyautogui.size()
target_x = int(width / 2)
target_y = int(height / 2)

# Función para verificar si el color es verde (#4bdb6a)
def is_green_color(color):
    return color == (75, 219, 106)

# Función para esperar hasta que el color cambie a verde
def wait_for_green_color():
    while True:
        color = pyautogui.pixel(target_x, target_y)
        if is_green_color(color):
            break

# Comienza el juego
pyautogui.click(target_x, target_y)  # Haz clic para empezar
time.sleep(1)  # Espera un segundo antes de empezar

# Configuración personalizable
delay = 0.1 
lvls = 5

for _ in range(lvls):
    wait_for_green_color()
    time.sleep(delay)
    pyautogui.click(target_x, target_y)
    time.sleep(0.1)  # Espera corta antes de hacer clic nuevamente para el próximo nivel

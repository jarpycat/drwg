import win32api, win32con, mouse, time, random

SCREEN_SIZE = (1920,1080,)

mouse_down = False
intensity = 20
randomisation = 3

def move(x, y):
	win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x), int(y))

def on_mouse_down():
	global mouse_down
	mouse_down = True

def on_mouse_up():
	global mouse_down
	mouse_down = False

mouse.on_button(buttons=(mouse.LEFT), callback=on_mouse_down, types=(mouse.DOWN))
mouse.on_button(buttons=(mouse.LEFT), callback=on_mouse_up, types=(mouse.UP))

while True:
	if mouse_down:
		move(0, (intensity + random.randint(-randomisation, randomisation)))

	time.sleep(1/9)
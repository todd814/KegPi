import time
from random import randint
from flowmeter import *
import pytest

rand_flow = randint(142, 200)
f = FlowMeter()
clicks = 0

while True:
	if (clicks < rand_flow):
		clicks = clicks + 1
		time.sleep(.01)
		f.update()
	else:
		print "stopped"
		time.sleep(10)
		print f.last_pour_func()
		f.calibrate()
		print f.last_pour_in_oz()
		print f.last_pour_in_ml()
		break
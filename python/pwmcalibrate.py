import time, json, curses, wiringpi

PWM_MAX = 1023
DEFAULT_PIN = 1
DEFAULT_CALIBRATION_FILENAME = "pwmcalibrate.json"

class PWMCalibrator(object):
	"""Helper class for calibrating PWM-driven VU meters"""
	def __init__(self, pin=DEFAULT_PIN, calibration_file=None):
		super(PWMCalibrator, self).__init__()
		
		self.pin = pin

		wiringpi.wiringPiSetup()
		wiringpi.pinMode(self.pin, wiringpi.PWM_OUTPUT)

		self.calibration = []
		if calibration_file is not None:
			self.load(calibration_file)

	def load(self, filename=DEFAULT_CALIBRATION_FILENAME):
		f = open(filename, 'r')
		self.calibration = json.load(f)
		f.close()

	def setPWM(self, value):
		bottom_step = 0
		for i in range(0, len(self.calibration)-1):
			if value>=self.calibration[i][0] and value<self.calibration[i+1][0]:
				bottom_step = i

		# if it's an exact match (we have a specific lookup for this value) then use that precise calibration
		if value==self.calibration[bottom_step][0]:
			wiringpi.pwmWrite(self.pin, self.calibration[bottom_step][1])
		else:
			pct_diff = (value - self.calibration[bottom_step][0]) / (1.0 * (self.calibration[bottom_step + 1][0] - self.calibration[bottom_step][0]))
			pwm_value = self.calibration[bottom_step][1] + round(pct_diff * (self.calibration[bottom_step + 1][1] - self.calibration[bottom_step][1]))
			wiringpi.pwmWrite(self.pin, pwm_value)


	def calibrate(self, steps=None):
		# clear the calibration list
		self.calibration = []

		# init curses, preventing delay on keypress
		stdscr = curses.initscr()
		curses.cbreak()
		stdscr.nodelay(1)

		# max the display, ask for trim pot adjustment
		wiringpi.pwmWrite(self.pin, PWM_MAX)
		if steps==None:
			steps = int(input("Calibrate the trim pot until the meter is at maximum, then enter the desired number of steps and press <enter>"))
		else:
			input("Calibrate the trim pot until the meter is at maximum (%d), then press <enter>" % steps)
		
		# set the top step
		self.calibration.append((steps, PWM_MAX))

		# step down through the PWM range
		current_step = steps - 1
		for i in range(PWM_MAX, 0, -1):			
			wiringpi.pwmWrite(self.pin, i)

			stdscr.addstr(0,10,"Press the spacebar when the meter reads %s%d" % (curses.COLOR_RED, current_step))
			stdscr.refresh()

			key = stdscr.getch()
			if key==ord(' '):
				self.calibration.append((current_step, i))
				current_step = current_step - 1
				if current_step<0:
					break
			time.sleep(0.05)

		# append an entry for zero if one wasn't recorded
		found_zero = False
		for x in self.calibration:
			if x[0]==0:
				found_zero = True
		if not found_zero:
			self.calibration.append((0,0))

		# end the curses session
		curses.endwin()

		# sort the calibration list
		self.calibration.sort(lambda x: x[0])


	def save(self, filename=DEFAULT_CALIBRATION_FILENAME):
		f = open(filename, 'w')
		json.dump(self.calibration, f)
		f.close()



def main():
	c = PWMCalibrator()
	c.calibrate()
	c.save()

if __name__ == '__main__':
	main()

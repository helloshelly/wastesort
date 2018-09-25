import RPi.GPIO as GPIO
import sys, os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)


GPIO.output(13,0)
GPIO.output(18,0)
GPIO.output(10,0)

def pause():
	programPause = raw_input("Press ENTER to continue")


def getResult():
	file =open("result.txt","r")
	lines = file.readline()
	print(lines)
	if(lines == '1'):
		print("Compost")
		GPIO.output(13,1)
	if(lines == '2'):
		print("Recycling")
		GPIO.output(18,1)
	if(lines == '3'):
		print("Landfill")
		GPIO.output(10,1)
	file.close()

try:
        while True:
                if(GPIO.input(11)==1):
			GPIO.output(13,0)
			GPIO.output(18,0)
			GPIO.output(10,0)
			os.system("./runProgram.sh")
			pause()
			getResult()
		

except KeyboardInterrupt:
        GPIO.cleanup()
	sys.exit()






               

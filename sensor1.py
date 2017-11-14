#import the GPIO library
import RPi.GPIO as GPIO

#import the time library
from time import time
from time import sleep

#Use the Broadcom method for naming the GPIO pins   
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#sensor variables
TRIG = 23
ECHO = 24

#buzzer variables
BUZ = 17

#sensor and buzzer output settings

#channel output list
#chan_list = [17,TRIG]

#Set pin 17 and 23 as an output pin for buzzer
GPIO.setup(TRIG, GPIO.OUT)

#sensor input pin settings
#Set pin  24  as an input pin for sensor
GPIO.setup(ECHO,GPIO.IN)

#BUZZER OUTPUT SETTINGS
GPIO.setup(BUZ,GPIO.OUT)

#buzzer function definition

#create the function buzz and feed it the pitch and duration)
def buzz(pitch,duration):  

       #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
       period = 1.0/pitch    

       #calcuate the time for half of the wave
       delay = period/2     

       #the number of waves to produce is the duration times the frequency
       cycles = int(duration*pitch)   

       #start a loop from 0 to the variable cycles calculated above
       for i in range(cycles): 

           #set pin 17 to high  
           GPIO.output(BUZ, True)  

           #wait with pin 17 high
           sleep(delay)    

           #set pin 17 to low
           GPIO.output(BUZ, False)    

           #wait with pin 17 low
           sleep(delay)

       return
 

#start infinite loop
while True:

     #GPIO.cleanup()


     #sensor workings

     GPIO.output(TRIG, False)

     print("Waiting For Sensor To Settle")

     sleep(10)
     GPIO.output(TRIG, True)
     sleep(0.00001)
     GPIO.output(TRIG, False)
    
     while GPIO.input(ECHO)==0:
         pass
         pulse_start = time()
         #print("pulse_start {}".format(pulse_start))

     #sleep(5)

     while GPIO.input(ECHO)==1:
         pass
         pulse_end = time()
         #print("pulse_end {}".format(pulse_end))

     #calculating duration,Time = Width of Echo pulse, in uS (micro second)
     pulse_duration = pulse_end-pulse_start

     #calculating distance speed for 2d/2 is 17150 cm/sec for speed for sound 343m/s i.e 34300 cm/sec
     distance = pulse_duration*17150

     #rounding distance
     distance = round(distance,2)

     print("Distance: {} cm".format(distance))
   
     # range for ultrasonic sensor HCSR04 is max= 400cm ,min =  2cm  non-contact 
     if distance <= 200:

          #buzzer workings

          #convert pitch input to a floating decimal
          pitch = float(1000)

          #convert user input to a floating decimal( type in the duration) taken from sensor .................
          duration = float(distance)  

          #feed the pitch and duration to the function, buzz
          buzz(pitch,duration)  
          

#returning all channels you have used back to inputs it may be less usable here because while loop is running infinitely
GPIO.cleanup()

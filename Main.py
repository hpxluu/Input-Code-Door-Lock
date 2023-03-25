import Adafruit_BBIO.GPIO as GPIO   #import the Adafruit BBIO Library for controlling the GPIOs
import Adafruit_BBIO.PWM as PWM     #import the Adafruit BBIO Library for controlling the GPIOs with PWM properties
import time                         #import the time library


# Setting up the GPIO pin outs

GPIO.setup("P8_13", GPIO.IN, GPIO.PUD_DOWN) # pin outs for the buttons
GPIO.setup("P8_19", GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup("P9_16", GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup("P9_14", GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup("P9_15", GPIO.OUT) # pin outs for the red and green LEDs
GPIO.setup("P8_12", GPIO.OUT)

GPIO.setup("P8_8", GPIO.OUT) # pin outs for the 4 LEDs 
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_23", GPIO.OUT)
GPIO.setup("P9_27", GPIO.OUT)


# empty arrays used to store passcodes
code = [] 
codeCheck = []
code2 = [2,2,2,2]


# First program call to initialize and create a passcode

def firstPassword():
    code.append(int(input("Enter the first digit ")))
    code.append(int(input("Enter the second digit ")))
    code.append(int(input("Enter the third digit ")))
    code.append(int(input("Enter the fourth digit ")))
    

# Main function to check the user inputted password stored in a 
# temporary array (codeCheck) and compares it with the user stored password 
# in the code array. The method also has an option to reset the password when
# entering a certain combination of pin out numbers.

def passwordCheck(codeCheck):
    checks = 0
    checks2 = 0
    for i in range(len(codeCheck)):
        if (code[i]==codeCheck[i]):
            checks=checks+1
            
    for i in range(len(codeCheck)):
        if (code2[i]==codeCheck[i]):
            checks2=checks2+1
    
    if checks == len(code):
        GPIO.output("P9_15", GPIO.HIGH)
        print("Correct password")
    
    elif checks2 == len(code2):
        code.clear()
        code.append(int(input("Enter the first digit ")))
        code.append(int(input("Enter the second digit ")))
        code.append(int(input("Enter the third digit ")))
        code.append(int(input("Enter the fourth digit ")))
        
    else:
        GPIO.output("P8_12", GPIO.HIGH)
        print("Incorrect password")

# Main loop method for inputting the password

try:
    firstPassword()
    while True:
        if GPIO.input("P8_13") == 1:
            codeCheck.append(1)
            GPIO.output("P9_23", GPIO.HIGH)
            time.sleep(0.5) 
      
        if GPIO.input("P8_19") == 1:
            codeCheck.append(2)
            GPIO.output("P9_27", GPIO.HIGH)
            time.sleep(0.5) 
            
        if GPIO.input("P9_16") == 1:
            codeCheck.append(3)
            GPIO.output("P9_12", GPIO.HIGH)
            time.sleep(0.5) 
            
        if GPIO.input("P9_14") == 1:
            codeCheck.append(4)
            GPIO.output("P8_8", GPIO.HIGH)
            time.sleep(0.5) 
            
        if len(codeCheck) == len(code):
            passwordCheck(codeCheck)
            codeCheck.clear()
            time.sleep(0.5) 

            
        # After inputting the password and getting a response from
        # either the green or red LED, all the LEDs are set to low for the
        # next iteration.
        GPIO.output("P9_12", GPIO.LOW)
        GPIO.output("P9_15", GPIO.LOW)
        GPIO.output("P9_27", GPIO.LOW)
        GPIO.output("P9_23", GPIO.LOW)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.output("P8_8", GPIO.LOW)

except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
    GPIO.output("P9_12", GPIO.LOW)
    GPIO.output("P9_15", GPIO.LOW)
    GPIO.output("P9_27", GPIO.LOW)
    GPIO.output("P9_23", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.cleanup()                          #cleanup all used GPIO pins
    print ("Ending program")                #print end of program to terminal
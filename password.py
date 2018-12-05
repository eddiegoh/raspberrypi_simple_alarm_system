import time
import Lcd,Sensor1
import unarmedState
import MatrixKey_func

lcd = Lcd.Lcd()
sensor = Sensor1.Sensor(11)
Unarm = unarmedState.Unarmed()
start ='B'
temp =''
password_full =''
password_hidden ='' 
#password =''
tries = 1
cont = 'C'


class Password:
    def ___init__(self):
        # Received keypress A to arm the system
        # checking for the correct password to arm the system
        # Request for password display
        lcd = Lcd.Lcd()
        sensor = Sensor1.Sensor(11)
        Unarm = unarmedState.Unarmed()
        lcd.clear()
        
    def enterPW(self):    
        lcd.display_string("Enter your password:",1)
        lcd.display_string("Press # to confirm",4)

    # while loop to put password into a String
    # while ( start = 'A' and sensor.getState() == 0):
    def passwordString(self, singleChar):
        global password_full
        global password_hidden
        #global password
        if( singleChar != '#' ):
            password_hidden = password_hidden + '*'
            lcd.display_string(password_hidden, 2)
            password_full  = password_full + singleChar
            print(password_full)
        else:
            print('return:' + password_full)
            password = password_full
            password_full =''
            password_hidden =''
            #return password_full
            return password
        

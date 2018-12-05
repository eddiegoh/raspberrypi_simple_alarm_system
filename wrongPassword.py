import time
import Lcd,Sensor1
import unarmedState
import MatrixKey_func
import password


lcd = Lcd.Lcd()
lcd.clear()
sensor = Sensor1.Sensor(11)
Unarm = unarmedState.Unarmed()
pw = password.Password()
start ='B'
temp =''
password_full =''
password_hidden =''
password =''
cont = 'C'



class wrongPW:
    def ___init__(self):
        # Received keypress A to arm the system
        # checking for the correct password to arm the system
        # Request for password display
        lcd = Lcd.Lcd()
        sensor = Sensor1.Sensor(11)
        Unarm = unarmedState.Unarmed()
        lcd.clear()
    def wrongPassword(self, tries):
        # Receive incorrect password 
        
        print 'WRONG PASSWORD'
        lcd.clear()
        lcd.display_string("   WRONG PASSWORD   ",1)
        lcd.display_string("Tries:%d" %tries , 2)
        lcd.display_string("Press C to try again",3)

    def pressWrong(self, keypress):
        #cont = str(MatrixKey_func.matrix_input())
        if ( keypress != 'C' ):
            lcd.display_string("Wrong Button Pressed",4)
            time.sleep(1)
            lcd.display_string("                    ",4)
        else:
            lcd.clear()
   
        

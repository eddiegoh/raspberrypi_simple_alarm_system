import time

import Lcd,Sensor1

import MatrixKey_func


lcd = Lcd.Lcd()
sensor = Sensor1.Sensor(11)

class Armed:
    def ___init__(self):
        lcd = Lcd.Lcd()
        lcd.clear()
        sensor = Sensor1.Sensor(11)
    def armState(self):

        lcd.clear()
        lcd.display_string("    Alarm System    ",1) 
        lcd.display_string("     Activated!     ",2)
        #lcd.display_string("  Press D to DISARM ",3)
        # from here onward start checking for break in
        # to go into deactivate state 

    def correctState(self, keypress):
        #self.keypress = temp
        # When user press A to arm the system
        # Check for the correct condition to arm the alarm system
        '''
        if (keypress!='A' or sensor.getState() != 0):
            if (keypress!='A' and sensor.getState() != 0):
                lcd.display_string("Wrong Button Pressed",4) 
                time.sleep(1.5)
                lcd.display_string("And Door Not Closed!",4)
                time.sleep(1.5)
                lcd.display_string("Wrong Button Pressed",4) 
                time.sleep(1.5)
                lcd.display_string("And Door Not Closed!",4)
                time.sleep(1.5)
                lcd.clear()
                return False
        '''
        if (keypress!='D' and sensor.getState() == 0):
            lcd.display_string("Wrong Button Pressed",4) 
            time.sleep(1)
            lcd.display_string("                    ",4) 
            return False
            '''
            if (keypress == 'A' and sensor.getState() != 0):
                lcd.display_string("  Door not closed!  ",4) 
                time.sleep(3)
                lcd.clear()
                return False
             '''   
        elif (keypress == 'D' and sensor.getState() == 0):
            return True 
        

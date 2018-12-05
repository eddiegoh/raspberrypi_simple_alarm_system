import time
import Lcd,Sensor1
import MatrixKey_func


lcd = Lcd.Lcd()
sensor = Sensor1.Sensor(11)

class Broken:
    def ___init__(self):
        lcd = Lcd.Lcd()
        lcd.clear()
        sensor = Sensor1.Sensor(11)
    def brokeState(self):

        lcd.clear()
        lcd.display_string("UNAUTHORIZED ACCESS!",1)
        lcd.display_string(" CLOSE THE DOOR AND ",2)
        lcd.display_string("  Press D to DISARM ",3)
        # to go into deactivate state 

    def correctState(self, keypress):
        #self.keypress = temp
        # When user press A to arm the system
        # Check for the correct condition to arm the alarm system
        
        if (keypress!='D' or sensor.getState() != 0):
            if (keypress!='D' and sensor.getState() != 0):
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
            
            if (keypress!='D' and sensor.getState() == 0):
                lcd.display_string("Wrong Button Pressed",4) 
                time.sleep(3)
                lcd.clear()
                return False
            
            if (keypress == 'D' and sensor.getState() != 0):
                lcd.display_string("  Door not closed!  ",4) 
                time.sleep(3)
                lcd.clear()
                return False
       
        elif (keypress == 'D' and sensor.getState() == 0):
            return True 
        

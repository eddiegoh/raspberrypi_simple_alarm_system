import time
import Lcd,Sensor1
import unarmedState
import armedState
import brokenState
import MatrixKey_func
import password
import wrongPassword
import alertEmail
import camera

wrongPW = wrongPassword.wrongPW()
Armed = armedState.Armed()
broken = brokenState.Broken()
lcd = Lcd.Lcd()
sensor = Sensor1.Sensor(11)
Unarm = unarmedState.Unarmed()
pw = password.Password()
alert = alertEmail.emailAlert()
camerashot = camera.Camera()


temp =''
password_full =''
password_hidden =''
password =''
tries = 1
Alarm=0 # indicate alarm in active or inactive state
breakoff = False
  
while(True):
    while (Alarm == 0): # alarm inactive
        Unarm.unarmState()
        temp=str(MatrixKey_func.matrix_input())
        if (Unarm.correctState(temp) == True):
            lcd.clear()
            break

    
    while (Alarm == 0):
        pw.enterPW()
        temp=str(MatrixKey_func.matrix_input())
        password_full = pw.passwordString(temp)
        if( password_full == '123456'): # if correct password
            Alarm = 1
            lcd.clear()
            tries = 1 
            break
        elif(password_full != '123456' and temp=='#'): #wrong password
            wrongPW.wrongPassword(tries)  
            tries = tries + 1
            while(temp != 'C'):
                temp=str(MatrixKey_func.matrix_input())
                wrongPW.pressWrong(temp)
                                   

    
    Armed.armState()
    while ( Alarm == 1):
         if( sensor.getState() == 1 ):
             break   


    while (Alarm == 1 and sensor.getState() == 1): #In broken state
        broken.brokeState()
        camerashot.takevideo()
        #time.sleep(1)
        alert.sendVideo()
        print("send picture")
        
        while(True):
            print("waiting for input to disarm")
            broken.brokeState()
            temp=str(MatrixKey_func.matrix_input())
            if (broken.correctState(temp) == True): # if accidentally triggered alarm
                lcd.clear()
                break
        break

        
    while (Alarm == 1 and sensor.getState() != 1):
        pw.enterPW()
        temp=str(MatrixKey_func.matrix_input())
        password_full = pw.passwordString(temp)
        if( password_full == '123456'): # if correct password
            Alarm = 0
            lcd.clear()
            tries = 1 
            break
        elif(password_full != '123456' and temp=='#'): #wrong password
            wrongPW.wrongPassword(tries)  
            tries = tries + 1
            while(temp != 'C'):
                temp=str(MatrixKey_func.matrix_input())
                wrongPW.pressWrong(temp)
        
    



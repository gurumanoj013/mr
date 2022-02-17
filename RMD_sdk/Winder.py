from RMD_main_Func import *
import math
import time

motor3 = RMD('can1',1000000,3)
motor2 = RMD('can1',1000000,2)
motor1 = RMD('can1',1000000,1)

motor1.Position_Ctrl_1(0)
motor1.Send_Receive_Message()
motor1.decode_mesgrecv()
motor2.Position_Ctrl_1(0)
motor2.Send_Receive_Message()
motor2.decode_mesgrecv()
motor3.Position_Ctrl_1(0)
motor3.Send_Receive_Message()
motor3.decode_mesgrecv()

motor1.Motor_OFF()
motor1.Send_Receive_Message()
motor1.decode_mesgrecv()
motor2.Motor_OFF()
motor2.Send_Receive_Message()
motor2.decode_mesgrecv()
motor3.Motor_OFF()
motor3.Send_Receive_Message()
motor3.decode_mesgrecv()



print('Enter the length')
length = input(int)
length = int(length)
print('Enter the bent angle')
angle = input(int)
angle = int(angle)
print('Enter the length of the total winding')
Cutting_Length = input ()

Arc_Angle = int((length/(2*3.141592653589793*25))*360)
Total_Angle = 0

while True:
    try:
        Arc_Angle = 60+Total_Angle
        motor1.Position_Ctrl_2(60,Arc_Angle)
        motor1.Send_Receive_Message()
        motor1.decode_mesgrecv()
        while True:
            motor1.RD_Multi_turn_Angle()
            motor1.Send_Receive_Message()
            motor1.decode_mesgrecv()
            print(int(RMD_Dcl.MULTI_TURN_ANG_OUT))
            print(Total_Angle)
            if int(RMD_Dcl.MULTI_TURN_ANG_OUT) == int(Arc_Angle):
                print('Equal')
                Total_Angle = int(RMD_Dcl.MULTI_TURN_ANG_OUT)
                break
        
        motor2.Position_Ctrl_2(90,90)
        motor2.Send_Receive_Message()
        motor2.decode_mesgrecv()
        while True:
            motor2.RD_Multi_turn_Angle()
            motor2.Send_Receive_Message()
            motor2.decode_mesgrecv()
            if int(RMD_Dcl.MULTI_TURN_ANG_OUT) == 90:
                motor2.Position_Ctrl_2(90,0)
                motor2.Send_Receive_Message()
                motor2.decode_mesgrecv()
                while True:
                    motor2.RD_Multi_turn_Angle()
                    motor2.Send_Receive_Message()
                    motor2.decode_mesgrecv()
                    if int(RMD_Dcl.MULTI_TURN_ANG_OUT) == 0:
                        break
                break

    except KeyboardInterrupt:
        motor1.Speed_Ctrl_Mode(0)
        motor1.Send_Receive_Message()
        motor2.Speed_Ctrl_Mode(0)
        motor2.Send_Receive_Message()
        motor3.Speed_Ctrl_Mode(0)
        motor3.Send_Receive_Message()
        break        

    
from RMD_main_Func import *
import time

motor3 = RMD('can1',1000000,3)
motor2 = RMD('can1',1000000,2)




# while True:
#     motor2.RD_Multi_turn_Angle()
#     motor2.Send_Receive_Message()
#     motor2.decode_mesgrecv()
#     print('Motor2',RMD_Dcl.MULTI_TURN_ANG_OUT)
#     motor3.Position_Ctrl_1(RMD_Dcl.MULTI_TURN_ANG_OUT)
#     motor3.Send_Receive_Message()
#     motor3.decode_mesgrecv()
#     # time.sleep(0.1)
#     motor3.RD_Multi_turn_Angle
#     motor3.Send_Receive_Message()
#     motor3.decode_mesgrecv()
#     print('Motor3',RMD_Dcl.MULTI_TURN_ANG_OUT)
#     motor2.Position_Ctrl_1(RMD_Dcl.MULTI_TURN_ANG_OUT)
#     motor2.Send_Receive_Message()
#     motor2.decode_mesgrecv()
#     # time.sleep(0.1)



while True:
    print('Loop Started')
    motor2.RD_Multi_turn_Angle()
    motor2.Send_Receive_Message()
    motor2.decode_mesgrecv()
    motor2_Multi = int(RMD_Dcl.MULTI_TURN_ANG_OUT/8)
    print('Motor 2 is ',motor2_Multi)
    motor3.RD_Multi_turn_Angle()
    motor3.Send_Receive_Message()
    motor3.decode_mesgrecv()
    motor3_Multi = int(RMD_Dcl.MULTI_TURN_ANG_OUT/8)
    print('Motor 3 is ',motor3_Multi)
    if motor2_Multi > motor3_Multi:
        motor3.Speed_Ctrl_Mode(0.3)
        motor3.Send_Receive_Message()
        motor2.Speed_Ctrl_Mode(-0.3)
        motor2.Send_Receive_Message()
    elif motor2_Multi < motor3_Multi:
        motor3.Speed_Ctrl_Mode(-0.3)
        motor3.Send_Receive_Message()
        motor2.Speed_Ctrl_Mode(0.3)
        motor2.Send_Receive_Message()
    elif motor2_Multi == motor3_Multi:
        motor2.Speed_Ctrl_Mode(0)
        motor2.Send_Receive_Message()
        motor3.Speed_Ctrl_Mode(0)
        motor3.Send_Receive_Message





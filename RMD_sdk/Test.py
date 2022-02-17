
# import struct
from RMD_main_Func import *
import time
# motor3 = RMD('can1',1000000,3)
# motor2 = RMD('can1',1000000,2)
# motor1 = RMD('can1',1000000,1)

# motor1.Speed_Ctrl_Mode(0.2)
# motor1.Send_Receive_Message()
# motor1.decode_mesgrecv()

# motor2.Speed_Ctrl_Mode(0.2)
# motor2.Send_Receive_Message()
# motor2.decode_mesgrecv()

# motor3.Speed_Ctrl_Mode(0.2)
# motor3.Send_Receive_Message()
# motor3.decode_mesgrecv()

# A = '00 00 00 00 00 00 02 8D'
# A = 'FF FF FF FF FF FF 02 8D'
# b = struct.unpack('>q', bytearray.fromhex(A))
# b = int(b[0])
# print(b)



# def signed_int(h):
#     x = int(h, 16)
#     print(x)
#     if x > 0x7FFFFFFFFFFFFF:
#         a = 'FF'
#         print(a)
#         x = f'{a}{h}'
#         print(x)
#         x = struct.unpack('>q', bytearray.fromhex(x))
#         x = int(x[0])
#     return x
# print(signed_int('ffffffffff45cb'))



motor1 = RMD('can1',1000000,1)
motor2 = RMD('can1',1000000,2)
motor3 = RMD('can1',1000000,3)
# motor4 = RMD('can1',1000000,4)

# motor2.Speed_Ctrl_Mode(-0.001)
# motor2.Send_Receive_Message()
# motor2.decode_mesgrecv()

while True:
    motor2.RD_Multi_turn_Angle()
    motor2.Send_Receive_Message()
    motor2.decode_mesgrecv()
#     motor1.RD_PID_Data()
#     # motor1.WR_PID_RAM(100,100,100,100,100,100)
#     # motor1.WR_PID_ROM(100,100,50,40,50,50)
#     # motor1.RD_Acceleration_Data()
#     # motor1.WR_Acceleration_Data(0)
#     # motor1.RD_Encoder_Data()
#     # motor1.WR_Encoder_Offset(0)
#     # motor1.WR_Current_Position_AS_Offset_ROM()
#     # motor1.RD_Multi_turn_Angle()
#     # motor1.RD_Single_Circle_Angle()
#     # motor1.RD_Error_Flag()
#     # motor1.Clr_Error_flags()
#     # motor1.RD_Motor_Status_2()
#     # motor1.RD_Motor_Status_3()
#     # motor1.Motor_OFF()
#     # motor1.Motor_Stop()
#     # motor1.Motor_Start()
#     # motor1.Torque_Ctrl_Mode(0)
#     # motor1.Speed_Ctrl_Mode(0)   #(Direction 0 or 1, Speed in rev/sec in float)
#     # motor1.Position_Ctrl_1(360)
#     # motor1.Position_Ctrl_2(10,0)
#     # motor1.Position_Ctrl_3(0,359)
#     # motor1.Position_Ctrl_4(1,30,0)
#     # motor1.Position_Ctrl_5(180)
#     # motor1.Position_Ctrl_6(60,180)
#     motor1.Send_Receive_Message()
#     motor1.decode_mesgrecv()
    time.sleep(0.2)




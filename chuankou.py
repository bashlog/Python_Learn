import serial #导入模块

import serial.tools.list_ports
port_list = list(serial.tools.list_ports.comports())
print(port_list)
if len(port_list) == 0:
   print('No ports available')
else:
    for i in range(0,len(port_list)):
        print(port_list[i])
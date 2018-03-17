from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from time import sleep
client = ModbusClient(host = '172.21.217.6', port = 502)
i = 0

while True:
# Holding Registers
	client.connect()
	result1 = client.read_holding_registers(0,1)
	i = i+1
	client.close()
	print(result1.registers)
	#sleep(1)

client.connect()
res = client.write_registers(0,[2,1,0])
client.close()
print(res)

# Coils
sleep(1)
client.connect()
result2 = client.read_coils(0,3)
client.close()
print(result2.bits)
sleep(1)
client.connect()
res = client.write_coils(0,[False,True,False])
client.close()
print(res)

# Input registers
sleep(1)
client.connect()
result3 = client.read_input_registers(0,3)
client.close()
print(result3.registers)

# Discrete inputs
sleep(1)
client.connect()
result4 = client.read_discrete_inputs(0,3)
client.close()
print(result4.bits)









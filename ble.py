import bluetooth
 
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print "Accepted connection from ",address
while 1:
 
 data = client_socket.recv(1024)
 print "Received: %s" % data
 client_socket.send(data)
 if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 LOW, LED OFF")
 if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 HIGH, LED ON")
 if (data == "q"):
  print ("Quit")
  break
 
client_socket.close()
server_socket.close()

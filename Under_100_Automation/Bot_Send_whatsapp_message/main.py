import pywhatkit

mobile = input('Enter Mobile No of Receiver : ')
message = input('Enter Message you wanna send : ')
print("Now you need to insert what time you want the message to be sent")
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(mobile,message,hour,minute)

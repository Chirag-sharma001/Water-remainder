import time
# import winsound
# from plyer import notification
# uncomment this when you are using this program in windows 
from win10toast import ToastNotifier
import datetime

frequency=390
duration=1500

def getTimeInput():
	hour = int(input("Enter hours of interval :"))
	minutes = int(input("Enter Mins of interval :"))
	seconds = int(input("Enter Secs of interval :"))
	time_interval = seconds+(minutes*60)+(hour*3600)
	return time_interval


def log():
	now = datetime.datetime.now()
	start_time = now.strftime("%H:%M:%S")
	with open("log.txt", 'a') as f:
		f.write(f"You drank water {now} \n")
	return 0


def notify():
	# this is lines of code  for windows 
	# winsound.Beep(frequency,duration)
	notification = ToastNotifier()
	notification.show_toast("Time to drink water")
# 	notification.notify(
# 			title = "Remainder please drink water",
# 			message=" Have you drank water " ,
		
# 			# displaying time
# 			timeout=2
# )
# 		# waiting time
# 	time.sleep(7)

	log()
	return 0


def starttime(time_interval):
	while True:
		time.sleep(time_interval)
		notify()


if __name__ == '__main__':
	time_interval = getTimeInput()
	starttime(time_interval)


	

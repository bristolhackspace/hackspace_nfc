import nxppy
import time
import sys
import signal


def signal_term_handler(signum = None, frame = None):
	sys.stderr.write("Terminated.\n")
	f.close()
	sys.exit(0)

for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]: 
	signal.signal(sig, signal_term_handler)

mifare = nxppy.Mifare()
uid = None

f = open("user_list.csv",'r')

user_hash = {}

for line in f:
	user_hash[line.split(',')[0]] = line.split(',')[1].strip()

# Select the first available tag and return the UID
while True:
	try:
		uid = mifare.select()
	except nxppy.SelectError:
		pass
	if uid is not None:
		print "Card detected:", uid
		if uid in user_hash.keys():
			print "hello ", user_hash[uid] 
		uid = None #reset uid to None
		time.sleep(2) #pause for 2 seconds



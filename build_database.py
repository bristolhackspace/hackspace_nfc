import nxppy
import time

mifare = nxppy.Mifare()
uid = None
# Select the first available tag and return the UID
while True:
	try:
		uid = mifare.select()
	except nxppy.SelectError:
		pass
	if uid is not None:
		print "Card detected:", uid
		username = raw_input("Please enter member name: ")
		print username, "ID:", uid
		uid = None #reset uid to None
		time.sleep(2) #pause for 2 seconds


#print blockbytes

# Read 16 bytes starting from block 10 
# (each block is 4 bytes, so technically this reads blocks 10-13)
#block10bytes = mifare.read_block(10)

# Write a single block of 4 bytes
#mifare.write_block(10, b'abcd')

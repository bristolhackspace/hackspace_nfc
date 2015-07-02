import nxppy

mifare = nxppy.Mifare()
uid = None
# Select the first available tag and return the UID
while True:
	try:
		uid = mifare.select()
		#mifare.write_block(10,b'abcd')
		#blockbytes = mifare.read_block(10)
	except nxppy.SelectError:
		pass
	if uid is not None:
		break
print uid
for i in range(64):
	blockbytes = mifare.read_block(i)
	print i, blockbytes, len(blockbytes)

#print blockbytes

# Read 16 bytes starting from block 10 
# (each block is 4 bytes, so technically this reads blocks 10-13)
#block10bytes = mifare.read_block(10)

# Write a single block of 4 bytes
#mifare.write_block(10, b'abcd')

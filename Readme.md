# hackspace-nfc
Software for Bristol Hackspace NFC system.

This is designed to run on a Raspberry Pi with the NXP Explore-NFC card reader attached.

Requirements:
* python
* nxppy python library (https://github.com/svvitale/nxppy)

Currently contains 2 scripts:

	1. build_database.py
		* this script builds a table with 2 columns: card ID, user name and writes to user_list.csv
	2. nfc_logbook.py
		* this script reads user_list.csv and prints a greeting when a particular user's card is scanned.
		* To do: write a text log with date and time when card was scanned.

## Wish list

* script to record equipment borrowing
* script to record equipment usage time (laser cutter/3D printer/etc)
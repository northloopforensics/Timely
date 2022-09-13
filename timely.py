#   A script to convert timestamps on Mac

import time
import datetime
import argparse

#   Test timestamps
# input_timestamp = 590517794000000000      #   coredata nano   2019-09-18 12:43:14
# input_timestamp = 590517794                 #   coredata   2019-09-18 12:43:14
# input_timestamp = 1662521895
# input_timestamp = 1662521895000000000        #   APFS timestamp
# input_timestamp = 6318253A                 #  in hex


###############     Argument Parser     #################

_author_ = ['Copyright 2022 North Loop Consulting']
_copy_ = ['(C) 2022']
_description_ = ("TIMELY.PY is just another timestamp conversion tool. \n\n\n"
                 " To run the script, enter 'python3 timely.py <timestamp>'.  For example, 'python3 timely.py 68475131' for decimal or 'python3 timely.py 14e864cb8520e8a4 -x' for hex"
                 )

parser = argparse.ArgumentParser(
    description=_description_,
    epilog="{}".format(
        ", ".join(_author_), _copy_))


#Add positional arguments
parser.add_argument("timestamp", type=(str) ,help="Timestamp to convert")

# Optional Arguments

parser.add_argument("-x", "--hex", action="store_true",help="convert from hex value" )

#Parsing and using the arguments

args = parser.parse_args()

input_timestamp = args.timestamp
# input_timestamp = int(input_timestamp)
length = len(str(input_timestamp))


def convertHex(timestamp):
    hex_characters = ['a', 'b', 'c', 'd', 'e', 'f']

    if isinstance(timestamp, int) == False:         # checks if is integer
        try:
            int_timestamp = int(timestamp, 16)
            # print(int_timestamp)
            global new_input_timestamp
            new_input_timestamp = int_timestamp
            return(new_input_timestamp)
        except:
            print("This is not an accepted format. Please use a decimal or hex value.")
    for ele in hex_characters:
        if ele in input_timestamp == True:
            try:
                int_timestamp = int(timestamp, 16)
                # print(int_timestamp)
                
                new_input_timestamp = int_timestamp
                return(new_input_timestamp)
            except:
                print("This is not an accepted format. Please use a decimal or hex value.")

    else:
        pass

def fromUnix(timestamp):
    try:
        timestamp = int(timestamp)
        if length <= 11:
            unix = datetime.datetime.strptime(time.ctime(timestamp),"%a %b %d %H:%M:%S %Y")
            unix.strftime('%m/%d/%Y %H:%M:%S')
            unix = str(unix)
            print("Unix Time:  \t\t\t" + unix + " Local Time")
            unixUTC = str(datetime.datetime.utcfromtimestamp(timestamp))
            print("Unix Time:  \t\t\t" + unixUTC + " UTC")
        else:
            pass
    except TypeError:
        print("Type error - integer required")

def fromCocoa(timestamp):
    if length < 11:
        cocoa = int(timestamp) + 978307200
        convCocoa = datetime.datetime.strptime(time.ctime(cocoa),"%a %b %d %H:%M:%S %Y")
        convCocoa.strftime('%m-%d-%Y %H:%M:%S')
        convCocoa = str(convCocoa)
        print("Mac Cocoa/Core Time (Sec): \t" + convCocoa + " Local Time")
        cocoaUTC = str(datetime.datetime.utcfromtimestamp(cocoa))
        print("Mac Cocoa/Core Time (Sec): \t" + cocoaUTC + " UTC")
    else:
        pass

def fromCocoaNano(timestamp):
    if length > 11:
        cocoa = int(timestamp) + 978307200000000000
        cocoa = cocoa / 1000000000
        convCocoa = datetime.datetime.strptime(time.ctime(cocoa),"%a %b %d %H:%M:%S %Y")
        convCocoa.strftime('%m-%d-%Y %H:%M:%S')
        convCocoa = str(convCocoa)
        print("Mac Cocoa/Core Time (Nano): \t" + convCocoa)
    else:
        pass

def APFS(timestamp):        #   not working
    timestamp = int(timestamp)
    t = (datetime.datetime(1970,1,1) + datetime.timedelta(microseconds=timestamp / 1000. ))
    new_t = t.strftime('%Y-%m-%d %H:%M:%S')
    print("Mac APFS Time: \t\t\t" +str(new_t))

if args.hex:                        # is the hex flag set in command? then this converts to integer
    convertHex(input_timestamp)
    input_timestamp = new_input_timestamp
print(" ")
fromUnix(input_timestamp)
fromCocoa(input_timestamp)
fromCocoaNano(input_timestamp)
APFS(input_timestamp)
print(" ")



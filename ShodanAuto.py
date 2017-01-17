# time complexity = O(N^2 * m)
# N = Loop through IP values
# m = Loop through ports to print

import sys
import shodan
import time

SHODAN_API_KEY = ''
api = shodan.Shodan (SHODAN_API_KEY)

subnet    = '127.0.'
thirdSub  = '0'
fourthSub = '0'
subnetArr = []

# Open subnet file and add to array
INPUT = sys.argv[1]
with open (INPUT) as file:
    inputList = file.read().splitlines()

for row in inputList:
    entry = row.split(" ")
    subnetArr.append (entry)

# Open/Create the output file
OUTPUT = sys.argv[2]
outfile = open (OUTPUT, 'w')
outfile.truncate ()

# loop through and grab subsequent hosts in the subnet
c1 = 0
x = subnetArr[c1][0]
y = subnetArr[c1][1]
i = int(x)

while(i >= int(x) and i < int(y) + 1):
    for j in range (0, 256):
        thirdSub  = i
        fourthSub = j
        IP = subnet + str(thirdSub) + '.' + str(fourthSub)

        print ("Scanning IP: " + IP)

        try:
            host = api.host (IP)
            print ("\tMATCH FOUND")
            #time.sleep(2)

            # add the returned data to a file
            outfile.write ( "\nIP: %s\nOrganization: %s\nOperating System: %s\n" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

            for item in host['data']:
                outfile.write ("Port: %s\nBanner: %s\n" % (item['port'], item['data']))
        except:
            pass

    try:
        if (i == (int(y) - 1)):
            # update the range

            c1 += 1
            x = subnetArr[c1][0]
            y = subnetArr[c1][1]

            i += int(x) - (int(subnetArr[c1 - 1][1]) - 1)
    except:
        pass

    i += 1

# close file when finished
outfile.close ()

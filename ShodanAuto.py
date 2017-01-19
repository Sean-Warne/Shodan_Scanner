import sys
import shodan
import time

SHODAN_API_KEY = ''
api = shodan.Shodan (SHODAN_API_KEY)

subnet    = '127.0.'
thirdSub  = '0'
fourthSub = '0'
subnetArr = []

INPUT    = sys.argv[1]
OUTPUT   = sys.argv[2]

# Open subnet file and add to array
with open (INPUT) as file:
    inputList = file.read().splitlines()

for row in inputList:
    entry = row.split(" ")
    subnetArr.append (entry)

# Open/Create the output file
outfile = open (OUTPUT, 'w')
outfile.truncate ()

# loop through and grab subsequent hosts in the subnet
c1 = 0
x = subnetArr[c1][0]
y = subnetArr[c1][1]
i = int(x)

# CSV header
outfile.write ("IP,Hostname,Operating System,Ports\n")

while(i >= int(x) and i < int(y) + 1):
    for j in range (0, 256):
        thirdSub  = i
        fourthSub = j
        IP = subnet + str(thirdSub) + '.' + str(fourthSub)
        outString = ""

        print ("Scanning IP: " + IP)

        try:
            host = api.host (IP)
            print ("\tMATCH FOUND")

            # add the returned data to a file
            outfile.write ("%s,%s,%s,\"" % (host['ip_str'], host['hostnames'], host.get('os', 'n/a')))

            temp = []
            for item in host['data']:
                temp.append (str(item['port']))

            portString = ', '.join (temp)
            outfile.write ("%s\"\n" % (portString))
        except:
            pass

    try:
        # update the subnet range
        if (i == (int(y) - 1)):
            c1 += 1
            x = subnetArr[c1][0]
            y = subnetArr[c1][1]

            i += int(x) - (int(subnetArr[c1 - 1][1]) - 1)
    except:
        pass

    i += 1

# close file when finished
outfile.close ()

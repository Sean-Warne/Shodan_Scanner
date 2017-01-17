Author: Warne, Sean
Date: 12/12/2016

Description: This script uses the Shodan API to scan over multiple IPs/Subnets using 
		a text file that is populated with subnet ranges (x1 y1 where x1 is 
		the start value and y1 is the end value).

Execute: 
On Linux: # sudo easy_install shodan
	  # python ShodanAuto.py <input file> <output file> -> python ShodanAuto.py subnets.txt output.txt

On Windows: > pip install shodan
	    > python ShodanAuto.py <input file> <output file> -> python ShodanAuto.py subnets.txt output.txt

Note: A shodan API key is needed from https://www.shodan.io/ to properly execute the scan.
	The script may be modified with your own personal key.

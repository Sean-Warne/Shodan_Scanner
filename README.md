Author: Warne, Sean  
Date: 12/12/2016

Description: 
This script uses the Shodan API to scan over multiple IPs/Subnets using a text file that is populated with subnet ranges (x1 y1...xn yn where x is the beginning range and y is the end range). It will scan through all IPs in the subnet ranges (0..255). The results are output in CSV format as "IP,Hostname,Operating System,Ports".

Execute: 
On Linux: 
# sudo easy_install shodan  
# python ShodanAuto.py <input file> <output file> -> python ShodanAuto.py subnets.txt output.txt  

On Windows: 
# pip install shodan  
# python ShodanAuto.py <input file> <output file> -> python ShodanAuto.py subnets.txt output.txt  

Note: A shodan API key is needed from https://www.shodan.io/ to properly execute the scan.
	The script may be modified with your own personal key.

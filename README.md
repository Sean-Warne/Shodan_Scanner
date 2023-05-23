# Shodan.io IoT Network Scanner #

## Summary and Purpose ##

This script uses the Shodan API to scan over multiple IPs/Subnets using a text file that is populated with subnet ranges (x1 y1...xn yn where x is the beginning range and y is the end range). It will scan through all IPs in the subnet ranges (0..255). The results are output in CSV format as "IP,Hostname,Operating System,Ports".

## Usage ##

Before using, you must create an account at shodan.io and generate an API key.

``` bash
python -m pip install -r requirements.txt
python ShodanAuto.py subnets.txt results.json
```

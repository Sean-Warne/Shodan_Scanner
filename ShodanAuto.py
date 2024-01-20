import argparse
import ipaddress

import shodan


def run_shodan_scan(api_key, ip_address, output):
    api = shodan.Shodan (api_key)

    # parse the IP(s)
    ips = ipaddress.ip_network(ip_address, strict=True).hosts()

    # Open/Create the output file
    outfile = open (output, 'w')
    outfile.truncate ()

    # CSV header
    outfile.write ("IP,Hostname,Operating System,Ports\n")

    for ip in ips:
        ip = str(ip)
        
        print ("Scanning IP: " + ip)

        try:
            host = api.host (ip)
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

    # close file when finished
    outfile.close ()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('api_key', help='Shodan.io API key generated under account settings')
    parser.add_argument('ip_address', help='IP Address to scan with or without a subnet mask')
    parser.add_argument('output', default=None, help='Path and filename of output file')

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit

    return args


def main(
        api_key,
        ip_address,
        output
):
    run_shodan_scan(api_key, ip_address, output)


if __name__ == "__main__":
    args = parse_args()
    main(
        args.api_key,
        args.ip_address,
        args.output
    )

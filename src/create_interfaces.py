'''
Created on May 24, 2013

@author: elingyu
'''

import optparse

def parse_args():
    usage = """usage: %prog [options]
this is the Ubuntu interfaces file generator.
Run it like this:

    python create_interfaces.py -d eth1 -n 10.200.1 -s 1 -e 20 -x 1 -m 255.255.0.0
    
it means it  will generate network configurations for Ubuntu OS, like:

auto eth1:1
iface eth1:1 inet static
address 10.200.1.1
netmask 255.255.0.0
broadcast 10.200.1.255
.
.
.
auto eth1:20
iface eth1:20 inet static
address 10.200.1.20
netmask 255.255.0.0
broadcast 10.200.1.255

"""

    parser = optparse.OptionParser(usage)
    parser.add_option("-d", "--device", dest="device", help="please input device", default="eth1")
    parser.add_option("-n", "--netaddress", dest="netaddress", help="please input netaddress", default="10.200.1")
    parser.add_option("-s", "--startaddress", dest="startaddress", type="int", help="please input startaddress", default=1)
    parser.add_option("-e", "--stopaddress", dest="stopaddress", type="int", help="please input stopaddress", default=20)
    parser.add_option("-x", "--startindex", dest="startindex", type="int", help="please input startindex", default=1)
    parser.add_option("-m", "--networkmask", dest="networkmask", help="please input networkmask", default="255.255.0.0")
    options, _ = parser.parse_args()
    
    return options.device, options.netaddress, options.startaddress, options.stopaddress, options.startindex, options.networkmask


def create_interfaces():
    dev, netadd, startadd, stopadd, startindx, netmask = parse_args()
    conf = ''
    for i in range(startadd, stopadd + 1):
        conf = conf + 'auto ' + dev + ':' + str(startindx) + '\n'
        conf = conf + 'iface ' + dev + ':' + str(startindx) + ' inet static\n' 
        conf = conf + 'address ' + netadd + '.' + str(i) + '\n'
        conf = conf + 'netmask ' + netmask + '\n'
        conf = conf + 'broadcast ' + netadd + '.255\n'
        conf = conf + '\n'
        startindx = startindx +1
        
    print conf
    
if __name__ == '__main__':
    create_interfaces()
    
    
    
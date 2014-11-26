'''
Created on May 24, 2013

@author: elingyu
'''

import optparse

def parse_args():
    usage = """usage: %prog [options]
this is the Ubuntu interfaces file generator.
Run it like this:

    python create_interfaces.py -d eth1 -n 10.29 -t 101 -p 124 -s 1 -e 254 -x 1 -m 255.255.0.0 -o "C:\simon\workspace\create_interfaces\src" -f "int.txt"
    
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
    parser.add_option("-n", "--netaddress", dest="netaddress", help="please input netaddress", default="10.200")
    parser.add_option("-t", "--startaddress_1", dest="startaddress_1", type="int", help="please input startaddress_1", default=1)
    parser.add_option("-p", "--stopaddress_1", dest="stopaddress_1", type="int", help="please input stopaddress_1", default=20)
    parser.add_option("-s", "--startaddress_2", dest="startaddress_2", type="int", help="please input startaddress_2", default=1)
    parser.add_option("-e", "--stopaddress_2", dest="stopaddress_2", type="int", help="please input stopaddress_2", default=20)
    parser.add_option("-x", "--startindex", dest="startindex", type="int", help="please input startindex", default=1)
    parser.add_option("-m", "--networkmask", dest="networkmask", help="please input networkmask", default="255.255.0.0")
    parser.add_option("-o", "--directory", dest="directory", type="string", help="please input the file's directory", default="c:")
    parser.add_option("-f", "--file", dest="file", type="string", help="please input the file's name", default="int.txt")
    options, _ = parser.parse_args()
    
    return options.device, options.netaddress, options.startaddress_1, options.stopaddress_1, options.startaddress_2, options.stopaddress_2, options.startindex, options.networkmask, options.directory, options.file

def create_interfaces():
    dev, netadd, startadd_1, stopadd_1, startadd_2, stopadd_2, startindx, netmask, directory, file_name = parse_args()
    int_file = open(directory + "//" + file_name, 'a')

    for j in range(startadd_1, stopadd_1 + 1):
        for i in range(startadd_2, stopadd_2 + 1):
            conf = ''
            conf = conf + 'auto ' + dev + ':' + str(startindx) + '\n'
            conf = conf + 'iface ' + dev + ':' + str(startindx) + ' inet static\n' 
            conf = conf + 'address ' + netadd + '.' + str(j)
            conf = conf + '.' + str(i) + '\n'
            conf = conf + 'netmask ' + netmask + '\n'
            conf = conf + 'broadcast ' + netadd + '.' + str(j)
            conf = conf + '.255\n'
            conf = conf + '\n'
            startindx = startindx + 1
            print conf
            int_file.writelines(conf)
    int_file.close()
    
if __name__ == '__main__':
    create_interfaces()
    
    
    

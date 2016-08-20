import random
import sys

def subnet_calc():
    try:
        #check IP address validity
        while True:
            ip_addr = raw_input('\nEnter IP address: ')
        
            a = ip_addr.split('.')
            #print a
            
            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and ((int(a[0]) != 169) or (int(a[1]) != 254)) and (0 <= int(a[1]) <= 255) and (0 <= int(a[2]) <= 255) and (0 <= int(a[3]) <= 255):
                break
            else:
                print 'Invalid IP Address! Please retry.'
                continue
        masks = [255,254,252,248,240,224,192,128,0]
        
        #check subnet mask validity
        while True:
            sub_mask = raw_input('Enter Subnet Mask: ')
            
            b = sub_mask.split('.')
            #print b
            
            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
                break
            else:
                print 'Invalid Subnet Mask! Please retry.'
                continue
           
        #convert mask to binary
        mask_octet_bin = []
        mask_octet_decimal = sub_mask.split('.')
        #print mask_octet_decimal
        
        for each_decimal in mask_octet_decimal:
            each_bin = bin(int(each_decimal)).split('b')[1]
            #print each_bin
            
            if len(each_bin) == 8:
                mask_octet_bin.append(each_bin)
            elif len(each_bin) < 8:
                 bin_octet_ext = each_bin.zfill(8)
                 mask_octet_bin.append(bin_octet_ext)
        #print mask_octet_bin
        
        #join binary elements in list
        bin_mask_joined = ''.join(mask_octet_bin)
        #print bin_mask_joined
        
        host_bit_count = bin_mask_joined.count('0')
        #print host_bit_count
        
        network_bit_count = 32 - host_bit_count
        #print network_bit_count
        
        no_of_host = abs((2**host_bit_count)-2)
        #print no_of_host
        
        wildcard_octet = []
        for element in b:
            wild_mask = 255 - int(element)
            wildcard_octet.append(str(wild_mask))
        
        wildcard_mask = '.'.join(wildcard_octet)
        #print wildcard_mask
        
        #convert ip to binary
        ip_octet_bin = []
        ip_octet_decimal = ip_addr.split('.')
        #print ip_octet_decimal
        
        for each_ip_decimal in ip_octet_decimal:
            ip_bin = bin(int(each_ip_decimal)).split('b')[1]
            #print ip_bin
       
            if len(ip_bin) == 8:
                ip_octet_bin.append(ip_bin)
            elif len(ip_bin) < 8:
                ip_bin_octet_ext = ip_bin.zfill(8)
                ip_octet_bin.append(ip_bin_octet_ext)
        #print ip_octet_bin
        
        # Get Network and Broadcast address
        bin_ip_joined = ''.join(ip_octet_bin)
        net_add_bin = bin_ip_joined[:network_bit_count] + '0'*host_bit_count
        #print net_add_bin
        
        broad_add_bin = bin_ip_joined[:network_bit_count] + '1'*host_bit_count
        #print broad_add_bin
        
        net_ip_octet = []
        for elem_bin in range(0,len(net_add_bin),8):
            net_ip = net_add_bin[elem_bin : elem_bin + 8]
            net_ip_octet.append(str(int(net_ip, 2)))
        #print net_ip_octet
        
        net_ip_add = '.'.join(net_ip_octet)
        #print net_ip_add
        
        broad_ip_octet = []
        for elem_bin in range(0,len(broad_add_bin), 8):
            broad_ip = broad_add_bin[elem_bin:elem_bin + 8]
            broad_ip_octet.append(str(int(broad_ip, 2)))
        #print broad_ip_octet
        
        broad_ip_add = '.'.join(broad_ip_octet)
        #print broad_ip_add
        
        class_A = 8
        class_B = 16
        class_C = 24
        
        #Calculate Subnet
        enter_class = raw_input('Enter Network Class A, B or C: ')
        if enter_class is 'A':
            subnet_bits = abs(class_A - network_bit_count)
            number_of_subnet = 2**subnet_bits
        elif enter_class is 'B':
            subnet_bits = abs(class_B - network_bit_count)
            number_of_subnet = 2**subnet_bits
        elif enter_class is 'C':
            subnet_bits = abs(class_B - network_bit_count)
            number_of_subnet = 2**subnet_bits
        
        # Print output
        print '\n'
        print 'Network Address: ', net_ip_add
        print 'Broadcast Address: ', broad_ip_add
        print 'Number of valid host per subnet: ', no_of_host
        print 'Number of Subnet Bits: ', subnet_bits
        print 'Number of possible Subnets: ', number_of_subnet
        print 'Wildcard Mask: ', wildcard_mask
        print 'Number of Mask bits: ', network_bit_count
        print '\n' 
        
        #Generate random IP Address in subnet
        while True:
            entered_input = raw_input('\nGenerate random IP address? (y/n) :')
            
            if entered_input is 'y':
                generate_ip = []
                
                for indexb, oct_broad in enumerate(broad_ip_octet):
                    #print indexb, oct_broad
                    for indexn, oct_net in enumerate(net_ip_octet):
                        #print indexn, oct_net
                        if indexb == indexn:
                            if oct_broad == oct_net:
                                generate_ip.append(oct_broad)
                            else:
                                generate_ip.append(str(random.randint(int(oct_net), int(oct_broad))))
                            
               # print generate_ip
                rand_ip = '.'.join(generate_ip)
                print '\nRandom IP Address: ', rand_ip
                continue
                
            else:
                break
                
    except:
        print 'Program closed...'
        sys.exit()
        
subnet_calc()
            

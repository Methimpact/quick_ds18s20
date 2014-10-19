"""

"""
import string
import os
import time

mnt_dir = "/sys/bus/w1/devices/"
rd_stream = "/w1_slave"
os.system( "modprobe w1-gpio" )
os.system( "modprobe w1-therm" )

def dsgrab_data( addr ) :
    def read_stream( addr ) :
        fp = open( mnt_dir + addr + rd_stream , 'r' )
        data = fp.readlines( )
        fp.close( )
        return data

    ok = i = 0
    while not ok :
        if i :                   time.sleep( 0.1 )
        elif i > 10 :            return -1.0
        data = read_stream( addr )
        ok = data[0].find( "YES" )
        i = i + 1
        
    ok = data[1].find( "t=" )
    if ok :        return float( int( data[1][ok+2:] ) ) / 1000.0
    else :         return -1.0

it = 0
for top, dirs, files in os.walk( mnt_dir ) :
    for nm in dirs :
        if nm.startswith( '28' ) :
            print "# "+ str( it ) +" "+ str( nm ) + " "+ str( dsgrab_data( nm ) )
            it = it + 1
            

import serial, utm

# remember:
# ls -lt /dev/tty* | head

file_name = 'test3-long_run.txt' # remember to change for each run
port_name = '.usbserial-210' # remember to change for different computers


def str2dec(str):
    deg = int(float(str) / 100)
    minutes = float(str) - deg*100

    decimal = deg + minutes/60
    return decimal


port = serial.Serial("/dev/tty"+port_name, baudrate=4800, timeout=10.0)
print("connected to: " + port.portstr)

file = open(f'../GPS data/{file_name}', 'w')
print('creating text file:', file_name)
while True:
    try:
        line = port.readline()
    except:
        line = ''

    if line.startswith(b'$GPGGA'):
        line = str(line).split(",")
        try:
            lat = str2dec(line[2])
            lon = str2dec(line[4])
            alt = float(line[9])

            [easting, northing, zone, letter] = utm.from_latlon(lat, lon)

            print('easting, northing, alt:', easting, northing, alt)
            file.write(f"{easting} {northing} {alt}\n")

        except:
            print('no data:', line)
            pass
        
file.close()
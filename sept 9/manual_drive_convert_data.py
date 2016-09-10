# parsing the gps data from the super field test
# with the new barometer sensor!
# 
# frequency - 1s, 5s, 30s, 60s, 120s, 300s
# file 1 - simple:
# lat, lon
# file 2 - for a map:
# lat, lon, alt, heading dir
# file 3 - more info:
# date, time, sats, hdop, lat, lon, alt, speed, heading, heading dir
#
# by Erin RobotGrrl for Robot Missions
# http://robotmissions.org
# Aug 27, 2016

f = open('MANUAL_DRIVE.TXT', 'r')

frequency = 1
#file1 = open('file1.csv', 'w')
file2 = open('manual_drive_path.csv', 'w')
#file3 = open('file3.csv', 'w')

#file1.write("latitude, longitude\n")
file2.write("latitude, longitude, datanum, time, pressure, altitude, temperature\n")
#file3.write("datanum, date, time, sats, hdop, latitude, longitude, altitude, speed, heading, heading dir, pressure, altitude, temperature\n")

linenum = 0
datanum = 0

for line in f:
  if linenum < 3:
    print("skip")
  else:
    if (linenum-3)%frequency == 0:
        s = f.readline()
        splittystring = s.split(" ")

        datum = []
        for item in splittystring:
            if item == ' ' or item == '' or item == '\n':
                1+1
            else:
                datum.append(item)
        
        sats = datum[0]
        hdop = datum[1]
        lat = datum[2]
        lon = datum[3]
        fix_age = datum[4]
        date = datum[5]
        time = datum[6]
        date_age = datum[7]
        alt = datum[8]
        speed = datum[9]
        heading = datum[10]
        heading_dir = datum[11]
        chars_processed = datum[12]
        sentences_with_fix = datum[13]
        failed_checksum = datum[14]
        pressure = datum[15]
        altitude = datum[16]
        temperature = datum[17]

        datanum = datanum+1

        #file1.write("%s, %s\n" % (lat, lon))
        file2.write("%s, %s, %d, %s, %s, %s, %s\n" % (lat, lon, datanum, time, pressure, altitude, temperature))
        #file3.write("%d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n" % (datanum, date, time, sats, hdop, lat, lon, alt, speed, heading, heading_dir, pressure, altitude, temperature))

        print("%d sats %s" % (linenum, sats))

  linenum = linenum+1


#file1.close()
file2.close()
#file3.close()

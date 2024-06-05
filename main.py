hid = open("HID_Sign.txt", "x")
count = 0
sec = 0
min = 0
mtfcount = 0
elg = False
length = 1200 #how many seconds this program will run for. Default is 1200 (20 minutes)

while count <= length:
    if sec % 60 == 0 and count != 0:
        sec -= 60
        min += 1
    if count % 280 == 0 and count != 0:
        elg = True
    if elg == True and mtfcount <= 70:
        hid.write( f"{min:02d}:" + f"{sec:02d}" + " Spawn Eligible" + "\n")
        hid.write( f"{min:02d}:" + f"{sec:02d}" + " Spawn Eligible" + "\n")
        mtfcount += 1
        count += 1
        sec += 1
    else:
        elg = False
        mtfcount = 0
        hid.write( f"{min:02d}:" + f"{sec:02d}" + "\n")
        hid.write( f"{min:02d}:" + f"{sec:02d}" + "\n")
        count += 1
        sec += 1

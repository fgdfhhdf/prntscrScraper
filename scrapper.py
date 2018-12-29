import string, random, urllib, os, thread, array, sys


if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python " + sys.argv[0] + " (Number of threads)")
threadAmount = int(sys.argv[1])


temp = 0
#while temp < 10:

noneWorking = [0, 503, 4939, 4940, 4941, 12003, 5556]


def scrapePictures():
    while True:
        # N = int(''.join(random.choice('1' + '2') for _ in range(1)))
        amount = int(''.join(random.choice('5' + '6') for _ in range(1)))

        N = 5
        picture2 = ''

        if amount == 6:
            N = 3
            picture2 = str(''.join(random.choice(string.digits + string.lowercase) for _ in range(N)))
        picture = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(N)))
        name = str(picture) + str(picture2)
        printsc = "http://i.imgur.com/" + name + ".jpg"
        jpg_name = "images/%s.jpg" % name
        png_name = "images/%s.png" % name

        urllib.urlretrieve(printsc, jpg_name)

        f = open(jpg_name, 'r')
        flines = f.read().splitlines()
        fsize = os.path.getsize(jpg_name)

        if (fsize in noneWorking) or (flines[-1] == '</html>'):
            print "[-] Invalid: " + jpg_name
            os.remove(jpg_name)
        else:
            if bytes(flines[0]) == '\x89PNG':
                os.rename(jpg_name, png_name)
                print "[+] Valid: " + png_name
            else:
                print "[+] Valid: " + jpg_name


tempVar2 = 1
#threadAmount = sys.argv[2]
while (tempVar2 <= threadAmount):
    try:
        print ("Starting thread #" + str(tempVar2))
        thread.start_new_thread(scrapePictures, ())
        tempVar2 += 1
    except:
        print "Error initializing thread...."

#Make threads never stop
while (True):
    temp = 1+1
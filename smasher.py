import os
import sys
import time
import random

def main():
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    count = 0
    while True:
        randomhash = random.getrandbits(128)
        randombits = random.getrandbits(3650)

        # Message size payload will be ~1.2KB
        print 'LogSmasher for OpenShift generated at:',time.ctime(),' counter:',count,' hash:',randomhash,' data:',randombits
        count = count + 1

        # Create 1000+ events/second
        time.sleep(.0002)

if __name__ == "__main__":
    main()

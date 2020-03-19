import pigpio
import time

RX = 15
GREEN = 21
RED = 16
BLUE = 20
BUZZ = 17

pi = pigpio.pi()
pi.set_mode(RX, pigpio.INPUT)
pi.set_mode(GREEN, pigpio.OUTPUT)
pi.set_mode(RED, pigpio.OUTPUT)
pi.set_mode(BUZZ, pigpio.OUTPUT)

# pi.bb_serial_read_close(RX)
pi.bb_serial_read_open(RX, 115200)


def getTFminiData():
    loop = 1
    prev = []
    while True:
        time.sleep(0.1)   # Time between sensor reads
        (count, recv) = pi.bb_serial_read(RX)
        if count > 8:
            for i in range(0, count-9):
                if recv[i] == 89 and recv[i+1] == 89:
                    checksum = 0
                    for j in range(0, 8):
                        checksum = checksum + recv[i+j]
                    checksum = checksum % 256
                    if checksum == recv[i+8]:
                        distance = recv[i+2] + recv[i+3] * 256
                        strength = recv[i+4] + recv[i+5] * 256
                        if distance <= 1200 and strength < 2000:
                            # print(distance, strength)
                            prev.insert(0, distance)
                            if loop > 2:
                                del prev[2]
                            if loop > 2 and prev[0] > prev[1] + 10:
                                pi.write(BUZZ, 1)
                                pi.write(RED, 1)
                                time.sleep(1)
                                pi.write(BUZZ, 0)
                                pi.write(RED, 0)
                            # print("[new, prev] = {}".format(prev))
                            loop += 1


if __name__ == '__main__':
    try:
        getTFminiData()
    except KeyboardInterrupt:
        pi.bb_serial_read_close(RX)
        pi.write(RED, 0)
        pi.write(BUZZ, 0)
        pi.stop()
        print('Program stopped...')

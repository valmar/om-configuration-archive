import numpy
import time
import client

print('Connecting...')
krb_client = client.Client('tcp://10.253.0.51:4510')
print('Listening...')

while True:
    event = {}
    event['data'], event['metadata'] = krb_client.next()
    timestamp = numpy.float64(str(event['metadata']['SPB_DET_AGIPD1M-1/CAL/APPEND_CORRECTED']['timestamp.sec']) + '.' + str(event['metadata']['SPB_DET_AGIPD1M-1/CAL/APPEND_CORRECTED']['timestamp.frac']))
    curr = time.time()
    print('Delay:', curr-timestamp)
    time.sleep(3.5)


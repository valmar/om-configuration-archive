import h5py
import sys
import numpy

file_in = sys.argv[1]
file_out = sys.argv[2]

fh_in = h5py.File(file_in, 'r')
data_in = fh_in['/data/data'][:]
fh_in.close()

data_out = numpy.zeros((16*128, 512), dtype=numpy.int16)

for p_num in range(0, 16):

    print('Converting panel:', p_num)

    p_in = data_in[
        512 * p_num:
        512 * (p_num + 1),

        0:128
    ]

    p_out = data_out[
        128 * p_num:
        128 * (p_num + 1),

        0:512
    ]

    for y in range(0, 128):
        for x in range(0, 512):
            p_out[y,x] = p_in[x,y]

fh_out = h5py.File(file_out, 'w')
fh_out.create_dataset('/data/data', data=data_out)
print('Done!')
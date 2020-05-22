import h5py
import sys
import pyqtgraph


mask_file = h5py.File(sys.argv[1], 'r')
print 'Opened mask file:', sys.argv[1]
mask = mask_file['/data/data'][:]


def show_sum(filenames): 

    total_sum = None

    for filename in filenames:

       print 'Summing file', filename

       file_ = h5py.File(filename, 'r')
       print 'Opened file:', filename
       data = file_['/entry/data/data'][:]
       file_.close()

       print 'Summing',data.shape[0],"frames"
       sum_ = data.sum(axis=0)

       if total_sum is None:
           total_sum = sum_
       else:
           total_sum += sum_

    masked_total_sum = total_sum * mask
    image_window = pyqtgraph.show(masked_total_sum)



def show_sum_with_subtraction(filenames, filenames_to_subtract, factor=1.0): 

    total_sum = None

    for filename in filenames:

        print 'Summing file', filename

        file_ = h5py.File(filename, 'r')
        print 'Opened file:', filename
        data = file_['/entry/data/data'][:]
        file_.close()

        print 'Summing',data.shape[0],"frames"
        sum_ = data.sum(axis=0)

        if total_sum is None:
            total_sum = sum_
        else:
            total_sum += sum_

    masked_total_sum = total_sum * mask

   
    total_sum_to_subtract = None
 
    for filename in filenames_to_subtract:

        print 'Summing file for subtraction', filename

        file_ = h5py.File(filename, 'r')
        print 'Opened file:', filename
        data = file_['/entry/data/data'][:]
        file_.close()

        print 'Summing',data.shape[0],"frames"
        sum_to_s = data.sum(axis=0)

        if total_sum_to_subtract is None:
            total_sum_to_subtract = sum_to_s
        else:
            total_sum_to_subtract += sum_to_s

    masked_total_sum_to_subtract = total_sum_to_subtract * mask

    subtracted = masked_total_sum - (masked_total_sum_to_subtract * factor)
    image_window = pyqtgraph.show(subtracted)




from __future__ import print_function
import sys
import h5py
import numpy as np
import glob

scan_files = '/gpfs-bl/current/raw/sardana/0001_alignment/scan_[scan_num]/eiger4m_01/scan_[scan_num]_data_*.h5'
output     = '/gpfs-bl/current/shared/whitefield_scan_[scan_num].h5'
 
if __name__ == '__main__':
    scan_no = int(sys.argv[1])
    
    # replace [scan_num] with zero padded scan_nos
    scan_files = scan_files.replace('[scan_num]', str(scan_no).zfill(5))
    fnams = np.sort([fnam.strip() for fnam in glob.glob(scan_files)])
        
    # read the frames
    frames = []
    for fnam in fnams :
        try : 
            f = h5py.File(fnam)
            frames += [f['entry/data/data'][i] for i in range(f['entry/data/data'].shape[0])]
            f.close()
        except Exception as e :
            print(e)
            print('failed to read:', fnam)
    white = np.mean(np.array(frames).astype(np.float), axis=0)
    white[white > 1e7] = 1.
    white[white == 0]  = 1.
    
    # output fnam
    out_fnam = output.replace('[scan_num]', str(scan_no).zfill(5))
    print('outputing whitefield to:', out_fnam)
    f = h5py.File(out_fnam, 'w')
    if 'data/data' in f :
        print('deleting previous entry...')
        del f['data/data'] 
    f['data/data'] = white
    f.close()
    print('Done!')

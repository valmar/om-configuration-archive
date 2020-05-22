from __future__ import print_function
import sys
import h5py
import numpy as np
import glob
import PIL.Image
import os.path

scan_files = '/gpfs-bl/current/raw/sardana/0001_alignment/scan_[scan_num]/eiger4m_01/scan_[scan_num]_data_*.h5'
output     = '/gpfs-bl/current/shared/tifs/'

 
if __name__ == '__main__':
    scan_no = int(sys.argv[1])
    whitefield_filename = sys.argv[2]
    
    with h5py.File(whitefield_filename) as f:
       whitefield = f['/data/data/'][:]

    # replace [scan_num] with zero padded scan_nos
    scan_files = scan_files.replace('[scan_num]', str(scan_no).zfill(5))
    out_fnam = output.replace('[scan_num]', str(scan_no).zfill(5))
    fnams = np.sort([fnam.strip() for fnam in glob.glob(scan_files)])
        
    # read the frames
    frames = []
    for fnam in fnams :
        print('Processing', fnam)
        try : 
            with h5py.File(fnam) as f:
                for i in range(f['entry/data/data'].shape[0]):
                    frame = f['entry/data/data'][i]
                    frame[frame > 1e7] = 0.
                    corr_frame = frame/whitefield
                    frame_img = PIL.Image.fromarray(corr_frame)
                    frame_img.save(os.path.join(output, os.path.basename(fnam)+'_'+str(i).zfill(5)+'.tif'))
        except Exception as e :
            print(e)
            print('failed to read:', fnam)
    print('Done!')

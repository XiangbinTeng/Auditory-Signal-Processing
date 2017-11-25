# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:16:59 2016
I add something here
@author: xiangbin
"""

import os.path as op
from mne.io import read_raw_kit

freesurfer_dir = '/Users/xiangbin/Desktop/MNE/Anatomy'
subject = 'R0420'

meg_subject_dir = '/Users/xiangbin/Dropbox/EXP_Classification/data/R0420'

# -- KIT data is split between different files
raw_kit_fname = op.join(meg_subject_dir, 'R0420_singletone_4.30.15.sqd')
mrk_fname = op.join(meg_subject_dir, 'R0420_Marker1_4.30.15.sqd')  # markers
hsp_fname = op.join(meg_subject_dir, 'R0398_BS.txt')  # digitization
elp_fname = op.join(meg_subject_dir, 'R0398_MK.txt')  # landmarks


# -- The following files will be created in this script.
raw_fname = op.join(meg_subject_dir, 'R0398_singletone.fif')
fwd_fname = op.join(meg_subject_dir, subject + '-meg-fwd.fif')
cov_fname = op.join(meg_subject_dir, subject + '-cov.fif')
inv_fname = op.join(meg_subject_dir, subject + '-inv.fif')

overwrite = False
# 0. Depending on what we do, we'll need epoch data at several steps. Hence
# the function. This is the most ad-hoc part.

global epochs
epochs = None


if overwrite or not op.exists(raw_fname):
    raw = read_raw_kit(raw_kit_fname, mrk=mrk_fname, elp=elp_fname,
                       hsp=hsp_fname)
    raw.save(raw_fname, overwrite=overwrite)
else:
    from mne.io import Raw
    raw = Raw(raw_fname, preload=False)
    
    
save_dir = '/'.join(raw_fname.split('/')[:-1])
print('Save/read directory: %s' % save_dir)
    
    
trans_fname = op.join(save_dir,  '-trans.fif')
bem_sol_fname = op.join(freesurfer_dir, subject, 'bem',
                                subject + '-5120-bem-sol.fif')
oct_fname = op.join(freesurfer_dir, subject, 'bem',
                            subject + '-oct-6-src.fif')
fwd_fname = op.join(save_dir, subject + '-meg-fwd.fif')
    
    
    
overwrite=True
    
from mne.bem import make_watershed_bem
    
    
    
    
make_watershed_bem(subject=subject, subjects_dir=freesurfer_dir,overwrite=True, volume='T1', atlas=False,gcaatlas=False, preflood=None)
    
    
    
    

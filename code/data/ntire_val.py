import os

from data import common
from data import srdata

import numpy as np
import scipy.misc as misc

import torch
import torch.utils.data as data

class NTIRE_VAL(srdata.SRData):
    def __init__(self, args, train=True):
        super(NTIRE_VAL, self).__init__(args, train)
        self.repeat = args.test_every / (args.n_train / args.batch_size)

    def _scan(self):
        list_hr = []
        list_lr = [[] for _ in self.scale]
        if self.train:
            NotImplementedError
        else:
            idx_begin = 0
            idx_end = self.args.n_val
        
        for j in [1,2]:
            for i in range(idx_begin + 1, idx_end + 1):
                filename = 'cam{}_0{}'.format(j, i)
                list_hr.append(os.path.join(self.dir_hr, filename + self.ext))

                list_lr[0].append(os.path.join(
                        self.dir_lr,
                        '{}{}'.format(filename, self.ext)
                    ))

        return list_hr, list_lr

    def _set_filesystem(self, dir_data):
        self.apath = dir_data + '/ntire2019'
        self.dir_hr = os.path.join(self.apath, 'val')
        self.dir_lr = os.path.join(self.apath, 'val')
        self.ext = '.png'

    def _name_hrbin(self):
        return os.path.join(
            self.apath,
            'bin',
            '{}_bin_HR.npy'.format(self.split)
        )

    def _name_lrbin(self, scale):
        return os.path.join(
            self.apath,
            'bin',
            '{}_bin_LR_X{}.npy'.format(self.split, scale)
        )

    def __len__(self):
        if self.train:
            return int(len(self.images_hr) * self.repeat)
        else:
            return len(self.images_hr)

    def _get_index(self, idx):
        if self.train:
            return idx % len(self.images_hr)
        else:
            return idx


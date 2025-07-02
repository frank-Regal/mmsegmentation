# Copyright (c) The University of Texas at Austin. All rights reserved.

from mmseg.registry import DATASETS
from mmseg.datasets.basesegdataset import BaseSegDataset

@DATASETS.register_module()
class EgoNRGDataset(BaseSegDataset):
    """EgoNRG dataset definition."""

    METAINFO = dict(
        classes=('background', 
                 'left_limb', 
                 'right_limb'),
        palette=[[0, 0, 0],   # black
                 [0, 0, 255], # blue
                 [0, 255, 0]] # green
    )

    def __init__(self,
                 img_suffix='.png',     # raw image suffix
                 seg_map_suffix='.png', # ann image suffix
                 **kwargs):
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

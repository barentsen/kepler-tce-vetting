"""Extract temperatures from the Kepler ancillary engineering data files."""
import os
import glob
from astropy.io import fits
import pandas as pd

PATH = '/home/gb/Downloads/*anc-eng*'
FIELDS = ['PEDDRV1T', 'PEDDRV2T', 'PEDDRV3T', 'PEDDRV4T', 'PEDDRV5T',
          'PEDACQ1T', 'PEDACQ2T', 'PEDACQ3T', 'PEDACQ4T', 'PEDACQ5T']
OUTPUT_DIR = '/tmp'

for filename in glob.glob(PATH):
    fts = fits.open(filename)
    for field in FIELDS:
        output_fn = '{}-{}.csv'.format(os.path.basename(filename), field)
        pd.DataFrame(fts[field].data).to_csv(
                                        os.path.join(OUTPUT_DIR, output_fn),
                                        index=False)


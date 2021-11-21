import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.

    files = []

    for file in os.listdir(data_dir):
        files.append(file)

    random.shuffle(files)
    train = 100 * 75 / len(files)
    val = len(files) - (100 * 10 / len(files))
    test = len(files)

    train_path = data_dir + "../train/"
    val_path = data_dir + "../val/"
    test_path = data_dir + "../test/"

    file_counter = 0

    for file in files:
        source_file = data_dir + file
        dest_file = ""

        if file_counter < train:
            dest_file = train_path + file

        if train <= file_counter and file_counter < val:
            dest_file = val_path + file


        if val <= file_counter < test:
            dest_file = test_path + file

        os.popen("cp {} {}".format(source_file, dest_file))

        file_counter += 1
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)
from cirrus import Preprocessing, Normalization
import numpy as np
import boto3
import os

local_path = "csv_to_libsvm_train.txt"
s3_input = "criteo-kaggle"
s3_output = "criteo-norm"

s3 = boto3.client('s3')
# if os.path.isfile(local_path):
#     print("found")
# else:
#     print("Downloading file")
#     s3.download_file('cirrus-public', 'csv_to_libsvm.txt', local_path)

Preprocessing.load_libsvm(local_path, s3_input)
Preprocessing.normalize(s3_input, s3_output,
    Normalization.MIN_MAX, 0.0, 1.0)

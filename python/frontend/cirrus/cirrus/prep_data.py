from cirrus import Preprocessing, Normalization
import numpy as np

local_path = "lshtc/test-mini.csv"
s3_input = "criteo-kaggle"
s3_output = "criteo-norm"
Preprocessing.load_libsvm(local_path, s3_input)
Preprocessing.normalize(s3_input, s3_output,
    Normalization.MIN_MAX, 0.0, 1.0)

import os
os.system("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/python3.8/site-packages/tensorrt/")
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
import tensorrt
print(tensorrt.__version__)
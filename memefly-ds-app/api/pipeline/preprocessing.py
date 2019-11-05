import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.inception_v3 import preprocess_input
from api.config import get_logger

_logger = get_logger(logger_name=__name__)

async def extract_features(*, model: tf.keras.models,
                     img_array: np.ndarray) -> np.ndarray:
    """
    Extracts image feature vectors from an image file using a pretrained/saved
    InceptionV3 model without classification layers.

    INPUTS:
    ========
    model: pretrained InceptionV3 model without classification layers.
    img_file: path/filename of the image file to be loaded.

    OUTPUTS:
    ========
    feature: image embeddings, shape (2048, 1)
    """

    image = img_array.reshape((1, img_array.shape[0],
                               img_array.shape[1], img_array.shape[2]))

    image = preprocess_input(image)
    feature = model.predict(image, verbose=0)

    return feature

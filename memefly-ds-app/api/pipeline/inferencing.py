import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.inception_v3 import preprocess_input
from api.config import get_logger

_logger = get_logger(logger_name=__name__)


def generate_text(model: tf.keras.models, tokenizer: tf.keras.preprocessing,
                  img_emb: np.ndarray, max_length: int) -> str:
    """
    This function generates text using trained image captioning model. To 
    generate text, we have to seed the sentence with a 'startseq' token. We will
    then use the model to predict the next word in the sequence, until the next 
    word is either None or 'endseq'. We choose to use 'startseq' and 'endseq' 
    to mark the beginning and the end of the sentence as start/end are common
    words, and <START> and <END>will get scrubbed/cleaned by Keras tokenizers.

    Input:
    ========
    model: pretrained and loaded keras model
    tokenizer: pretrained tokenizer that's responsible to convert from either 
        word to
    integer or integer to word
    img_emb: image feature extracted using pretrained InceptionV3, expected 
        shape (2048,)
    max_length: maximum length of the generated meme text

    Output:
    ========
    sentence: sentences, python string.
    """
    # seed the start of the sentence
    sentence = 'startseq'

    for i in range(max_length):
        # encode input sequence to integer
        sequence = tokenizer.texts_to_sequences([sentence])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)

        next_word = model.predict([img_emb, sequence], verbose=0)
        next_word = np.argmax(next_word)
        word = tokenizer.sequences_to_texts([[next_word]])[0]

        if word is None:
            break
        sentence += ' ' + word
        if word == 'endseq':
            break

    sentence = ' '.join(w for w in sentence.split() if w not in ['startseq', 'endseq'])

    return sentence

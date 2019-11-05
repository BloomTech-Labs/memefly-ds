"""Keras network code for the cnn -> rnn encoder decoder for image caption.""" 
from typing import List, Tuple 
from tensorflow.keras.models import Input, Model
from tensorflow.keras.layers import Dense, GRU, Embedding, Droupout, add, Concatenate, 
from tensorflow.keras import backend as K


def cnn_par_inject_rnn_network(*, vocab_size: int, maxlen: int, embedding_dim: int, rnn_units: int, batch_size: int) -> tf.keras.Model:
    """
    Injecting image embedding using par-inject method (3) as described in the following paper.
    [Where to put the Image in an Image CaptionGenerator](https://arxiv.org/abs/1703.09137)
    
    Par-inject was used as [Neural Image Caption Generation with Visual Attention](https://arxiv.org/abs/1502.03044)
    """    
    img_emb_input = Input(shape=(2048,), name="image_input")
    x1 = Dropout(0.5, name='image_dropout')(img_emb_input)
    x1 = Dense(embedding_dim, activation='relu', name='image_dense')(x1)
    x1 = RepeatVector(maxlen, name='image_repeat')(x1)

    tokenized_text_input = Input(shape=(maxlen,), name='text_input')
    x2 = Embedding(vocab_size,
                   embedding_dim,
                   mask_zero=True,
                   batch_input_shape=[batch_size, None],
                   name='text_embedding')(tokenized_text_input)
    
    decoder = Concatenate(name='concat_image_text')([x1, x2])
    decoder = GRU(rnn_units, name='GRU_combined')(decoder)
    decoder = Dense(256, activation='relu', name='combined_dense')(decoder)
    outputs = Dense(vocab_size, activation='softmax', name='output')(decoder)

    model = Model(inputs=[img_emb_input, tokenized_text_input], outputs=outputs)
    
    return model

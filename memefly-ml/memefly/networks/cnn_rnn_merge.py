"""Keras network code for the cnn -> rnn encoder decoder for image caption.""" 
from typing import List, Tuple 
from tensorflow.keras.models import Input, Model
from tensorflow.keras.layers import Dense, GRU, Embedding, Droupout, add, Add, RepeatVector, Attention
from tensorflow.keras import backend as K

def cnn_merge_rnn_network(*, vocab_size: int, max_length:int) -> Model:
    """
    Function to instantiate a cnn-rnn encoder decoder model, with image embedding injection
    using merge method (4) as described in the following paper.
    [Where to put the Image in an Image CaptionGenerator](https://arxiv.org/abs/1703.09137)
    """     
    img_emb_input = Input(shape=(2048,), name="image_input")
    x1 = Dropout(0.5, name='image_dropout')(img_emb_input)
    x1 = Dense(256, activation='relu', name='image_dense')(x1)

    tokenized_text_input = Input(shape=(max_length,), name='text_input')
    x2 = Embedding(vocab_size, 256, mask_zero=True, name='text_embedding')(tokenized_text_input)
    x2 = Dropout(0.5, name='text_dropout')(x2)
    x2 = GRU(256, name='GRU_text')(x2)
    
    decoder = add([x1, x2], name='add')
    decoder = Dense(256, activation='relu', name='combined_dense')(decoder)
    outputs = Dense(vocab_size, activation='softmax', name='output')(decoder)

    model = Model(inputs=[img_emb_input, tokenized_text_input], outputs=outputs)

    return model
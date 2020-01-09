from typing import Callable, Dict
import os
import sys
import time
sys.path.append(os.path.abspath('..'))
import numpy as np

<<<<<<< HEAD
from memefly.datasets import MemeflyDataset
from memefly.networks import cnn_par_inject_rnn_network
from memefly.datasets import MemeDataGenerator
import wandb
=======
#from memefly.models import base_model
from memefly.datasets import MemeflyDataset
from memefly.networks import cnn_par_inject_rnn_network
from memefly.datasets import MemeDataGenerator
#import wandb
>>>>>>> c3a097b... 'rc'

class Config:
    DATA_VERSION = 'v2'
    MODEL_TYPE = 'word'
    TIMESTAMP = time.strftime('%Y%m%d%H%M')
    TOKENIZER = f'../weights/memefly-{MODEL_TYPE}-data-{DATA_VERSION}-tokenizer.pkl'
    IMAGE_MODEL_FILENAME = "../weights/inceptionv3_embeddings.h5"

INPUT_JSON_FILE = '../datasets/combined_data.json'
DESCRIPTION_FILE = f'../datasets/memefly-{Config.DATA_VERSION}-descriptions.txt'
IMG_FEATURES_PKL = f'../datasets/memefly-{Config.DATA_VERSION}-features.pkl'

<<<<<<< HEAD
=======
#Config = Config()
>>>>>>> c3a097b... 'rc'
dataset = MemeflyDataset(input_json_file=INPUT_JSON_FILE,
                         img_model=Config.IMAGE_MODEL_FILENAME, 
                         description_file=DESCRIPTION_FILE, 
                         img_features_pkl=IMG_FEATURES_PKL)
dataset.preprocess_text()
dataset.preprocess_img()

meme_dataset = dataset.text_data
MEME_IMG_VEC = dataset.img_data
VOCAB_SIZE = dataset.vocab_size
MAX_LENGTH = dataset.max_length
TOKENIZER = dataset.tokenizer
print(f"Full data: {len(meme_dataset)}\nmemes images: {len(MEME_IMG_VEC)}\nVocab size: {VOCAB_SIZE}\nMax meme length: {MAX_LENGTH}\n")

train_dataset, val_dataset = train_test_split(meme_dataset, test_size=0.05)
print(len(train_dataset), len(val_dataset))

model = image_captioning_model(vocab_size=VOCAB_SIZE, 
                               maxlen=MAX_LENGTH, 
                               embedding_dim=256, 
                               rnn_units=256, 
                               batch_size=BATCH_SIZE)

<<<<<<< HEAD
wandb.init(config={"hyper": "parameter"}, project="")

EPOCHS = 100
BATCH_SIZE = 128
=======
# wandb.init(config={"hyper": "parameter"}, project="proj_m")

EPOCHS = 2
# BATCH_SIZE = 35 # 6GB ram max. V100 32GB p3.2xlarge can fit 250.

# EPOCHS = 10
# BATCH_SIZE = 250
>>>>>>> c3a097b... 'rc'

train_datagen = MemeDataGenerator(dataset=train_dataset, 
                                  img_embds=MEME_IMG_VEC,
                                  tokenizer=TOKENIZER,
                                  batch_size=BATCH_SIZE,
                                  max_length=MAX_LENGTH,
                                  vocab_size=VOCAB_SIZE)

val_datagen = MemeDataGenerator(dataset=val_dataset,
                                img_embds=MEME_IMG_VEC,
                                tokenizer=TOKENIZER,
                                batch_size=BATCH_SIZE,
                                max_length=MAX_LENGTH,
                                vocab_size=VOCAB_SIZE)

model = image_captioning_model(vocab_size=VOCAB_SIZE, 
                               maxlen=MAX_LENGTH, 
                               embedding_dim=256, 
                               rnn_units=256, 
                               batch_size=BATCH_SIZE)

filepath = f"../weights/ckpt/memefly-{Config.MODEL_TYPE}-{MAX_LENGTH}-{Config.TIMESTAMP}"+"-{epoch:02d}-{val_loss:.2f}.h5"
checkpoint = ModelCheckpoint(filepath, 
                             verbose=1, 
                             save_weights_only=False, 
                             save_best_only=False)

model.fit_generator(train_datagen, 
                    epochs=EPOCHS, 
                    verbose=1, 
                    validation_data=val_datagen,
                    callbacks=[checkpoint])
<<<<<<< HEAD
                    callbacks=[WandbCallback(), checkpoint])
=======
                    #callbacks=[WandbCallback(), checkpoint])
>>>>>>> c3a097b... 'rc'

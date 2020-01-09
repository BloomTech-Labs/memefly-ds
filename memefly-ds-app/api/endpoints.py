import os
from fastapi import APIRouter
from pydantic import BaseModel
import tensorflow as tf
import pickle
from api.config import DevelopmentConfig as conf
from api.pipeline import ingesting, preprocessing, inferencing, postprocessing, beam_search

MEME_GEN_MODEL = conf.MODEL
TOKENIZER = conf.TOKENIZER
IMG_FEATURE_EXTRACTOR = conf.IMG_FEATURE_EXTRACTOR
VERSION = 'VERSION'
MAX_LENGTH = conf.MAX_LENGTH

# Load all the necessary model files at startup.
tokenizer = pickle.load(open(TOKENIZER, 'rb'))
img_vec_model = tf.keras.models.load_model(IMG_FEATURE_EXTRACTOR, compile=False)
text_gen_model = tf.keras.models.load_model(MEME_GEN_MODEL)

with open(VERSION) as file_io:
    version = [line.rstrip() for line in file_io]

bounding_box = postprocessing.bounding_box_dict_gen('api/combined_data.json')

# Starts the FastAPI Router to be used by the FastAPI app.
router = APIRouter()


@router.get('/')
async def root():
    """
    Root URL, for version checking.
    """
    return f"Memefly REST API, Model {version[0]}"


@router.get('/get-meme-names')
def get_meme_names():
    """
    This endpoint returns a list of meme names used in training.
    """
    return list(bounding_box.keys())


class MemeName(BaseModel):
    """
    Input schema class for generate_meme_text. Forces FastAPI to use MemeName
    object for type checking w/ pydantic. Without type checking, FastAPI post
    requests url response will appear like get reequest.
    """
    mname: str


@router.post('/generate-meme-text')#, response_model=MemeName)
async def generate_meme_text(*, mname: MemeName):
    """
    POST SCHEMA:
    {"meme_name": string}

    OUTPUTS:
    ========
    {"meme_url": string,
     "meme_text": string,
     "bounding_box": list,}
    """
    meme_name = mname.mname

    # Model inferencing pipeline. ingesting -> preprocessing -> inferencing.
    img = await ingesting.load_img_from_url(meme_name=meme_name)
    img_emb = await preprocessing.extract_features(model=img_vec_model,
                                             img_array=img)
<<<<<<< HEAD
<<<<<<< HEAD
    meme = inferencing.generate_text(model=text_gen_model,
                                     tokenizer=tokenizer,
                                     img_emb=img_emb,
                                     max_length=MAX_LENGTH)
=======
=======
>>>>>>> 3452575... 'rc'
    # meme = inferencing.generate_text(model=text_gen_model,
    #                                  tokenizer=tokenizer,
    #                                  img_emb=img_emb,
    #                                  max_length=MAX_LENGTH)
    meme = await beam_search.beamsearch(beam_search.probabilities_function,
                                  model=text_gen_model,
                                  tokenizer=tokenizer,
                                  img_emb=img_emb,
                                  maxlen=MAX_LENGTH,
                                  beam_width=1)
<<<<<<< HEAD
>>>>>>> c3a097b... 'rc'
=======
>>>>>>> 3452575... 'rc'

    return {'meme_url' : bounding_box[meme_name][0],
            "meme_text" : meme,
            "bounding_box": bounding_box[meme_name][1]}

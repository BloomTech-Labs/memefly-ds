#import os
#import sys
import tempfile
import requests
import shutil
import boto3
#from dotenv import load_dotenv
#from decouple import config
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from api.config import DevelopmentConfig as conf
from api.config import get_logger


_logger = get_logger(logger_name=__name__)
BUCKET_NAME = conf.BUCKET_NAME #config('BUCKET_NAME')
S3_FOLDER = conf.S3_FOLDER #config('IMG_FOLDER_NAME')


#def load_env():
#    if load_dotenv(dotenv_path='.env'):
#        _logger.info('[INFO]: Environment file loaded successfully')
#    else:
#        load_dotenv(find_dotenv())
#        _logger.info('[INFO]: Environment file loaded successfully')
#
# def load_img_from_aws(*, meme_name: str) -> np.ndarray:
#    # BUCKET_NAME = 'memefly-datalake'
#    # S3_FOLDER = 'base-meme-images'
#
#    #load_env()
#
#    s3 = boto3.resource(
#        's3',
#        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
#        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
#    )
#
#    bucket = s3.Bucket(BUCKET_NAME)
#    s3_link = f"{S3_FOLDER}/{meme_name}.jpg"
#    _logger.debug(f'DEBUG {s3_link}')
#
#    try:
#        object = bucket.Object(s3_link)
#    except Exception as e:
#        _logger.error(f'[ERROR]: S3 Object Initialization Error: {e}')
#        sys.exit(1)
#
#    try:
#        tmp = tempfile.NamedTemporaryFile()
#        with open(tmp.name, 'wb') as f:
#            object.download_fileobj(f)
#    except Exception as e:
#        _logger.error(f'[ERROR]: S3 Object Downloading Error: {e}')
#        sys.exit(1)
#
#    try:
#        image = load_img(tmp.name, target_size=(299, 299))
#    except Exception as e:
#        _logger.error(f'[ERROR]: Image Reading Error: {e}')
#        sys.exit(1)
#
#    image = img_to_array(image)
#
#    return image


async def load_img_from_url(*, meme_name: str) -> np.ndarray:
    """
    Load image from public AWS S3 bucket given the meme_name. The URL is pseudo
    hard coded.

    OUTPUT:
    ========
    image vector of the meme_name.
    """

    url = f"https://memefly-datalake.s3.us-east-2.amazonaws.com/base-meme-images/{meme_name}.jpg"

    # Have to use long headers otherwise AWS will throw 403 forbidden errors.
    # Also, request headers dont like line breaks, so this is a long string.
    headers = {'User-Agent': """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"""}

    _logger.info(f"[DEBUG]: url is {url}")
    _logger.info(f"[DEBUG]: header is {url}")

    r = requests.get(url, headers=headers)

    print(r.status_code, "\n\n\n")

    try:
        if r.status_code == 200:
            try:
                tmp = tempfile.NamedTemporaryFile()
                with open(tmp.name, 'wb')as f:
                    f.write(r.content)
            except Exception as e:
                _logger.error(f"[ERROR]: tempfile open error {e}")
                sys.exit(1)
    except Exception as e:
        _logger.error(f"[ERROR]: status code {e}")
        sys.exit(1)


    image = load_img(tmp.name, target_size=(299, 299))
    image = img_to_array(image)

    return image

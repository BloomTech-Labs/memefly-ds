from api.config import get_logger
import json

_logger = get_logger(logger_name=__name__)


def bounding_box_dict_gen(json_file: str) -> dict:
    """
    Read and parse json data and returns a dictionary of
    {'meme_name': 'meme_bounding_box'}
    """
    try:
        with open(json_file) as json_obj:
            json_data = json_obj.read()
    except Exception as e:
        _logger.exception('[ERROR]: Error opening json file {e}')
        sys.exit(1)

    data = json.loads(json_data)
    meme_dict = dict()
    for item in iter(data):
        meme_name = item['meme_name']
        meme_info = [item['meme_url'], item['meme_bounding_box']]
        meme_dict[meme_name] = meme_info

    return meme_dict

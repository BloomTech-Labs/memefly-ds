import os
import json
import requests
import shutil
#import util

JSON_DATA_V1 = "combined_data.json"

with open(JSON_DATA_V1) as json_file:
    data =json.load(json_file)

# for our input data schema, we have meme_name as the keys and will construct
# two separate dictionaries. First, a dictionary w/ meme-name and the image
# vectors.  Second, a dictionary with meme-name and list of all the meme-texts.
# and for post-procesing at inference time, we would also need the bounding box
# to return to the frontend.

image_files = list(set([data[i]['url'] for i in range(len(data))]))
meme_names = [filename.split('.')[0] for filename in [file.split('/')[-1] for
    file in image_files]]

# download data if its not there
name_of_zip = 'memefly_images_0.2.zip'
if not os.path.exists(os.path.abspath('.') + '/' + name_of_zip):
    img_zip = tf.keras.utils.get_file(name_of_zip,
                                      cache_subdir=os.path.abspath('.'),
                                      origin="http h3 link",
                                      extract=True)
    PATH = os.path.dirname(img_zip)+'/train/'
else:
    PATH = os.path.abspath('.')+'/train/'

# also download data?
#util.download(meme_names)
def _download_shit(url_list):
    """
    """
    count = 0
    for i in range(len(url_list)):
        r = requests.get(url_list[i], 
                         stream=True, 
                         headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            count += 1
            print(f"downloading {count} image")
            with open(f"{meme_name[i]}.jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    if count == len(url_list):
        print("all images in url_list downloaded")
    pass


meme_name_text_pair = [[data[i]['meme_name'], data[i]['base_meme_text']] for i
    in range(len(data))]

meme_texts = [data[i]['base_meme_text'] for i in range(len(data))]

def calc_max_length(text_list):
    #return max(len(t) for t in text_list)
    return len(max(meme_texts, key=len))






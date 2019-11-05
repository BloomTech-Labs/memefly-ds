class MemeflyDataset:
    def __init__(self, input_json_file: str, img_model: tf.keras.Model, description_file: str, img_features_pkl: str):
        self.json_data = self.__load_json(input_json_file)
        self.description_file = description_file
        self.img_features_pkl = img_features_pkl
        self.img_model = tf.keras.models.load_model(img_model, compile=False)
        self.tokenizer = None
        self.max_length = None
        self.vocab_size = None
        self.text_data = None
        self.img_data = None

        def __load_json(self, path):
            """ Loads json file """
            try:
                with open(path) as robj:
                    data = json.load(robj)
                    return data
            except Exception as e:
                raise e
            
        def preprocess_text(self):
            """         Preprocess input_json and save to instance attributes
            Generates:
            ========
            description_file: meme_name meme_text file, for sanity checking and debugging
            tokenizer: tf.keras tokenizer
            vocab_size: size of the tokenizer, int
            max_length: maximum length of meme text, int
            text_data: list of [meme_name, meme_text] pairs
            """
            print("Preprocessing text ...")
            corpus = []
            meme_data = []
            with open(self.description_file, 'w') as outfile:
                for row in iter(self.json_data):
                    meme_name = row["meme_name"]
                    for meme_text in row["meme_text"]:
                        meme_text = f"startseq {meme_text} endseq\n"
                        #text = f"{meme_name} startseq {meme_text} endseq\n"
                        corpus.append(meme_text.rstrip())#.split(' '))
                        meme_data.append([meme_name, meme_text.rstrip()])
                        outfile.write(f"{meme_name} {meme_text}")#text)
            
            tokenizer = Tokenizer(lower=True)
            tokenizer.fit_on_texts(corpus)
            pickle.dump(tokenizer, open(Config.TOKENIZER, 'wb'))
            self.tokenizer = tokenizer
            self.vocab_size = len(tokenizer.word_index) + 1
            self.text_data = meme_data
            self.max_length = len(max([item[1] for item in meme_data], key=len))
            pass

        def preprocess_img(self):
            """
            Preprocess input_json and save to instance attributes
            Generates:
            ========
            images files: downloaded image file given the urls
            img_features_pkl: pickled dictionary of {meme_name: img_vec file}
            img_data: dictionary of {meme_name: img_vec file}
            """
            print("\nPreprocessing images ...")
            img_urls = [item['meme_url'] for item in self.json_data]
            meme_names = [item['meme_name'] for item in self.json_data]
            self.__download_images(img_urls, meme_names)
            self.img_data = self.__extract_features(meme_names)
            pass
        
        def __download_images(self, url_list: List, meme_name: List):
            """ Download meme images from 'meme_url', skip if already exists """
            print("\nDownloading images ...")
            count = 0
            for i in tqdm(range(len(url_list))):
                filename = f"../datasets/images/{meme_name[i]}.jpg"
                if not pathlib.Path(filename).exists():
                    r = requests.get(url_list[i],
                                     stream=True,
                                     #headers={'User-agent': 'Mozilla/5.0'}
                                     )
                    if r.status_code == 200:
                        count += 1
                        with open(filename, 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)

            if count == len(url_list):
                print("all images in url_list downloaded")
                
            pass
        
        def __extract_features(self, meme_name: list) -> dict:
            """
            Takes a preloaded Tensorflow Keras InceptionV3 Model with embeddings and a list of images
            and return a dict with keys: image_name w/o the .jpg and the values: image embeddings extracted
            using InceptionV3 with global average pooling layer and pretrained imagenet weights.
            """
            print("Creating image embedding vectors ...")
            features = dict()
            for img_file in tqdm(meme_name):
                filename = f"../datasets/images/{img_file}.jpg"
                img = load_img(filename, target_size=(299, 299))
                img = img_to_array(img)
                img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
                img = preprocess_input(img)
                feature = self.img_model.predict(img, verbose=0)

            features[img_file] = feature              
            pickle.dump(features, open(self.img_features_pkl, 'wb'))
            return features

class MemeDataGenerator(tf.keras.utils.Sequence):
    """
    An iterable that returns [batch_size, (images embeddigns, [unrolled input text sequences, text target])].
    Instead of batching over images, we choose to batch over [image, description] pairs because unlike typical
    image captioning tasks that has 3-5 texts per image, we have 180-200 texts per image. Batching over images
    in our case significantly boosted memory cost and we could only batch 1-2 images using AWS p2.xLarge or p3
    This class inherets from tf.keras.utils.Sequences to avoid data redundancy and syncing error.
    https://www.tensorflow.org/api_docs/python/tf/keras/utils/Sequence
    https://keras.io/utils/#sequence
    
    dataset: [meme name, meme text] pairs
    shuffle: If True, shuffles the samples before every epoch
    batch_size: How many images to return in each call
    INPUT:
    ========
    - dataset: list of meme_name and meme_text pairs. [[meme_name, meme_text], [...], ...]
    - img_embds: a pickled dictionary of {meme_name: image embeddings}
    - tokenizer: tf.keras.preprocessing.text.Tokenizer
    - batch_size: batch size
    - max_length: maximum length of words
    - vocab_size: size of the vocaburaries.
    - shuffle: if True, shuffles the dataset between every epoch
    OUTPUT:
    =======
    - outputs list: Usually empty in regular training. But if detection_targets
    is True then the outputs list contains target class_ids, bbox deltas,       
    and masks.
    """
    def __init__(self, dataset, img_embds, tokenizer, batch_size: int, max_length: int, vocab_size: int, shuffle=False):
        self.dataset = dataset
        self.img_embds = img_embds
        self.tokenizer = tokenizer
        self.batch_size = batch_size
        self.max_length = max_length
        self.vocab_size = vocab_size
        self.shuffle = shuffle
        self.on_epoch_end()
        
    def __len__(self):
        """ Number of batches in the Sequence """
        return int(np.floor(len(self.dataset) / self.batch_size))
    
    def __getitem__(self, idx):
        """         
        Generate one batch of data. One element in a batch is a pair of meme_name, meme_text.
        Dataset is indexed using 'indexes' and 'indexes' will be shuffled every epoch if shuffle is True.
        """
        indexes = self.indexes[idx*self.batch_size:(idx+1)*self.batch_size]
        current_data = [self.dataset[i] for i in indexes]
        in_img, in_seq, out_word = self.__generate_data(current_data)
        #         print(in_img.shape, in_seq.shape, out_word.shape)
        return [in_img, in_seq], out_word
    
    def on_epoch_end(self):
        """ Method called at between every epoch """
        self.indexes = np.arange(len(self.dataset))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)
        pass
    
    def __generate_data(self, data_batch):
        """         
        Loop through the batch of data list and generate unrolled sequences of each list of data
        """
        X1, X2, y = list(), list(), list()
        #         print("start ___generate_data")
        for data in data_batch:
            img_embd = self.img_embds[data[0]][0]
            X1_tmp, X2_tmp, y_tmp = self.__create_sequence(img_embd, data[1])
            #             print("after __create_sequence")
            #             print(X1_tmp, X2_tmp, y_tmp)
            #             print(len(X1_tmp), len(X2_tmp), len(y_tmp))
            #             print(np.array(X1_tmp).shape, np.array(X2_tmp).shape, np.array(y_tmp).shape)
            #             X1.append(X1_tmp[0])
            #             X2.append(X2_tmp[0])
            #             y.append(y_tmp[0])
            #             X1.append(X1_tmp)
            #             X2.append(X2_tmp)
            #             y.append(y_tmp)
            X1.extend(X1_tmp)
            X2.extend(X2_tmp)
            y.extend(y_tmp)
            #         print("end__generate_data")
            #         print(len(X1), len(X2), len(y))
            #         print(np.array(X1).shape, np.array(X2).shape, np.array(y).shape)
            return np.array(X1), np.array(X2), np.array(y)
        
    def __create_sequence(self, image, meme_text):
        """         
        Create one sequence of images, input sequences and output text for a single meme_text, e.g.,
        img_vec   input                               output
        ========  ========                            ========
        IMAGE_VEC startseq                            hi
        IMAGE_VEC startseq hi                         this
        IMAGE_VEC startseq hi this                    is
        IMAGE_VEC startseq hi this is                 not
        IMAGE_VEC startseq hi this is not             fun
        IMAGE_VEC startseq hi this is not fun         endseq
        
        Tokenized sequences will be padded from the front, keras default. The output word will be
        one hot encoded w/ keras' to_categorical, and to save memory size, we cast it to float16
        # https://stackoverflow.com/questions/42943291/what-does-keras-io-preprocessing-sequence-pad-sequences-do
        INPUT:
        ========
        image: image vectors
        meme_text:  text to be unrolled into max length length of sequences
        tokenizer:  tokenizer used to convert words to numbers
        OUTPUT:
        ========
        X1:         image vector, list
        X2:         tokenized sequences, padded to max length, list
        y:          next texts, target, list
        """
        X1, X2, y = list(), list(), list()
        seq = self.tokenizer.texts_to_sequences([meme_text])[0]
        #seq = meme_text.split(' ')#self.tokenizer.texts_to_sequences([meme_text])[0]
        for i in range(1, len(seq)):
            in_seq, out_seq = seq[:i], seq[i]
            #             print(in_seq, out_seq)
            in_seq = pad_sequences([in_seq], maxlen=self.max_length)[0]
            out_seq = to_categorical([out_seq], num_classes=self.vocab_size, dtype='float16')[0]
            X1.append(image)
            X2.append(in_seq)
            y.append(out_seq) # bracket or not?
            #         print("__create_sequence")
            #         print(X1, X2, y)
            #         print(np.array(X1).shape, np.array(X2).shape, np.array(y).shape)         
        return X1, X2, y

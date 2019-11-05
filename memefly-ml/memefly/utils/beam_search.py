import heapq
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


class Beam(object):
    # THIS IS A MAX HEAP. Heap is used to pop out the lowest scores and keep the top 'beam_width' scores only
    #For comparison of prefixes, the tuple (prefix_probability, complete_sentence) is used.
    #This is so that if two prefixes have equal probabilities then a complete sentence is preferred over an incomplete one since (0.5, False) < (0.5, True)

    def __init__(self, beam_width):
        self.heap = list()
        self.beam_width = beam_width

    def add(self, prob, complete, prefix):
        heapq.heappush(self.heap, (prob, complete, prefix))
        if len(self.heap) > self.beam_width:
            heapq.heappop(self.heap)

    def __iter__(self):
        return iter(self.heap)

    def __repr__(self):
        return '\n'.join([str(t) for t in self.heap])

def probabilities_function(model: tf.keras.models, tokenizer: tf.keras.preprocessing, img_emb: np.ndarray, sentence, maxlen):
    """
    return probabilitity and word indices.
    """
    sequence = tokenizer.texts_to_sequences([sentence])[0]
    sequence = pad_sequences([sequence], maxlen=max_length)

    next_word_prob = model.predict([img_emb, sequence], verbose=0)
    words = tokenizer.sequences_to_texts([[i] for i in range(len(next_word_prob[0]))])
    return zip(next_word_prob[0], words)

# adopted from https://geekyisawesome.blogspot.com/2016/10/using-beam-search-to-generate-most.html
def beamsearch(probabilities_function, model, tokenizer, img_emb, maxlen=150, beam_width=5):
    prev_beam = Beam(beam_width)
    prev_beam.add(0.0, False, 'startseq')
    while True:
        curr_beam = Beam(beam_width)

        # Add complete sentences that do not yet have the best probability to the current beam, 
        # the rest prepare to add more words to them.
        for (prefix_prob, complete, prefix) in prev_beam:
            if complete == True:
                curr_beam.add(prefix_prob, True, prefix)
            else:
                # Get probability of each possible next word for the incomplete prefix.
                for next_prob, next_word in probabilities_function(model, tokenizer, img_emb, prefix, maxlen):
                    t = len(prefix.split(' '))
                    if next_word == 'endseq':
                        # if next word is the end token then mark prefix as complete and leave out the end token
                        curr_beam.add(prefix_prob + np.log(next_prob+1e-9)/t, True, prefix)
                    else:
                        # if next word is a non-end token then mark prefix as incomplete, and use normalized log prob
                        curr_beam.add(prefix_prob*t/(t+1) + np.log(next_prob+1e-9)/(t+1), False, prefix+' '+next_word)

        (best_prob, best_complete, best_prefix) = max(curr_beam)
        count = sum([item[1] for item in curr_beam])

        # return a random top 5 when we get 5 completed sentences or reach max length.
        if count == 5 or len(best_prefix)-1 == maxlen:
            return np.random.choice([' '.join(item[2].split(' ')[1:]) for item in curr_beam])

        prev_beam = curr_beam

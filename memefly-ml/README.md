# Memefly Machine Learning Engineering

Automatic meme generation model using Tensorflow Keras. 

# Directory Structure:
```
├── README.md
├── assets
├── datasets
├── notebooks
├── memefly
│     ├── datasets
│     ├── models
│     ├── networks
│     ├── tests
│     ├── experiments
│     └── train.py
│                
├── weights
└── requirements.txt
```

# Change log:

2019-12-07 - Han - Added par-inject cnn-rnn model in preparation for attention.
    
2019-11-30 - Han - Added beam search for inferencing.

2019-11-26 - Han - Rewrote training notebook in 06. Wrote new dataset class for data ingestion and preprocessing. Wrote new tf.keras.utils.Sequences generator that generates base on meme image/meme text pairs. Wrote new training script with connection to wandb for experiment tracking. Started to port notebooks into .py files for better experiment tracking and code updates.

2019-11-13 - Han - Refactored API endpoints. Added logging. Testing in progress.

2019-11-07 - Han - Built and tested Docker Image, locally. Reorganized directory structure. Added scripts for building docker images.

2019-11-07 - Han, Hursh, Nick - Built and tested Flask API.

2019-11-05 - Han - started training memefly initial model. 

2019-11-04 - Han - memefly data cleaning and organization in preparation for training.

2019-11-04 - Han - Tested InceptionV3 quantization. Got model size down to 21MB from 84MB but inference time slowed down to 900ms from 200ms. Putting quantization on hold until future discovery.

2019-11-03 - Han - Tested model loading time and inference time. Model loading time is ~9s, might be okay. Inferencing time costs ~5.77s, that is too long and not acceptable. More tests after the first inference, it reduces down to ~400ms per inference. Might be good enough.

2019-10-29 - Han - Fixed data generator for model training. Trained initial model, 2.81 loss.

2019-10-27 - Han - Initial preprocessing steps completed using Flikr8 dataset. Image features pickled and descriptions extracted and stored in the Datasets folder. Initial Keras model setup with InceptionV3 for encoder and simple LSTM for decoder. For some reason dataset is too big to fit into memory (1.6 GB pickled) despite having 16+ GB free memoryData too big to fit into memory for some reason. Data_generator not working.

2019-10-26 - Han - Setup monorepo barebone template structure

# References:

[Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)

[Show and Tell: A Neural Image Caption Generator](https://arxiv.org/abs/1411.4555)

[Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/abs/1502.03044)

[Where to put the Image in an Image CaptionGenerator](https://arxiv.org/abs/1703.09137)

[Dank Learning: GeneratingMemes Using Deep Neural Networks](https://arxiv.org/abs/1806.04510)

[Learning to Evaluate Image Captioning](https://arxiv.org/abs/1806.06422)
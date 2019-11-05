import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np
import click


SAMPLE_IMG = "../datasets/cyber-musk.jpg"

def load_img_to_array(*, imgfile:str) -> np.ndarray:
    img = load_img(imgfile, target_size=(299, 299))
    img = img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = preprocess_input(img)

    return img

def keras_to_tfserving(*, model_name:str, output_dir:str, img:np.ndarray) -> np.ndarray:
    model = tf.keras.models.load_model(model_name, compile=False)
    tf.saved_model.save(model, output_dir)
    features = model.predict(img, verbose=0)

    return features

def test_loaded_model(*, output_dir:str, img:np.ndarray, ref_pred:np.ndarray) -> bool:
    loaded = tf.saved_model.load(output_dir)
    infer_key = list(loaded.signatures.keys())
    infer = loaded.signatures[infer_key[0]]
    print(f'Model output layer: {infer.structured_outputs}')
    # print(f"Reference output: {ref_pred}")
    out = infer(tf.constant(img))['global_average_pooling2d']
    # print(f"Translated output: {out}")

    return np.all(ref_pred == out)

@click.command()
@click.argument('model_file')
@click.argument('output_dir')
@click.argument('ver')
def main(*, model_file:str, output_dir:str, ver:int) -> None:
    img = load_img_to_array(imgfile=SAMPLE_IMG)
    features = keras_to_tfserving(model_name=model_file,
                                  output_dir=output_dir+'/'+ver,
                                  img=img)
    print(features.shape)
    werk = test_loaded_model(output_dir=output_dir+'/'+ver,
                             img=img,
                             ref_pred=features)
    print(f'Converted model output the same: {werk}')


if __name__ == "__main__":
    main()

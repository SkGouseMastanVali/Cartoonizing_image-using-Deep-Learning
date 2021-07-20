from flask import Flask, render_template, request
from model import model_network, model_guided_filter
import os
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from tqdm import tqdm


app = Flask(__name__,static_folder='./uploads')

app.config['UPLOAD_PATH'] = './uploads/normal_images'

@app.route('/')
def home():
    return render_template("index.html")

def resize_crop(image):
    h, w, c = np.shape(image)
    if min(h, w) > 720:
        if h > w:
            h, w = int(720*h/w), 720
        else:
            h, w = 720, int(720*w/h)
    image = cv2.resize(image, (w, h),
                       interpolation=cv2.INTER_AREA)
    h, w = (h//8)*8, (w//8)*8
    image = image[:h, :w, :]
    return image

@app.route('/cartoonize', methods = ['GET', 'POST'])
def cartoonize():
    if request.method == 'POST':
      f = request.files['ifile']
    if f.filename != '':
        f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
    model_path = 'checkpoint'
    load_folder = './uploads/normal_images'
    save_folder = './uploads/cartoonized_images'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    input_photo = tf.placeholder(tf.float32, [1, None, None, 3])
    network_out = model_network.unet_generator(input_photo)
    final_out = model_guided_filter.guided_filter(input_photo, network_out, r=1, eps=5e-3)

    all_vars = tf.trainable_variables()
    gene_vars = [var for var in all_vars if 'generator' in var.name]
    saver = tf.train.Saver(var_list=gene_vars)

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    sess.run(tf.global_variables_initializer())
    saver.restore(sess, tf.train.latest_checkpoint(model_path))
    name_list = os.listdir(load_folder)
    for name in name_list:
        if name == f.filename:
            img = name
            break
    try:
        load_path = os.path.join(load_folder, img)
        save_path = os.path.join(save_folder, img)
        image = cv2.imread(load_path)
        image = resize_crop(image)
        batch_image = image.astype(np.float32)/127.5 - 1
        batch_image = np.expand_dims(batch_image, axis=0)
        output = sess.run(final_out, feed_dict={input_photo: batch_image})
        output = (np.squeeze(output)+1)*127.5
        output = np.clip(output, 0, 255).astype(np.uint8)
        cv2.imwrite(save_path, output)
    except:
        print('cartoonize {} failed.......'.format(img))
    return render_template('index.html', img_name = img)




if __name__ == '__main__':
    app.run(debug = True)

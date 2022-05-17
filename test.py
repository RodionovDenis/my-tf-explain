import tensorflow as tf
import numpy as np

from tf_explain.core.grad_cam import GradCAM
from PIL import Image

# Load pretrained model or your own
model = tf.keras.applications.vgg16.VGG16(weights="imagenet", include_top=True)

# Load a sample image (or multiple ones)
img = tf.keras.preprocessing.image.load_img("images/input_nn/shark.jpg", target_size=(224, 224))
img = tf.keras.preprocessing.image.img_to_array(img)
data = ([img], None)

# Start explainer
explainer = GradCAM()
actual = explainer.explain(data, model, class_index=3)  # 281 is the tabby cat index in ImageNet
# 3 - shark, 180 - dog

explainer.save(actual, '.', 'src/shark.png')

#expected = np.asarray(Image.open('images/output_nn/cat.png'))

#assert np.array_equal(actual, expected), "shit happens!" 

#print("Tests are passed!")

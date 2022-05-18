import tensorflow as tf
import numpy as np

from tf_explain.core.grad_cam import GradCAM
from PIL import Image

# Load pretrained model or your own
model = tf.keras.applications.vgg16.VGG16(weights="imagenet", include_top=True)

examples = {281 : 'cat', 180 : 'dog', 3 : 'shark'}

for key, name in examples.items():
    
    # Load a sample image (or multiple ones)
    img = tf.keras.preprocessing.image.load_img("images/input_nn/" + name + ".jpg", target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    data = ([img], None)

    # Start explainer
    explainer = GradCAM()
    actual = explainer.explain(data, model, class_index=key)

    explainer.save(actual, '.', "src/" + name + ".png")

    expected = np.asarray(Image.open("images/output_nn/" + name + ".png"))

    assert np.array_equal(actual, expected), name + " is wrong"
    
    print(name + " is correct") 

print("Tests are passed!")

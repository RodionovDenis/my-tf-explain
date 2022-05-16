import tensorflow as tf
from tf_explain.core.grad_cam import GradCAM
from PIL import Image
from PIL import ImageChops


# Load pretrained model or your own
model = tf.keras.applications.vgg16.VGG16(weights="imagenet", include_top=True)

# Load a sample image (or multiple ones)
img = tf.keras.preprocessing.image.load_img("images/cat.jpg", target_size=(224, 224))
img = tf.keras.preprocessing.image.img_to_array(img)
data = ([img], None)

# Start explainer
explainer = GradCAM()
grid = explainer.explain(data, model, class_index=281)  # 281 is the tabby cat index in ImageNet

actual = Image.fromarray(grid)
expected = Image.open('images/expected.png')

diff = ImageChops.difference(actual, expected)

assert diff.getbbox() == False, "shit happens!" 

print("Test is passed.")

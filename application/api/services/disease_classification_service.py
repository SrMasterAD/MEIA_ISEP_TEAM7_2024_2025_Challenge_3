import application.api.constants.diseases as diseases
from fastapi import UploadFile
from PIL import Image
from io import BytesIO
import numpy as np
from application.api.constants import diseases
from keras.layers import TFSMLayer
from keras import Sequential

def dummy_tf_op_lambda(x):
    return x


model = Sequential([
    TFSMLayer("application/api/ai_models/cnn_vit_saved_model", call_endpoint="serving_default")
])
class_names = [diseases.BROWN_RUST, diseases.HEALTHY, diseases.MILDEW, diseases.SEPTORIA, diseases.YELLOW_RUST]

async def classify_disease(image: UploadFile):
    image_data = await image.read()
    pil_image = Image.open(BytesIO(image_data)).convert("RGB")
    pil_image = pil_image.resize((256, 256))

    img_array = np.array(pil_image)
    img_array = np.expand_dims(img_array, axis=0)

    outputs = model.predict(img_array)
    output_array = list(outputs.values())[0]
    pred_class = int(np.argmax(output_array))

    return class_names[pred_class]
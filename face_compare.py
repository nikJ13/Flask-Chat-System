import face_recognition
from PIL import Image
import base64
import io
import numpy as np

def comparison(arr,raw_data):
    #print(raw_data)
    decoded = base64.b64decode(raw_data[23:])
    image = Image.open(io.BytesIO(decoded))
    #print(image)
    image_np = np.array(image)
    #print(face_recognition.face_encodings(arr)[0])
    #print(face_recognition.face_encodings(image_np)[0])
    try:
        return face_recognition.compare_faces([face_recognition.face_encodings(arr)[0]],face_recognition.face_encodings(image_np)[0])
    except IndexError:
        return None
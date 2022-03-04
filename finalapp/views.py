from importlib.resources import path
from matplotlib import image
import numpy as np

from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing.image import img_to_array, load_img
from keras.models import load_model
from tensorflow.python.keras.backend import set_session

from .models import Photo
from .forms import PhotoForm

from cloudinary.forms import cl_init_js_callbacks

from io import BytesIO
from PIL import Image
import requests
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']


def loadImage(url):
    response = requests.get(url)
    img_bytes = BytesIO(response.content)
    img = Image.open(img_bytes)
    img = img.convert('RGB')
    img = img.resize((32, 32), Image.NEAREST)
    img = img_to_array(img)
    return img


# Create your views here.
@csrf_exempt
def index(request):

    if request.method == "POST":
        #
        # Form
        #
        form = PhotoForm(request.POST, request.FILES)
        form.save()
        #
        # Cloudinary
        #
        photo = Photo.objects.last()

        #
        # Django image API
        #
        model = load_model('model.h5')
        numpy_array = loadImage(
            Photo.objects.last().image.url)
        image_batch = img_to_array(numpy_array)
        image_batch = np.expand_dims(numpy_array, axis=0)

        result = model.predict(image_batch)
        #
        # Output/Return data
        #
        max = result[0][0]
        images = 0
        for i in range(0, 10):
            if(result[0][i] > max):
                max = result[0][i]
                images = i
        print(result)
        return render(request, "img_page.html", {"predictions": class_names[images], "photo": photo, "form": form})

    else:
        form = PhotoForm()
        return render(request, "index.html", {"form": form})

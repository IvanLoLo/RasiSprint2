from ..models import ContractFile
from datetime import timedelta
from django.utils.dateparse import parse_date
from storages.backends.gcloud import GoogleCloudStorage
from django.core.files.base import ContentFile
import io
import os
import uuid
import shortuuid


storage = GoogleCloudStorage()

def sanitize_filename(filename):
    # Get the file name without the path
    basename = os.path.basename(filename)
    # Remove any potentially harmful characters
    safe_filename = ''.join(e for e in basename if (e.isalnum() or e in ['.', '-', '_']))
    return safe_filename


def create_contract(file):

     try:
        file_data = io.BytesIO(file.read())
        file_data.seek(0)
        target_path = sanitize_filename(shortuuid.uuid() + file.name)
        path = storage.save(target_path, ContentFile(file_data.read()))
        # storage.url(path)
        contractFile = ContractFile.objects.create(fileName='Some Value', publicURI='Some URI')
        return contractFile
     except Exception as e:
        raise Exception(e)


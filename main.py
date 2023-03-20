import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import uuid
import requests
import subprocess

from dotenv import load_dotenv
from fastapi import FastAPI
app = FastAPI()

load_dotenv()

config = cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)


def uploadImage():
    name_of_the_image = uuid.uuid4()
    command = f"fswebcam -r 1280x720 --no-banner {name_of_the_image}.jpeg"
    subprocess.call(command, shell=True)
    cloudinary.uploader.upload(f"{name_of_the_image}.jpeg",
                               public_id=f"{name_of_the_image}", unique_filename=False, overwrite=True)

    srcURL = cloudinary.CloudinaryImage(f"{name_of_the_image}").build_url()
    resp = requests.post(
        "http://13.233.233.124:8000/compare_faces", json={"url": srcURL})
    print(resp.json())

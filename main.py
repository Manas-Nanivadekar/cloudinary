import os
import cloudinary.api
import cloudinary.uploader
import cloudinary
from dotenv import load_dotenv
load_dotenv()

config = cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

print("****1. Set up and configure the SDK:****\nCredentials: ",
      config.cloud_name, config.api_key, "\n")


def uploadImage():

    cloudinary.uploader.upload("test.jpeg",
                               public_id="test_image", unique_filename=False, overwrite=True)

    srcURL = cloudinary.CloudinaryImage("test_image").build_url()

    print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")


uploadImage()

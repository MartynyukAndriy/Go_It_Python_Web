import hashlib

import cloudinary
import cloudinary.uploader

from src.conf.config import settings


class UploadService:
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True
    )

    @staticmethod
    def create_name_avatar(email: str, prefix: str):
        """
        The create_name_avatar function takes an email and a prefix, hashes the email,
        and returns a string of the form 'prefix/name' where name is the first 10 characters
        of the hashed email. This function is used to create unique names for avatars.

        :param email: str: Specify the type of data that is expected to be passed into the function
        :param prefix: str: Specify the directory in which the avatar will be stored
        :return: A string
        :doc-author: Andriy
        """
        name = hashlib.sha256(email.encode()).hexdigest()[:10]
        return f'{prefix}/{name}'

    @staticmethod
    def upload(file, public_id):
        """
        The upload function takes a file and public_id as arguments.
        It then uploads the file to Cloudinary using the public_id provided.
        The function returns a dictionary containing information about the uploaded image.

        :param file: Get the file that is being uploaded
        :param public_id: Specify the name of the file in cloudinary
        :return: A dictionary with the following keys:
        :doc-author: Andriy
        """
        r = cloudinary.uploader.upload(file, public_id=public_id, overwrite=True)
        return r

    @staticmethod
    def get_url_avatar(public_id, version):
        """
        The get_url_avatar function takes in a public_id and version number,
            then returns the url of the avatar image.

        :param public_id: Specify the image to be retrieved from cloudinary
        :param version: Get the image from a specific version
        :return: The url of the avatar image
        :doc-author: Andriy
        """
        src_url = cloudinary.CloudinaryImage(public_id) \
            .build_url(width=250, height=250, crop='fill', version=version)
        return src_url
    
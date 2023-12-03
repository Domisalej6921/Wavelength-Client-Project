import os
import shutil
import datetime

from typing import Union

from data.filesRepository import FilesRepository
from logic.cryptography import Cryptography

class Uploads:
    @staticmethod
    def checkImage(encoding: str) -> tuple[str, str, float]:
        """
        Decode the image and store it in the temp directory, return the UUID, extension and size
        """
        # Decode the image and store it in the temp directory
        UUID, extension = Cryptography.decodeImage(encoding)

        # Open the file in the OS
        # Sourced fileStats and fileStats.st_size from:
        # https://www.digitalocean.com/community/tutorials/how-to-get-file-size-in-python#
        fileStats = os.stat('temp/' + UUID + "." + extension)

        return UUID, extension, fileStats.st_size / (1024 * 1024)

    @staticmethod
    def acceptImage(imageID: str, extension: str) -> None:
        """
        Process the image by storing it in the uploads directory and storing a new record in the database
        """

        # Check that the uploads directory exists, if not create it
        if not os.path.exists("static/uploads/"):
            os.mkdir("static/uploads/")

        # Move the image from the temp directory to the uploads directory
        # Learnt about how to use shutil from:
        # https://stackoverflow.com/questions/8858008/how-do-i-move-a-file-in-python
        shutil.move("temp/" + imageID + "." + extension, "static/uploads/" + imageID + "." + extension)

        # Sourced from: https://www.tutorialspoint.com/how-to-convert-datetime-to-an-integer-in-python
        currentTime = int(datetime.datetime.now().timestamp())

        # Store the image data in the database
        FilesRepository().insert({
            "FileID": imageID,
            "Name": imageID,
            "Extension": extension,
            "Description": "",
            "Created": currentTime
        })

    @staticmethod
    def rejectImage(imageID: str, extension: str) -> None:
        """
        Reject the image by deleting it from the temp directory
        """
        # Delete the image from the temp directory
        os.remove("temp/" + imageID + "." + extension)

    @staticmethod
    def removeImage(imageID: Union[str, None]) -> None:
        """
        Remove the image by deleting it from the uploads directory and database
        """
        # Check if the imageID is None
        if imageID is None:
            return

        # Create a new instance of the FilesRepository class
        filesRepository = FilesRepository()

        # Get the image data from the database
        image = filesRepository.getWithID(imageID)
        try:
            # Delete the image from the uploads directory
            os.remove("static/uploads/" + imageID + "." + image[2])
        except:
            pass

        # Delete the image from the database
        filesRepository.delete(imageID)
import os
import shutil
import datetime

from data.filesRepository import FilesRepository
from cryptography import Cryptography

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
        # Move the image from the temp directory to the uploads directory
        # Learnt about how to use shutil from:
        # https://stackoverflow.com/questions/8858008/how-do-i-move-a-file-in-python
        shutil.move("temp/" + imageID + "." + extension, "uploads/" + imageID + "." + extension)

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

    def rejectImage(imageID: str, extension: str) -> None:
        """
        Reject the image by deleting it from the temp directory
        """
        # Delete the image from the temp directory
        os.remove("temp/" + imageID + "." + extension)
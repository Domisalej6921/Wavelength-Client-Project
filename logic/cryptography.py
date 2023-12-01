import passlib.hash as passlib
import uuid
import base64
import os
import random

class Cryptography:
    @staticmethod
    def digest(text: str) -> str:
        """
        Hash the text using the sha256 algorithm
        """
        return passlib.sha256_crypt.hash(text)

    @staticmethod
    def digestImage(imagePath: str) -> int:
        """
        Hash the image using perceptual hashing
        """
        pass

    @staticmethod
    def createSalt() -> str:
        characters = '1234567890!@£$%=+-_~qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        salt = ''
        for i in range(0, 16):
            salt += random.choice(characters)
        return salt

    @staticmethod
    def verifyPassword(text: str, hashedText: str) -> bool:
        """
        Verify the text matches the hashed text
        """
        if passlib.sha256_crypt.verify(text, hashedText):
            return True
        return False

    @staticmethod
    def createUUID() -> str:
        # Generate a random UUID and remove dashes
        random_uuid = str(uuid.uuid4().hex)

        # Extract the first 16 characters from the UUID
        sixteen_digit_uuid = random_uuid[:16]

        return sixteen_digit_uuid
        
    # Peer programmed method "decodeImage": Tom & Akshay
    @staticmethod
    def decodeImage(self, httpEncoding: str) -> str:
        """
        Decode the image using base64 then store the image in a temporary file, returning the UUID
        """

        # Check that the temp directory exists, if not create it
        if not os.path.exists("temp/"):
            os.mkdir("temp/")

        # Split the encoding into the image type and the image data
        encoding = httpEncoding.split(",")[1]
        extension = httpEncoding.split(";")[0].split("/")[1]
        
        # Convert the encoding to bytes
        image = encoding.encode()

        # Create a UUID for the image name
        imageUUID = self.createUUID()

        # Write the image to a temporary file
        # Used Stackoverflow to help with loading python objects:
        # https://stackoverflow.com/questions/2323128/convert-string-in-base64-to-image-and-save-on-filesystem
        with open(f"temp/{imageUUID}.{extension}", "wb") as file:
            file.write(base64.decodebytes(image))

        # Return the UUID
        return imageUUID

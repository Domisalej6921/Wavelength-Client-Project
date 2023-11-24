import passlib.hash as passlib
import uuid
import random

class Cryptography:
    @staticmethod
    def Digest(text: str) -> str:
        """
        Hash the text using the sha256 algorithm
        """
        return passlib.sha256_crypt.hash(text)

    @staticmethod
    def DigestImage(imagePath: str) -> int:
        """
        Hash the image using perceptual hashing
        """
        pass

    @staticmethod
    def CreateSalt() -> str:
        characters = '1234567890!@£$%=+-_~qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        salt = ''
        for i in range(0, 16):
            salt += random.choice(characters)
        return salt

    @staticmethod
    def VerifyPassword(text: str, hashedText: str) -> bool:
        """
        Verify the text matches the hashed text
        """
        if passlib.sha256_crypt.verify(text, hashedText):
            return True
        return False

    @staticmethod
    def CreateUUID() -> str:
        # Generate a random UUID and remove dashes
        random_uuid = str(uuid.uuid4().hex)

        # Extract the first 16 characters from the UUID
        sixteen_digit_uuid = random_uuid[:16]

        return sixteen_digit_uuid

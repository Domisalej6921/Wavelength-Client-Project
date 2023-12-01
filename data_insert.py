from logic.uploads import *

uploads = Uploads()

img = ""

print(uploads.checkImage(img))

imageID, extension, size = uploads.checkImage(img)

uploads.acceptImage(imageID, extension)
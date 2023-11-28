class FileUploads {
    // Peer programmed method "format": Tom & Akshay
    static async format(file) {
        return new Promise((resolve, reject) => {
            /* Used documentation and examples from:
            https://stackoverflow.com/questions/6150289/how-can-i-convert-an-image-into-base64-string-using-javascript
            https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL */
            const reader = new FileReader();
            reader.onload = function() {
                resolve(reader.result)
            }

            reader.readAsDataURL(file)
        });
    }
}

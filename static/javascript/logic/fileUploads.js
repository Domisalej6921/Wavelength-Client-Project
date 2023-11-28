class FileUploads {
    // Peer programmed method "encodeImage": Tom & Akshay
    static async format(file) {
        
        // Get the file extension
        let extension = file.split(".")[1];
        
        /* Used documentation and examples from:
        https://stackoverflow.com/questions/6150289/how-can-i-convert-an-image-into-base64-string-using-javascript
        https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL */
        var reader = new FileReader();
        reader.onload = function() {
            reader.readAsText(file, "base64");
            print(reader.result)
            return {
                encoding: reader.result,
                extension: extension
            }
        };
    }
}
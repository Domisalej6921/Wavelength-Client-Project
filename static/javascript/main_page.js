const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;

const db = new sqlite3.Database('general.db');

app.get('/image/:fileID', (req, res) => {
    const fileID = req.params.fileID;

    db.get('SELECT fileName, fileData FROM files WHERE fileID = ?', [fileID], (err, row) => {
        if (err) {
            console.error(err.message);
            res.status(500).send('Internal Server Error');
            return;
        }

        res.type('image/jpeg');
        res.send(row.fileData);
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});

const fileID = 1; 
        const imageUrl = `http://localhost:3000/image/${fileID}`;

        document.getElementById('image').src = imageUrl;

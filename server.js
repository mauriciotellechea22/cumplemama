const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the current directory (like the mp3 and any images)
app.use(express.static(__dirname));

// Serve the main HTML file on the root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'cumpleanos_mama.html'));
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

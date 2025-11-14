const express = require('express');
const axios = require('axios');
const app = express();
app.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:8000/cgi-bin/aaa.py');
        const data = response.data;
        const listItems = data.map(item => `<li>${item}</li>`).join('');
        const html = `<h1>case1</h1><ul>${listItems}</ul>`;
        res.send(html);
    } catch (error) {
        res.status(500).send('err: ' + error.message);
    }
});
app.listen(3000, () => console.log('Server running on http://localhost:3000'));

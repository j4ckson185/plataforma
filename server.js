const https = require('https');
const fs = require('fs');
const path = require('path');
const express = require('express');
const selfsigned = require('selfsigned');
const app = express();

const attrs = [{ name: 'commonName', value: 'localhost' }];
const pems = selfsigned.generate(attrs, { days: 365 });

const options = {
    key: pems.private,
    cert: pems.cert
};

app.use(express.static(path.join(__dirname, 'build')));

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

const PORT = process.env.PORT || 3001;

https.createServer(options, app).listen(PORT, () => {
    console.log(`Servidor HTTPS rodando em https://localhost:${PORT}`);
});

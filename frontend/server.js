const http = require('http');
const path = require('path');
const fs = require('fs');

const port = 8080;
const serverRoot = path.resolve(__dirname); // Resolves to /app in your Docker container

const mimeTypes = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.wav': 'audio/wav',
  '.mp4': 'video/mp4',
  '.woff': 'application/font-woff',
  '.ttf': 'application/font-ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.otf': 'application/font-otf',
  '.wasm': 'application/wasm'
};

const server = http.createServer((req, res) => {
  let filePath = req.url === '/' ? 'index.html' : req.url;
  // Remove the leading slash and resolve from serverRoot
  filePath = path.resolve(serverRoot, filePath.slice(1)); 

  // Perform the security check to prevent path traversal
  if (!filePath.startsWith(serverRoot)) {
    res.writeHead(400, { 'Content-Type': 'text/plain' });
    return res.end('400 Bad Request');
  }

  // Determine the content type
  const extname = String(path.extname(filePath)).toLowerCase();
  const contentType = mimeTypes[extname] || 'application/octet-stream';

  // Read the file and send the response
  fs.readFile(filePath, (error, content) => {
    if (error) {
      if (error.code === 'ENOENT') {
        fs.readFile(path.join(serverRoot, 'index.html'), (err, content) => {
          if (err) {
            res.writeHead(500);
            return res.end('500 Internal Server Error');
          } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            return res.end(content, 'utf-8');
          }
        });
      } else {
        res.writeHead(500);
        return res.end('500 Internal Server Error');
      }
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      return res.end(content, 'utf-8');
    }
  });
});

server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

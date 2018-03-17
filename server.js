const coap = require('coap') // or coap
    ,
    server = coap.createServer()

server.on('request', function(req, res) {
    res.end('Hello ' + req.url.split('/')[1] + '\n')
    console.log('got')
})

server.listen(5683, '192.168.1.4', function() {
    console.log('server started on port 5683')
})
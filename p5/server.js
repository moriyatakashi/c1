express = require('express')
app = express()
app.use(express.static(require('path').join(__dirname)))
app.listen(3000, () => { })
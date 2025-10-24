a=require('express');
b=a();
b.use(a.static(__dirname));
b.listen(3000);
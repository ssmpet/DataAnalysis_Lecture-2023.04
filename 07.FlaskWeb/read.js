let fs = require('fs');
let datas = ''
fs.readFile('static/js/famousSaying.txt', 'utf-8', function(err, data){
    console.log(data);
    datas = data
    let says = datas.split('\n')
    console.log('\n\nkim')
    console.log(says[0])
})


console.log('end test')
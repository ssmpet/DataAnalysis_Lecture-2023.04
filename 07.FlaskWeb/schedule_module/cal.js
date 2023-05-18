let today = new Date()

console.log(today)
today.setMonth(today.getMonth() - 1)
console.log(today.getMonth()+1)
console.log(today.getFullYear())
console.log(today.getDate())
day = '20230523'
console.log(Number(day.substring(6)))

desc = '신정 구정'
console.log(desc.indexOf(' '))
if( desc.indexOf(' ') >= 0) {
    console.log(desc.substring(0, desc.indexOf(' ')))
    console.log(desc.substring(desc.indexOf(' ')+1))
}



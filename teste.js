// While
// let i =0
// do {
//     console.log(i)
//     i++
// }while(i<6)

// for
for(let i = 1; i<=500000; i++){
    if(i%3==0 && i%5==0){
        console.log(i + ' Fizz Buzz')
    }

    else if(i%5==0){
        console.log(i + ' Buzz')
    }

    else if(i%3==0){
        console.log(i + ' Fizz')
    }
}
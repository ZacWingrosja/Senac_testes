// verificar se é maior de 18 anos

function maior18(idade){
    let saida = ''
    if(idade>=18)
        saida = 'É maior de idade'
    else
        saida = 'É menor de idade'
    return saida
}

let a = 10
let s = maior18(a)

console.log(s)
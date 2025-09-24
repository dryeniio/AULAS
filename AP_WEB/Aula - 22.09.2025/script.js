function Calcular(){
    let num1 = parseInt(document.querySelector("#num1").value)
    let num2 = parseInt(document.querySelector("#num2").value)
    let num3 = parseInt(document.querySelector("#num2").value)
let soma = num1 + num2 + num3
document.querySelector('#descricao').innerHTML = 'A soma foi:'
document.querySelector("#result").innerHTML = `${soma}`
}

function Calcular_nota(){
    let nota1 = parseFloat(document.querySelector('#num1').value)
    let nota2 = parseFloat(document.querySelector('#num2').value)
    let nota3 = parseFloat(document.querySelector('#num3').value)
    let media = (nota1 + nota2 + nota3)/3
    
    document.querySelector('#descricao').innerHTML = 'Foi aprovado?'

    if (media >= 7){
    document.querySelector('#result').innerHTML = `A média fói: ${media} - APROVADO`
    alert(`APROVADO com média: ${media}`);
    }
    else {
    document.querySelector('#result').innerHTML = `A média fói: ${media} - REPROVADO`
    alert(`REPROVADO com média: ${media}`);
    }
}
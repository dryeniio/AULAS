function salario(){
    let salario = parseFloat(document.querySelector('#salario').value)
    let sal20 = salario + (salario*0.20)
    let sal15 = salario + (salario*0.15)
    let sal10 = salario + (salario*0.10)
    let sal5 = salario + (salario*0.05)

 if (salario <= 280){
    document.querySelector('#result').innerHTML = ''
 }

}
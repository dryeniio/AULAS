function entrar() {
    let email = document.querySelector('#email').value
    let senha = document.querySelector('#senha').value
    
    if (email == 'enio.enrique14@gmail.com' && senha == '123456'){ //TEM QUE TROCAR O OPERADOR LÓGICO
        alert('LOGADO')
        window.location.href = "/questoes.html";
    }
    else{
        alert('DADOS INCORRETOS, Utilizar: enio.enrique14@gmail.com | 123456')
    }
}
function questoes() {
    if (document.querySelector('#quesito') !== null){
    var quesito = parseInt(document.querySelector('#quesito').value)
    }
    else{
        quesito = 0
    }

    let conteudo;
    let divconteudo;
    let textoconteudo;

    switch (quesito){

        case 1:

            conteudo = document.querySelector('#conteudo')
            conteudo.innerHTML = '--------------------------------------------------------'

            divconteudo = document.createElement('Div')
            
            textoconteudo = document.createTextNode('TESTE DE TEXTO QUESITO')
            divconteudo.appendChild(textoconteudo)
            
            conteudo.appendChild(divconteudo)
            document.querySelector('#quesito').remove()
            document.querySelector('h1').innerHTML = 'Questão 1'
            mudarbutao(1)
            break;
        
        case 2:
            document.querySelector('h1').innerHTML = 'Questão 2'

            conteudo = document.querySelector('#conteudo')
            conteudo.innerHTML = '--------------------------------------------------------'

            divconteudo = document.createElement('Div')
            
            textoconteudo = document.createTextNode('TESTE DE TEXTO QUESITO')
            divconteudo.appendChild(textoconteudo)
            
            conteudo.appendChild(divconteudo)
            document.querySelector('#quesito').remove()

            mudarbutao(1)
            break;
        case 3:
            document.querySelector('h1').innerHTML = 'Questão 3'

            conteudo = document.querySelector('#conteudo')
            conteudo.innerHTML = '--------------------------------------------------------'

            divconteudo = document.createElement('Div')
            
            textoconteudo = document.createTextNode('TESTE DE TEXTO QUESITO')
            divconteudo.appendChild(textoconteudo)
            
            conteudo.appendChild(divconteudo)
            document.querySelector('#quesito').remove()

            mudarbutao(1)
            break;
        case 4:
            document.querySelector('h1').innerHTML = 'Questão 4'

            conteudo = document.querySelector('#conteudo')
            conteudo.innerHTML = '--------------------------------------------------------'

            divconteudo = document.createElement('Div')
            
            textoconteudo = document.createTextNode('TESTE DE TEXTO QUESITO')
            divconteudo.appendChild(textoconteudo)
            
            conteudo.appendChild(divconteudo)
            document.querySelector('#quesito').remove()

            mudarbutao(1)
            break;
        case 5:
            document.querySelector('h1').innerHTML = 'Questão 5'

            conteudo = document.querySelector('#conteudo')
            conteudo.innerHTML = '--------------------------------------------------------'

            divconteudo = document.createElement('Div')
            
            textoconteudo = document.createTextNode('TESTE DE TEXTO QUESITO')
            divconteudo.appendChild(textoconteudo)
            
            conteudo.appendChild(divconteudo)
            document.querySelector('#quesito').remove()

            mudarbutao(1)
            break;
        case 6:
            document.querySelector('h1').innerHTML = 'Questão 6'

            conteudo = document.querySelector('#conteudo')
            conteudo.innerHTML = '--------------------------------------------------------'

            divconteudo = document.createElement('Div')
            
            textoconteudo = document.createTextNode('TESTE DE TEXTO QUESITO')
            divconteudo.appendChild(textoconteudo)
            
            conteudo.appendChild(divconteudo)
            document.querySelector('#quesito').remove()

            mudarbutao(1)
            break;
        case 7:
            mudarbutao(1)
            break;
        case 8:
            mudarbutao(1)
            break;
        case 9:
            mudarbutao(1)
            break;
        case 10:
            mudarbutao(1)
            break;
        case 11:
            mudarbutao(1)
            break;
        case 12:
            mudarbutao(1)
            break;
        case 13:
            mudarbutao(1)
            break;
        case 14:
            mudarbutao(1)
            break;
        case 15:
            mudarbutao(1)
            break;
        case 16:
            mudarbutao(1)
            break;
        case 17:
            mudarbutao(1)
            break;
        case 18:
            mudarbutao(1)
            break;
        case 19:
            mudarbutao(1)
            break;
        case 20:
            mudarbutao(1)
            break;
        default:
            mudarbutao(0)
            break;
        }
}
function mudarbutao(mudar){

  let butao = document.getElementById("button")
  
  if (butao.value == "Voltar" /**&& document.getElementById('quesito').value == ''**/)    {
    window.location.href = "/questoes.html"
    }
    if (mudar == 1) {
         butao.value = "Voltar"
    }
        
  

}
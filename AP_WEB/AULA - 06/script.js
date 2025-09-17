// let valor = parseFloat(prompt('Entre com o valor gasto do combst:  (litros)'));
// let distancia = parseFloat(prompt('Entre com a distancia: (quilometros)'));

// function Calcular(valor, distancia){
//     return distancia / valor;
// };

// let resultado = Calcular(valor, distancia);

// alert(`A média de consumo é ${resultado} Km/l.`);


// EXERCICIO 4 --


// let valorProduto = parseFloat(prompt('Digite o valor do produto SEM DESCONTO: '));
// let valorComDescoto = parseFloat(prompt('Digite o valor do produto com desconto: '));

// function calcularDesconto(valorProduto, valorComDescoto) {
//     let desconto = 100* ((valorProduto - valorComDescoto) / valorProduto);
//     let valor_desconto = valorProduto - valorComDescoto;
//     return [desconto, valor_desconto];
// };

// let resultado = calcularDesconto(valorProduto, valorComDescoto);


// alert(`O desconto foi de ${resultado[0].toFixed(2)}% || R$ ${resultado[1].toFixed(2)}.`);


// EXERCICIO 10

let nome = prompt('Insira seu nome:');
let peso = parseFloat(prompt(`Insira seu peso em Kg: `));
let idade = parseInt(prompt(`Digite sua Idade: `));
let altura = parseFloat(prompt(`Digite sua altura: `));

function imc(altura, peso){
    return peso / (altura*altura);
};

let imc = imc(peso, altura);

alert(`Seu nome: ${nome}`)
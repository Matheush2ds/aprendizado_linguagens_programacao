const verdade = true;

// let tem escopo de bloco {...bloco}
// Var só tem escopo de função

let nome = 'Matheus';
const nome2 = 'Matheus';

var nome2 = 'Fulano';

if (verdadeiro) {
    let nome = 'Fulano'; // criando
    var nome = 'Rogerio'; // redeclarando
    

    if (verdadeiro) {
        const nome = 'Robson'; //redeclarando
        console.log(nome,nome2);
    }
}
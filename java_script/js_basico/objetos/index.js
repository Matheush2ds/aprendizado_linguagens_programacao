const pessoa = {
    nome : 'Matheus',
    sobrenome : 'Santos',
    idade : 22,
    endereco : {
        rua : 'Av. Brasil',
        cidade : 'Juiz de Fora',
        estado : 'MG'
    }
};

const { nome: n = 'Fulano', sobrenome } = pessoa;
consolete.log(endereco);
// Espera o carregamento completo do documento HTML antes de executar o código
document.addEventListener('DOMContentLoaded', function () {
    // Seleciona os elementos HTML onde o resultado e expressões vão aparecer
    const display = document.getElementById('calculator-display');
    const resultadoFinalInput = document.getElementById('resultado-final');
    const expressaoDigitadaInput = document.getElementById('expressao-digitada');

    // Variável que armazena a expressão matemática que o usuário digita
    let expression = '';

    // Atualiza o visor da calculadora com o valor atual ou '0' se vazio
    const updateDisplay = (value) => {
        display.textContent = value || '0';
    };

    // Substitui os símbolos visuais por operadores JavaScript para poder calcular
    const sanitizeExpression = (expr) => {
        return expr.replace(/×/g, '*').replace(/÷/g, '/');
    };

    // Função que tenta calcular a expressão digitada
    const calculateResult = () => {
        try {
            const sanitized = sanitizeExpression(expression); // Limpa a expressão
            const result = eval(sanitized); // Calcula usando eval
            expression = String(result); // Atualiza a expressão com o resultado
            updateDisplay(expression); // Mostra o resultado no visor

            // Também atualiza os campos ocultos com o resultado e expressão usada
            resultadoFinalInput.value = expression;
            expressaoDigitadaInput.value = sanitized;
        } catch (error) {
            // Se der erro no cálculo, exibe 'Erro' e limpa os campos
            updateDisplay('Erro');
            resultadoFinalInput.value = '';
            expressaoDigitadaInput.value = expression;
            expression = '';
        }
    };

    // Seleciona todos os botões, exceto o botão com a classe "sair"
    const buttons = document.querySelectorAll('button:not(.sair)');

    // Adiciona um evento de clique para cada botão
    buttons.forEach(button => {
        button.addEventListener('click', (event) => {
            const value = button.textContent; // Pega o texto do botão

            // Se for botão de "=", chama função que calcula a expressão
            if (button.type === 'submit' && value === '=') {
                calculateResult();
                return;
            }

            // Impede que outros botões enviem o formulário
            event.preventDefault();

            // Limpa a expressão se clicar em "C"
            if (value === 'C') {
                expression = '';
                updateDisplay('');
            }
            // Alterna o sinal do último número se clicar em "±"
            else if (value === '±') {
                const match = expression.match(/(-?\d+)(?!.*\d)/); // Último número
                if (match) {
                    const num = match[0];
                    const toggled = String(-parseFloat(num));
                    expression = expression.slice(0, -num.length) + toggled;
                }
                updateDisplay(expression);
            }
            // Transforma o último número em porcentagem se clicar em "%"
            else if (value === '%') {
                const match = expression.match(/(\d+)(?!.*\d)/); // Último número
                if (match) {
                    const num = match[0];
                    const percent = String(parseFloat(num) / 100);
                    expression = expression.slice(0, -num.length) + percent;
                }
                updateDisplay(expression);
            }
            // Adiciona o valor do botão à expressão
            else {
                expression += value;
                updateDisplay(expression);
            }
        });
    });
});
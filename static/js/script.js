document.addEventListener('DOMContentLoaded', function () {
    const display = document.getElementById('calculator-display');
    const resultadoFinalInput = document.getElementById('resultado-final');
    const expressaoDigitadaInput = document.getElementById('expressao-digitada');
    let expression = '';

    const updateDisplay = (value) => {
        display.textContent = value || '0';
    };

    const sanitizeExpression = (expr) => {
        return expr.replace(/×/g, '*').replace(/÷/g, '/');
    };

    const calculateResult = () => {
        try {
            const sanitized = sanitizeExpression(expression);
            const result = eval(sanitized);
            expression = String(result);
            updateDisplay(expression);

            resultadoFinalInput.value = expression;
            expressaoDigitadaInput.value = sanitized;
        } catch (error) {
            updateDisplay('Erro');
            resultadoFinalInput.value = '';
            expressaoDigitadaInput.value = expression;
            expression = '';
        }
    };

    // 🔎 Seleciona todos os botões, menos o que tem class "sair"
    const buttons = document.querySelectorAll('button:not(.sair)');

    buttons.forEach(button => {
        button.addEventListener('click', (event) => {
            const value = button.textContent;

            // "=" calcula e permite submit
            if (button.type === 'submit' && value === '=') {
                calculateResult();
                return;
            }

            // Impede o envio de outros botões
            event.preventDefault();

            if (value === 'C') {
                expression = '';
                updateDisplay('');
            } else if (value === '±') {
                const match = expression.match(/(-?\d+)(?!.*\d)/);
                if (match) {
                    const num = match[0];
                    const toggled = String(-parseFloat(num));
                    expression = expression.slice(0, -num.length) + toggled;
                }
                updateDisplay(expression);
            } else if (value === '%') {
                const match = expression.match(/(\d+)(?!.*\d)/);
                if (match) {
                    const num = match[0];
                    const percent = String(parseFloat(num) / 100);
                    expression = expression.slice(0, -num.length) + percent;
                }
                updateDisplay(expression);
            } else {
                expression += value;
                updateDisplay(expression);
            }
        });
    });
});
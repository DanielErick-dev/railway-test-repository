const CPF_LENGTH = 14; 
const PHONE_LENGTH = 14; 

/**
 * Aplica máscara de CPF (999.999.999-99)
 * @param {HTMLInputElement} input - Elemento de input
 */
function applyCpfMask(input) {
    input.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length > 0) value = value.replace(/^(\d{3})/, '$1.');
        if (value.length > 7) value = value.replace(/^(\d{3}\.\d{3})/, '$1.');
        if (value.length > 11) value = value.replace(/^(\d{3}\.\d{3}\.\d{3})/, '$1-');
        e.target.value = value.substring(0, CPF_LENGTH);
    });

    input.addEventListener('blur', function(e) {
        const digitCount = e.target.value.replace(/\D/g, '').length;
        if (digitCount === 11) {
            input.classList.remove('is-invalid');
        } else {
            input.classList.add('is-invalid');
        }
    });
}

/**
 * Aplica máscara de telefone ((99) 99999-9999)
 * @param {HTMLInputElement} input - Elemento de input
 */
function applyPhoneMask(input) {
    input.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        
        
        let formatted = '';
        if (value.length > 0) {
            formatted = `(${value.substring(0, 2)}`; 
        }
        if (value.length > 2) {
            formatted += `) ${value.substring(2, 7)}`; 
        }
        if (value.length > 7) {
            formatted += `-${value.substring(7, 11)}`; 
        }
        
        e.target.value = formatted.substring(0, 15);
    });
    input.addEventListener('blur', function(e) {
        const digitCount = e.target.value.replace(/\D/g, '').length;
        if (digitCount === 11) {
            input.classList.remove('is-invalid');
        } else {
            input.classList.add('is-invalid');
        }
    });
}

function initMasks() {
    document.querySelectorAll('.mask-cpf').forEach(applyCpfMask);
    document.querySelectorAll('.mask-phone').forEach(applyPhoneMask);
}


function formatDisplayedData() {
    const cpfElement = document.querySelector('#formatted-cpf'); 
    const phoneElement = document.querySelector('#formatted-phone'); 
    if (cpfElement) {
        const fullText = cpfElement.textContent;
        const digits = fullText.replace(/\D/g, '');
        if (digits.length === 11) {
            cpfElement.textContent = `CPF: ${digits.substring(0, 3)}.${digits.substring(3, 6)}.${digits.substring(6, 9)}-${digits.substring(9)}`;
        }
    }
    if (phoneElement) {
        const fullText = phoneElement.textContent;
        const digits = fullText.replace(/\D/g, '');
        if (digits.length === 11) {
            phoneElement.innerHTML = `
                <span class="text-gray-400 block">Número de Telefone:</span>
                <span class="break-all font-medium">${`(${digits.substring(0, 2)}) ${digits.substring(2, 7)}-${digits.substring(7)}`}</span>
            `;
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    formatDisplayedData();
    document.querySelectorAll('.mask-cpf').forEach(applyCpfMask);
    document.querySelectorAll('.mask-phone').forEach(applyPhoneMask);
});
// static/js/script.js
document.addEventListener('DOMContentLoaded', function () {
    const cpfInput = document.getElementById('id_cpf');
    const telefoneInput = document.getElementById('id_telefone');

    if (cpfInput) {
        cpfInput.addEventListener('input', function () {
            this.value = maskCPF(this.value);
        });
    }

    if (telefoneInput) {
        telefoneInput.addEventListener('input', function () {
            this.value = maskTelefone(this.value);
        });
    }
});

function maskCPF(value) {
    return value
        .replace(/\D/g, '')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})$/, '$1-$2')
        .substring(0, 14); // Limita o tamanho
}

function maskTelefone(value) {
    return value
        .replace(/\D/g, '')
        .replace(/(\d{2})(\d)/, '($1) $2')
        .replace(/(\d{5})(\d)/, '$1-$2')
        .substring(0, 15);
}
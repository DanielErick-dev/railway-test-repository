window.confirmAtualize = (event, href, name, lastname, sexo) => {
    event.preventDefault();

    Swal.fire({
        title: "Você tem certeza?",
        text: sexo === 'M'
            ? `Deseja atualizar o pagamento do aluno ${name} ${lastname}?`
            : `Deseja atualizar o pagamento da aluna ${name} ${lastname}?`,
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#22c55e",
        cancelButtonColor: "#334155",
        confirmButtonText: "Sim, Atualizar",
        background: '#1e293b',
        color: '#f1f5f9'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Atualizado",
                text: sexo === 'M'
                    ? `Pagamento do aluno ${name} realizado com sucesso`
                    : `Pagamento da aluna ${name} realizado com sucesso`,
                icon: "success",
                background: '#1e293b',
                color: '#f1f5f9',
                confirmButtonColor: "#22c55e"
            });

            setTimeout(() => {
                window.location.href = href;
            }, 2000);
        }
    });
};

function getCSRFToken(){
    const cookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';

}

function showToast(message, icon){
    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: icon,
        title: message,
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true,
    });
}
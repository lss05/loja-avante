function StatusLogado(logado,ancora_entrarsair,ancora_criarconta,desviourl) {
    console.log(logado)
    console.log(desviourl)
    if (logado==1) {
        ancora_entrarsair.innerText = 'Sair'
        ancora_criarconta.innerText = 'Área do cliente'
        ancora_criarconta.href = desviourl

    }else {
        ancora_entrarsair.innerText = 'Entrar'
        ancora_criarconta.innerText = 'Criar Conta'
        ancora_criarconta.href = desviourl
    }
}

/*let ancora = logado==true?'Sair':'Entrar'
    ancora_entrarsair.innerText = ancora */

function path_image(path){
    console.log(path)
}

function prepara_image(img) {
    console.log(img)
    return 'imagefoto'
}

function pegajson(value){
    console.log(value)
}
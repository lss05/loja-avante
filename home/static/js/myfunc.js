function StatusLogado(data,ancora_entrarsair,ancora_criarconta) {
    console.log(data)
    console.log(ancora_entrarsair.innerText)

    let ancora = data==true?'Sair':'Entrar'

    ancora_entrarsair.innerText = ancora
    
}
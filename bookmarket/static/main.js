function textChangeSubmit() {
    const forms = document.getElementsByClassName('search-form')
    for (let i = 0; i < forms.length; i++) {
        forms[i].addEventListener('submit', e => {
            const elements = document.getElementsByClassName('search-title')
            for (let j = 0; j < elements.length; j++) {
                elements[j].innerHTML = "Got it! Give us a moment..."
            }
        })
    }
}
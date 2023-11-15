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

async function updateFavourite(loop_index) {
    id = "fav-button".concat(loop_index)
    isbn = document.getElementById(id).value;
    const update = await fetch("/updateFavourite?book="+isbn)
}

async function renderFavourites(loop_index) {
    heart_icon = "#heart-icon";
    selector = heart_icon.concat(loop_index);
    var element = document.querySelector(selector);
    if (element.classList.contains("fa-heart-o")) {
        element.classList.replace("fa-heart-o", "fa-heart");
    }
    else if (element.classList.contains("fa-heart")) {
        element.classList.replace("fa-heart", "fa-heart-o");
    }
    common_id = "fav-button"
    id = common_id.concat(loop_index)
    isbn = document.getElementById(id).value;
    const favourite = await fetch("/renderFavourite?book="+isbn);
}
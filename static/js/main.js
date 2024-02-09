function showAccount(){
    let account = document.getElementsByClassName("header__user__account__dropdown")[0]

    if(window.getComputedStyle(account).display === 'block'){
        account.style.display = 'none'
    } else{
        account.style.display = 'block'
    }
}



function showMenu(){
    let menu = document.getElementsByClassName("header__navbarMobile__dropdown")[0]
    let pageContainer = document.querySelector(".pageContainer")
    let header = document.querySelector(".header__content")
    let body = document.body

    if(window.getComputedStyle(menu).display === 'block'){
        menu.style.display = 'none'
        pageContainer.style.display = ''
        header.style.position = 'fixed'
        body.style.paddingTop = "80px";
    } else{
        menu.style.display = 'block'
        pageContainer.style.display = 'none'
        header.style.position = 'static'
        body.style.paddingTop = "0px";
    }
}

function showKatalog(){
    let katalog = document.getElementById("katalogSublinks") 
    let arrow_close = document.getElementsByClassName("arrow_close")[0]
    let arrow_open = document.getElementsByClassName("arrow_open")[0]
    
    if(window.getComputedStyle(katalog).display === 'none'){
        katalog.style.display = 'block'
        arrow_open.style.display = 'inline'
        arrow_close.style.display = 'none'
    } else{
        katalog.style.display = 'none'
        arrow_open.style.display = 'none'
        arrow_close.style.display = 'inline'
    }
}

function showSpolecznosc(){
    let spolecznosc = document.getElementById("spolecznoscSublinks") 
    let arrow_close = document.getElementsByClassName("arrow_close")[1]
    let arrow_open = document.getElementsByClassName("arrow_open")[1]
    
    if(window.getComputedStyle(spolecznosc).display === 'none'){
        spolecznosc.style.display = 'block'
        arrow_open.style.display = 'inline'
        arrow_close.style.display = 'none'
    } else{
        spolecznosc.style.display = 'none'
        arrow_open.style.display = 'none'
        arrow_close.style.display = 'inline'
    }

}

function toggleGenres(label) {
    const category = label.parentElement;
    const genresList = category.querySelector('ul.bookcategory__genres');
    const arrow = category.querySelector('.arrow');

    if (genresList.style.display === 'none' || genresList.style.display === '') {
        genresList.style.display = 'block';
        arrow.style.color = "red";
        arrow.style.transform = "rotate(90deg)";
    } else {
        genresList.style.display = 'none';
        arrow.style.transform = "rotate(0deg)";
        arrow.style.color = "#ffda1d";
    }
}

function showFilters(){
    filters__button = document.querySelector(".filters__mobile")
    filters__exit = document.querySelector(".filters__mobile--exit")
    filters = document.querySelector(".filters__content")

    if (filters.style.display === 'none' || filters.style.display === ''){
        filters.style.display = 'block';
        filters__exit.style.display = 'block';
        filters.style.position = 'absolute';
        filters.style.top = '0';
    }

}

function hideFilters(){
    filters__button = document.querySelector(".filters__mobile")
    filters__exit = document.querySelector(".filters__mobile--exit")
    filters = document.querySelector(".filters__content")

    if (filters.style.display === 'block'){
        filters.style.display = '';
        filters.style.position = '';
        filters.style.top = '';
        filters__exit.style.display = 'none';
    }
}

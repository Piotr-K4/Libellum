function toggleMenu(){
    let mobileMenu = document.querySelector(".mobile-menu")
    let searchBox = document.querySelector(".header__menu-button--search")
    mobileMenu.classList.toggle("mobile-menu--is-active")
    searchBox.toggleAttribute("disabled")
}

function toggleSearchInput(){
    let searchBox = document.querySelector(".wrapper-search--mobile")
    searchBox.classList.toggle("wrapper-search--mobile-is-active")
}

// function toggleMenuLinks(option){
//     option.firstElementChild.classList.toggle("mobile-menu__option--button-is-active")
//     option.parentElement.nextElementSibling.classList.toggle("mobile-menu__links-is-active")
// }

function toggleMenuLinks(option) {
    const arrowIcon = option.firstElementChild;
    const menuLinks = option.parentElement.nextElementSibling;

    arrowIcon.classList.toggle("mobile-menu__option--button-is-active");

    if (arrowIcon.classList.contains("mobile-menu__option--button-is-active")) {
        arrowIcon.style.transition = "transform 0.2s ease-in-out";
        arrowIcon.style.transform = "rotate(90deg)";
        setTimeout(() => {
            menuLinks.classList.toggle("mobile-menu__links-is-active");
        }, 0);
    } else {
        arrowIcon.style.transition = "transform 0.2s ease-in-out";
        arrowIcon.style.transform = "rotate(0deg)";
        setTimeout(() => {
            menuLinks.classList.toggle("mobile-menu__links-is-active");
        }, 0);
    }
}


function toggleFilterItems(option){
    const arrowIcon = option.firstElementChild
    const filterItems = option.nextElementSibling

    console.log(option)

    filterItems.classList.toggle("filters__items--is-active");
    option.classList.toggle("filters__option-button--is-active")
    
    if(filterItems.classList.contains("filters__items--is-active")){
        arrowIcon.style.transition = "transform 0.1s ease-in-out";
        arrowIcon.style.transform = "rotate(90deg)";
    } else {
        arrowIcon.style.transition = "transform 0.1s ease-in-out";
        arrowIcon.style.transform = "rotate(0deg)";
    }
}


function toggleMobileFilters(){
    const mobileFilters = document.querySelector(".mobile-filters")
    mobileFilters.classList.toggle("mobile-filters--is-active")


    if(document.body.style.overflowY === ""){
        document.body.style.overflowY = "hidden" 
    } else {
        document.body.style.overflowY = "" 
    }
}


function toggleMobileUser(option){
    const mobileUser = document.querySelector(".userOptionsMobile");
    const desktopUser = document.querySelector(".userOptions");
    const arrowIcon = option.lastChild

    if(option.classList.contains("header__menu-button--mobile")){
        mobileUser.classList.toggle("userOptionsMobile--active")
        if(mobileUser.classList.contains("userOptionsMobile--active")){
            arrowIcon.style.transition = "transform 0.1s ease-in-out";
            arrowIcon.style.transform = "rotate(90deg)";
        } else {
            arrowIcon.style.transition = "transform 0.1s ease-in-out";
            arrowIcon.style.transform = "rotate(0deg)";
        }
    } else{
        desktopUser.classList.toggle("userOptions--active")
        if(desktopUser.classList.contains("userOptions--active")){
            arrowIcon.style.transition = "transform 0.1s ease-in-out";
            arrowIcon.style.transform = "rotate(90deg)";
        } else {
            arrowIcon.style.transition = "transform 0.1s ease-in-out";
            arrowIcon.style.transform = "rotate(0deg)";
        }
    }
    
}


window.addEventListener("resize", () => {
    if ( document.querySelector(".mobile-menu").className === "mobile-menu mobile-menu--is-active"){
        if(window.innerWidth >= 992){
            toggleMenu();
        }
    }

    if ( document.querySelector(".wrapper-search--mobile").className === "wrapper-search--mobile wrapper-search--mobile-is-active"){
        if(window.innerWidth >= 992){
            toggleSearchInput();
        }
    }
}
)










//Скрываем и показываем элемент header на странице
function userActions() {
    let el = document.getElementsByClassName("header-avatar-menu");
    for(let i = 0; i < el.length; i++) {
        if (el[i].style.display == 'block')
            el[i].style.display = 'none';
        else
            el[i].style.display = 'block';
    }
}
//Скрываем и показываем элементы добавления на addinfo
function categoryActions(select) {
    let elem = document.getElementsByClassName("add-info-category");
    for (let i = 0; i < elem.length; i++) {
        if (select.value == '0') {
            document.getElementsByClassName("add-date")[i].style.visibility = 'hidden';
            document.getElementsByClassName("add-subject")[i].style.visibility = 'hidden';
            document.getElementsByClassName("add-text")[i].style.visibility = 'hidden';
            document.getElementsByClassName("add-sending")[i].style.visibility = 'hidden';
        }
        else if (select.value == '1') {
            document.getElementsByClassName("add-date")[i].style.visibility = 'visible';
            document.getElementsByClassName("add-text")[i].style.visibility = 'visible';
            document.getElementsByClassName("add-sending")[i].style.visibility = 'visible';

            document.getElementsByClassName("add-subject")[i].style.visibility = 'hidden';
        }
        else if (select.value == '2') {
            document.getElementsByClassName("add-date")[i].style.visibility = 'visible';
            document.getElementsByClassName("add-subject")[i].style.visibility = 'visible';
            document.getElementsByClassName("add-text")[i].style.visibility = 'visible';
            document.getElementsByClassName("add-sending")[i].style.visibility = 'visible';
        }
    }
}
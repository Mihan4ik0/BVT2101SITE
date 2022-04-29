var selectItem;

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

//Скрываем и показываем элементы добавления на add_information.html
function categoryActions(select) {
    let elem = document.getElementsByClassName("add-info-category");
    window.selectItem = select.value;
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

//Показываем нужный цвет какой-либо пары
let sType = document.getElementsByClassName("schedule-type");
for (let i = 0; i < sType.length; i++) {
    if (sType[i].innerHTML == 'лек')
        sType[i].style.color = '#0f0';
    else if (sType[i].innerHTML == 'пр')
        sType[i].style.color = '#f66';
    else if (sType[i].innerHTML == 'лаб')
        sType[i].style.color = '#39f';
}

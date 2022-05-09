class addNews {
    /*Переделать конструктор и оставить только присвоение. Объект в роутах*/
    constructor () {
        this.elem = document.getElementById('news-list');
        this.groupNews = [{
                            id: "1",
                            date: "22.04.2022",
                            info: "18.05 будут проставляться зачеты!"
                            }, {
                            id: "2",
                            date: "20.04.2022",
                            info: "Просьба от С.М. Фроловичева подключиться в 17.00"
                            }, {
                            id: "3",
                            date: "19.04.2022",
                            info: "12.05 контрольная по английскому"
                            }, {
                            id: "4",
                            date: "17.04.2022",
                            info: "Физра будет 3 парой на улице"
                            }, {
                            id: "5",
                            date: "10.04.2022",
                            info: "Пересдать ВТ можно 11.04. в 15 в 223 каб."
                            },
                        ];
        this.listNews = this.listNews.bind(this);
        this.getTemplate = this.getTemplate.bind(this);
        this.listNews();
    }
    /*
    * Перебор списка новостей
    */
    listNews() {
        for (let i = 0; i < this.groupNews.length; i++){
            this.getTemplate(this.groupNews[i], this.elem);
        }
    }
    /*
    * Заполнение шаблона новостей в list-news
    */
    getTemplate(add_n, add_id) {
        this.tmp = `<div class="news-box" id="${add_n.id}">
				        <p class="news-box-date">${add_n.date}</p>
				        <p class="news-box-text">${add_n.info}</p>
			        </div>`

        this.elem.insertAdjacentHTML('beforebegin', this.tmp);
    }
}

let addnews = new addNews();




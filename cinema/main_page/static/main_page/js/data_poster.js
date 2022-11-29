    const lang = navigator.language; // определяет язык браузера
    let date = new Date(); // создание нового объекта с текущей датой и временем

    let dayNumber = date.getDate(); // получение даты
    if (dayNumber < 10){
        dayNumber = '0' + dayNumber
    }

    let month = date.getMonth(); // получение месяца
    let dayName = date.toLocaleString(lang,{weekday: 'long' }); // получения названия дня недели

    let monthName = date.toLocaleString(lang,{ month: 'long' }); // получение названия месяца
    let mounthes = ['Cічня', 'Лютого', 'Березня', 'Квітня', 'Травня', 'Червня', 'Липня', 'Серпня', 'Вересня', 'Жовтня', 'Листопада', 'Грудня'];
    let result = mounthes[month];

    var date_result =" " + dayNumber + " " + result + "," + dayName

    document.getElementById('date_result').innerText += date_result


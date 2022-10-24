const labels = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec"
];

const data = {
  labels: labels,
  datasets: [
    {
      label: "Сеанси(Всі користувачі)",
      // backgroundColor: "rgb(255, 99, 132)",
      borderColor: "rgb(255, 99, 132)",
      data: [0, 10, 5, 2, 20, 30, 17, 20, 22, 30, 28, 45]
    },
    {
      label: "Сеанси(Трафік планшетних і звичайних ПК)",
      // backgroundColor: "rgb(34,152,167)",
      borderColor: "rgb(34,152,167)",
      data: [0, 8, 15, 22, 10, 15, 18, 25, 26, 35, 37, 49]
    },
      {
      label: "Сеанси(Трафік з мобільних пристроїв)",
      // backgroundColor: "rgb(255, 99, 132)",
      borderColor: "rgb(255, 128, 0)",
      data: [0, 5, 5, 10, 20, 30, 17, 20, 25, 36, 21, 50]
    },
      {
      label: "Сеанси(Трафік смартфонів і планшетних ПК)",
      // backgroundColor: "rgb(255, 99, 132)",
      borderColor: "rgb(38, 139, 8)",
      data: [0, 10, 5, 20, 50, 10, 3, 13, 14, 23, 21, 12]
    },


  ]
};

const config = {
  type: "line",
  data: data,
  options: {}
};

const myChart = new Chart(document.getElementById("myChart"), config);


//CHART


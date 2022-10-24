var oilCanvas = document.getElementById("oilChart");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var oilData = {
    labels: [
        "Chrome",
        "Opera",
        "FireFox",
        "InternetExplore",
        "Brave"
    ],
    datasets: [
        {
            data: [133.3, 86.2, 52.2, 51.2, 50.2],
            backgroundColor: [
                "#FF6384",
                "#63FF84",
                "#84FF63",
                "#8463FF",
                "#6384FF"
            ]
        }]
};

var pieChart = new Chart(oilCanvas, {
  type: 'pie',
  data: oilData
});


// Chart.js scripts///////////////////////////////////////////////////////////



// var config = {
//     // The type of chart we want to create
//     type: 'line',
//
//     // The data for our dataset
//     data: {
//         labels: ["Year 1","Year 2","Year 3","Year 4","Year 5","Year 6","Year 7","Year 8","Year 9","Year 10"],
//         datasets: [{
//             label: "Propane",
//             borderColor: '#609DD3',
//             fill: false,
//             data: [0, 10, 5, 2, 20, 30, 45],
//         },
//         {
//             label: "Electric",
//             borderColor: '#A5A5A5',
//             fill: false,
//             data: [0, 8, 4, 6, 5, 18, 60],
//         }]
//     },
//
//     // Configuration options go here
//     options: {}
// };
//
// window.onload = function (){
//     var ctx = document.getElementById('myLineChart').getContext('2d');
//     window.myLineChart = chart = new Chart(ctx, config)
// }


//     function loadJson(selector) {
//   return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
// }
//
// var m = new Date();
// var dateString =
//     ("0" + (m.getUTCMonth()+1)).slice(-2) + "/" +
//     ("0" + m.getUTCDate()).slice(-2)
//
//
//
//
// var jsonFilm = loadJson('#jsonFilm');
//
// var poster = jsonFilm.map((item) => item.poster);
// var inawhile = jsonFilm.map((item) => item.while);
//
//
//
// new Chart(document.getElementById("myLineChart"), {
//     type: 'bar',
//   tooltipTemplate: "<%= datasetLabel %> - <%= value.toLocaleString() %>",
//     data: {
//       labels: [dateString, ],
//       datasets: [
//         {
//           label: "Poster",
//           backgroundColor: "#3e95cd",
//           data: [poster, ]
//         }, {
//           label: "InaWhile",
//           backgroundColor: "#8e5ea2",
//           data: [inawhile, ]
//         }
//       ]
//     },
//     options: {
//       tooltips: {
// 			  callbacks: {
// 					label: function(tooltipItem, data) {
// 						var value = data.datasets[0].data[tooltipItem.index];
// 						value = value.toString();
// 						value = value.split(/(?=(?:...)*$)/);
// 						value = value.join(',');
// 						return value;
// 					}
// 			  } // end callbacks:
// 			}, //end tooltips
//
//     }
// });


    function loadJson(selector) {
  return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}


  var jsonData = loadJson('#jsonFilm');

  var data = jsonData.map((item) => item.poster);
  var date = jsonData.map((item) => item.while);

    new Chart (document.getElementById("mybarChart"), {
        type: 'bar',
        data: {
            labels: ['1'],
            datasets: [{
                label: 'Poster',
                backgroundColor: "#000080",
                data: [data[0]]
            }, {
                label: 'While',
                backgroundColor: "#d3d3d3",
                data: [date[0]]
            },]
        },

        options: {
            legend: {
                display: true,
                position: 'top',
                labels: {
                    fontColor: "#000080",
                }
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

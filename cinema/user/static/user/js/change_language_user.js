var defaultLanguage = "english";
var jsonUrl = "https://jsonbin.org/krmfla/language/";
var barEl = document.getElementById("switchLanguageBar");

getData(defaultLanguage);
barEl.addEventListener("click", handleLanguage);

//=== function kits ===
function getData(language) {
  var url = jsonUrl + language;
  $('.content p').fadeOut();
  $.getJSON(url, function(data) {
    renderView(data);
  });
}

function renderView(data) {
  var titleEl = document.getElementById("title");
  var descriptionEl = document.getElementById("description");
  titleEl.innerText = data.title;
  descriptionEl.innerText = data.description;
  $('.content p').fadeIn();
}

function handleLanguage(event) {
  var attr = event.target.getAttribute("language");
  if (attr) {
    getData(attr)
  }
}
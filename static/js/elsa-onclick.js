// Section Displays


function displayContextSection() {
  var x = document.getElementById("context_detail");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 

function displayCollectionsSection() {
  var x = document.getElementById("collections_detail");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 






// Form Displays
document.getElementById("displayAliasForm").style.display = "none";
document.getElementById("displayCitationInformationForm").style.display = "none";
document.getElementById("displayDataForm").style.display = "none";

function displayAliasForm() {
  var x = document.getElementById("displayAliasForm");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 

function displayCitationInformationForm() {
  var x = document.getElementById("displayCitationInformationForm");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 

function displayDataForm() {
  var x = document.getElementById("displayDataForm");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 

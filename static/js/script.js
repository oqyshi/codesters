function setQuote() {
    fetch('https://oqyshi.kz/quote/')
        .then(response => response.json())
        .then(data => document.getElementById("quote").innerHTML = data.quote);
};

setInterval(() => {
    setQuote();
}, 10000);


function showTime() {
    var date = new Date();
    var h = date.getHours();
    var m = date.getMinutes();
    var s = date.getSeconds();

    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;

    var time = `${h}:${m}:${s}`;
    document.getElementById("MyClockDisplay").innerText = time;
    document.getElementById("MyClockDisplay").textContent = time;

    setTimeout(showTime, 1000);
}

/* important, otherwise won't run */
showTime();


function renderChart(health_data) {
    var chart = new CanvasJS.Chart("chartContainer", {
        theme: "light2",
        title: {
            text: "Your health stats"
        },
        data: [{
            type: "line",
            indexLabelFontSize: 16,
            dataPoints: health_data
        }]
    });
    chart.render();
}

fetch('https://oqyshi.kz/health/1')
    .then(response => response.json())
    .then(data => renderChart(data.health_data));


function openMeeting() {
    window.open('https://meet.jit.si/START_Hack_2021_Test', 'popUpWindow', 'height=500,width=500,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes')
}
var gamingRoom = document.getElementById('gamingroom');

gamingRoom.addEventListener("click", function () {
    openMeeting();
});


tasksMeeting.onclick = () => {
    openMeeting();
}

boardMeeting.onclick = () => {
    openMeeting();
}

calendar.addEventListener("click", function () {
    alert("Calendar!")
})



var hidebtn = document.getElementById("hide")
hidebtn.addEventListener("click", function () {
    document.getElementById("collapseExample").style.display = "none";
})

var showbtn = document.getElementById("show")
showbtn.addEventListener("click", function () {
    document.getElementById("collapseExample").style.display = "block";
})




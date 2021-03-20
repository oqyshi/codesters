function setQuote() {
    fetch('https://api.js-on.de/quote')
        .then(response => response.json())
        .then(data => document.getElementById("quote").innerHTML = data.quote);
};

setInterval(() => {
    setQuote();
}, 3000);


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
fetch('https://api.js-on.de/health/1')
    .then(response => response.json())
    .then(data => renderChart(data.health_data));
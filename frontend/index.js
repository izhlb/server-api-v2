let options_endpoint = 'http://192.168.0.106:5000/api/v2/system';


let cpu_list = null;
let mem_list = null;

let disk_free = null;
let disk_used = null;
let myChart;





 function disableZoom(event) {
  if (event.ctrlKey && (event.deltaY || event.wheelDelta)) {
      event.preventDefault();
  }
}


if (window.addEventListener) {
  window.addEventListener('wheel', disableZoom, { passive: false });
} else {

  window.attachEvent('onwheel', disableZoom);
}
function fetchData() {
    fetch(options_endpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
          cpu_list = JSON.parse(data.graphs.cpu);
          mem_list = JSON.parse(data.graphs.mem);
          disk_free = JSON.parse(data.disk.free);
          disk_used = JSON.parse(data.disk.used);
            document.getElementById('ping').textContent = data.net.ping + 'ms';
            document.getElementById('startup').textContent = data.other.startup;
            document.getElementById('hostname').textContent = data.other.hostname;
            document.getElementById('cpu_clock').textContent = data.cpu.clock;
            document.getElementById('cpu_threads').textContent = data.cpu.threads;
            document.getElementById('arch').textContent = data.cpu.arch;
            document.getElementById('cpu_name').textContent = data.cpu.brand;

            document.getElementById('mem_usage').textContent = data.memory.used;
            document.getElementById('mem_free').textContent = data.memory.percent + "%";
            document.getElementById('mem_total').textContent = data.memory.total;

            document.getElementById('disk_used').textContent = Math.round(disk_used) + " GB" ;
            document.getElementById('filesystem').textContent = data.disk.filesystem;
            document.getElementById('mountpoint').textContent = data.disk.mount;
            document.getElementById('disk_total').textContent = Math.round(data.disk.total) + " GB";

            document.getElementById('title').textContent = data.other.hostname + " – sysinf";

            




            if (myChart) {
                myChart.data.labels = cpu_list;
                memChart.data.labels = mem_list;
                myChart.data.datasets[0].data = cpu_list;
                memChart.data.datasets[0].data = mem_list;
                myChart.update();
                memChart.update();
            } else {
                cpu_chart();
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

function cpu_chart() {
    var data = {
        labels: [],
        datasets: [{
            label: "CPU",
            backgroundColor: 'rgba(59, 89, 135, 0.2)',
            borderColor: 'rgba(59, 89, 135, 1)',
            fill: true,
            pointBackgroundColor: 'rgba(75, 192, 192,0.0000001)',
            borderWidth: 0,
            data: cpu_list
        }]
    };

    var datadrive = {
      labels: ["Free",'Used'],
      datasets: [{
          label: "DISK",
          backgroundColor: ['rgb(59, 59, 59)','rgb(11, 111, 80)'],
          fill: true,

          pointBackgroundColor: 'rgba(75, 192, 192,0.0000001)',
          borderWidth: 0,
          data: [disk_free,disk_used]
      }]
  };

    var data2 = {
      labels: [],
      datasets: [{
          label: "Memory Usage",
          backgroundColor: 'rgba(161, 46, 50, 0.2)',
          borderColor: 'rgba(161, 46, 50, 1)',
          fill: true,
          pointBackgroundColor: 'rgba(75, 192, 192,0.0000001)',
          borderWidth: 0,
          data: mem_list
      }]
  };


    var options = {
        animation: false,
        plugins:{
        legend: {
            display: false
        },
      },
        tooltips: {
            enabled: false,
            callbacks: {
                label: function (tooltipItem) {
                    return tooltipItem.yLabel;
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
                ticks: {
                  stepSize: 20
                },
            },
            x: {
                display: false
            }
        }
    };




    var ctx = document.getElementById('myChart').getContext('2d');
    var ctx2 = document.getElementById('memChart').getContext('2d');
    var ctx3 = document.getElementById('diskChart').getContext('2d');


    myChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });
    memChart = new Chart(ctx2, {
      type: 'line',
      data: data2,
      options: options
  });

  diskChart = new Chart(ctx3, {
    type: 'doughnut',
    data: datadrive,
    borderWidth: 5 


});

};


function showsettings(){
    document.getElementById('options-container').style.display = 'flex';
};

function exitsettings(){
    document.getElementById('options-container').style.display = 'none';
};

fetchData();

setInterval(fetchData, 2000);

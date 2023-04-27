fetch('http://127.0.0.1:5000/data').then(response => response.json()).then(data => {
    const xAxis = [];
    const yAxis = [];

    for (let key in data) {
      xAxis.push(key);
      yAxis.push(data[key]);
    }

    const ctx = document.getElementById('myChart');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: xAxis,
        datasets: [{
          label: 'Energy Sources',
          data: yAxis,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            // add more colors as needed
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            // add more colors as needed
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });
  });
  


fetch('http://127.0.0.1:5000/data').then(response => response.json()).then(data => {
  const xAxis = [];
  const yAxis = [];
  
  for (let key in data) {
    xAxis.push(key);
    let value = 0; // Reset value on each iteration
    for (let i in data[key]){
      value += Number(data[key][i]); // Fix typo and cast to number
    }
    yAxis.push(value);
  }
  

    console.log(xAxis);
    console.log(yAxis);

    const ctx = document.getElementById('myChart');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: xAxis,
        datasets: [{
          label: 'Renewable Energy Sources',
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
  


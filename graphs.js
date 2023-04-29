const chartContainer = document.querySelector('.canvas-container');
const animationContainer = document.getElementById('animation-container');
const loader = document.querySelector('#loader');

// Show animationContainer while data is being fetched
animationContainer.style.display = 'block';
loader.style.display = 'block';
chartContainer.style.display = 'none';

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

  // Replace animationContainer with chart
  animationContainer.style.display = 'none';
  loader.style.display = 'none';
  chartContainer.style.display = 'block';
  const canvas = document.getElementById('myChart');
  canvas.style.display = 'block';
  const myChart = new Chart(canvas, {
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
          },
          scaleLabel: {
            display: true,
            labelString: 'Mwh'
          }
        }]
      }
    }
  });
});

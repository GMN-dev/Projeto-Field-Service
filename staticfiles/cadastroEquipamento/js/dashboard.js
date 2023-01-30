(() => {
  'use strict'

  let urlDashboard = '/home/api/dashboard/current-month'
  
  feather.replace({ 'aria-hidden': 'true' })
  
  //Fetch Data from API
  async function getData(uri) {
    const response = await fetch(uri)
    return response.json()
  }


  async function renderDashboard(){
    let dataApi = await getData(urlDashboard)

    let y = [];
    let x = [];
  
    dataApi.forEach(data => {
      y.push(data.operacao)
      x.push(data.qtd_chamados)
    });

  // Graphs
  const ctx = document.getElementById('myChart')
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: y,
        datasets: [{
          data: x,
          lineTension: 0,
          backgroundColor: '#007bff',
          borderColor: '#007bff',
          borderWidth: 4,
          pointBackgroundColor: '#007bff'
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        },
        legend: {
          display: false
        }
      }
    })
  }

  //Render -Dashboard-
  renderDashboard()
})()

(() => {
  'use strict'

  let urlDashboard = '/cadastro/api/dashboard'
  let url = '/cadastro/api/incidentes/'
  var tr = []

  
  //Fetch Data from API
  async function getData(uri) {
    const response = await fetch(uri)
    tr = await response.json()
  }

  
  feather.replace({ 'aria-hidden': 'true' })

  async function renderDashboard(){
    await getData(urlDashboard)

    let y = [];
    let x = [];

    tr.forEach(data => {
      y.push(data.operacao)
      x.push(data.qtd_solicitacao)
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

  //Render table *-Solicitações-*
  // renderTable()

  //Render -Dashboard-
  renderDashboard()
})()
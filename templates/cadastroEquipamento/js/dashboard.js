/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  const ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: [
        'Mongeral',
        'CAIXA Econ.',
        'Comgás',
        'Creditas',
        'DLL',
        'LATAM',
        'LATAM Pass',
        'Planejamento',
        'Sofisa',
        'Stefanini',
        'Via Varejo'
      ],
      datasets: [{
        data: [
          10,
          13,
          18,
          24,
          3,
          9,
          25,
          27,
          33,
          35,
          3
        ],
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
})()
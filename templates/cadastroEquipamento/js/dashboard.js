(() => {
  'use strict'

  // get API link and <tbody> element
  let url = '/cadastro/api/dashboard/'
  let table = document.querySelector('#tbody')

  let y = ['Mongeral','CAIXA Econ.','Comgás','Creditas','DLL','LATAM','LATAM Pass','Planejamento','Sofisa','Via Varejo']
  let x = [10,13,18,24,3,9,25,27,33,3]


  // access API and call function to create a dynamic table
  fetch(url).then(response => response.json())
    .then(jsonObj => tbody(jsonObj))
    .catch(() => alert('Não foi possível acessar a API'))

  // Function to create a dynamic <tbody> 
  function tbody(json) {
    json.forEach(count => {
      table.innerHTML +=
        '<tr>' +
          '<td>' + count.chamado + '</td>' +
          '<td>' + count.data_incidente + '</td>' +
          '<td>' + count.informante +  '</td>' +
          '<td>' + count.operacao + '</td>' +
          '<td>' + count.andar + 'º</td>' +
          '<td>' + count.periferico + '</td>' +
          '<td>' + count.motivo_solicitacao + '</td>' +
          '<td>' + count.observacao + '</td>' +
          '<td><button type="button" class="btn btn-secondary btn-sm">Editar</button> ' +
          '<button type="button" class="btn btn-danger btn-sm">Excluir</button></td>' +
        '</tr>'
    })  
  }

  feather.replace({ 'aria-hidden': 'true' })

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


})()
(() => {
  'use strict'

  let urlDashboard = '/cadastro/api/dashboard'
  let url = '/cadastro/api/incidentes/'
  const pageSize = 10;
  let curPage = 1;
  var tr = []

  async function renderTable(page = 1) {
    await getData(url)

    if (page == 1) {
      prevButton.style.visibility = "hidden";
    } else {
      prevButton.style.visibility = "visible";
    }

    if (page == numPages()) {
      nextButton.style.visibility = "hidden";
    } else {
      nextButton.style.visibility = "visible";
    }

    // Create Table
    var tbody = "";
    tr.filter((row, index) => {
      let start = (curPage - 1) * pageSize;
      let end = curPage * pageSize;
      if (index >= start && index < end) return true;
    }).forEach(data => {
      tbody += "<tr scope='row'>";
      tbody += `<td> ${data.chamado} </td>`;
      tbody += `<td> ${data.data_incidentes}</td>`;
      tbody += `<td> ${data.solicitante} </td>`;
      tbody += `<td> ${data.operacao}</td>`;
      tbody += `<td> ${data.andar}</td>`;
      tbody += `<td> ${data.periferico}</td>`;
      tbody += `<td> ${data.motivo}</td>`;
      tbody += `<td> ${data.observacao}</td>`;
      tbody += "<td><button type='button' class='btn btn-secondary btn-sm'>Editar</button> " +
      "<button type='button' class='btn btn-danger btn-sm'>Excluir</button></td><tr>";
    });
    document.getElementById("data").innerHTML = tbody;
  }

  function previousPage() {
    if (curPage > 1) {
      curPage--;
      renderTable(curPage);
    }
  }

  function nextPage() {
    if ((curPage * pageSize) < tr.length) {
      curPage++;
      renderTable(curPage);
    }
  }

  function numPages() {
    return Math.ceil(tr.length / pageSize);
  }

  document.querySelector('#nextButton').addEventListener('click', nextPage, false);
  document.querySelector('#prevButton').addEventListener('click', previousPage, false);
  
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
  renderTable()

  //Render -Dashboard-
  renderDashboard()
})()
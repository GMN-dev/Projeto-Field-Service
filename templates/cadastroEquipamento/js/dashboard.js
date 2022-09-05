(() => {
  'use strict'

  let url = '/cadastro/api/dashboard/'
  const pageSize = 10;
  let curPage = 1;
  var tr = []

  async function renderTable(page = 1) {
    await getData()

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
  async function getData() {
    const response = await fetch(url)
    tr = await response.json()
  }

  
  feather.replace({ 'aria-hidden': 'true' })

  let y = ['Mongeral','CAIXA Econ.','Comgás','Creditas','DLL','LATAM','LATAM Pass','Planejamento','Sofisa','Via Varejo']
  let x = [10,13,18,24,3,9,25,27,33,3]

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

  //Render table *-Solicitações-*
  renderTable()

})()
axios.get('http://127.0.0.1:5000/reports')
  .then(function (response) {
    // Pega o corpo da tabela onde as linhas serão inseridas
    let div = document.getElementById("report_div");

    // Loop para percorrer os dados e adicionar cada linha na tabela
    for (var i = 0; i < response.data.length; i++) {
      // Montando a linha da tabela com os dados
      let linha = `
        <tr>
          <td>${response.data[i]["id"]}</td>
          <td>${response.data[i]["chamado"]}</td>
          <td>${response.data[i]["usuario"]}</td>
          <td>${response.data[i]["titulo"]}</td>
          <td>${response.data[i]["info"]}</td>
        </tr>
      `;

      // Adicionando a linha na tabela
      div.innerHTML += linha;
    }
  })
  .catch(function (error) {
    // Manipula erros da requisição
    console.error(error);
  })
  .finally(function () {
    // Sempre será executado
  });

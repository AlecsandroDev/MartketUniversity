axios.get('http://127.0.0.1:5000/users')
  .then(function (response) {
    // Pega o corpo da tabela onde as linhas serão inseridas
    let div = document.getElementById("user_div");

    // Loop para percorrer os dados e adicionar cada linha na tabela
    for (var i = 0; i < response.data.length; i++) {

      // Montando a linha da tabela com os dados
      let linha = `
        <tr>
          <td>${response.data[i]["id"]}</td>
          <td>${response.data[i]["nome"]}</td>
          <td>${response.data[i]["email"]}</td>
          <td>${response.data[i]["telefone"]}</td>
          <td>${response.data[i]["cidade"]}</td>
          <td>${response.data[i]["estado"]}</td>
          <td>${response.data[i]["idade"]}</td>
          <td>
            <form action="/admin/dashboard/users/manage_users/${response.data[i]["id"]}" method="get">
              <button type="submit">Atualizar</button>
            </form>
          </td>
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

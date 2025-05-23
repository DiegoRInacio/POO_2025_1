document.getElementById('cadastroForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const nome = document.getElementById('nome').value;
  const idade = document.getElementById('idade').value;
  const email = document.getElementById('email').value;

  const usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
  usuarios.push({ nome, idade, email });
  localStorage.setItem('usuarios', JSON.stringify(usuarios));

  document.getElementById('cadastroForm').reset();

  window.location.href = 'usuarios.html';
});

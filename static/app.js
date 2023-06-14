const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

loginForm.addEventListener('submit', function(event) {
  event.preventDefault();
  const username = usernameInput.value;
  const password = passwordInput.value;
  
  // Enviar datos de inicio de sesión al servidor
  console.log(`Nombre de usuario: ${username}, Contraseña: ${password}`);
});

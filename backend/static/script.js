document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.onsubmit = function() {
        // Potresti voler aggiungere qui qualche verifica o logica prima dell'invio del form
        console.log("Form submitted!");
    };
});

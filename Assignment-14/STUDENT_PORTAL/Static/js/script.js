// script.js - simple client-side validation for login form

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const userError = document.getElementById('userError');
    const passError = document.getElementById('passError');

    form.addEventListener('submit', function (e) {
        // clear previous errors
        userError.textContent = '';
        passError.textContent = '';

        let valid = true;

        if (!username.value.trim()) {
            userError.textContent = 'Username cannot be empty';
            valid = false;
        }
        if (!password.value.trim()) {
            passError.textContent = 'Password cannot be empty';
            valid = false;
        }

        if (!valid) {
            e.preventDefault(); // stop form submission
        } else {
            // allow submission to server; you may do additional client-side checks here
        }
    });
});

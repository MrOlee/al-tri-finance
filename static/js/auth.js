function login(){

    const email = document.getElementById('email').value
    const password = document.getElementById('password').value

    if(email === '' || password === ''){
        alert('Isi email dan password')
        return
    }

    alert('Login berhasil')

    window.location.href = '/dashboard'
}

function register(){

    const email = document.getElementById('register-email').value
    const password = document.getElementById('register-password').value

    if(email === '' || password === ''){
        alert('Isi email dan password')
        return
    }

    alert('Register berhasil')

    window.location.href = '/login'
}

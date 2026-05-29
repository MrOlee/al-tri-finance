async function login(){

    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const { data, error } = await supabaseClient.auth.signInWithPassword({
        email: email,
        password: password
    })

    if(error){
        alert(error.message)
        return
    }

    window.location.href = "/dashboard"
}

async function register(){

    const email = document.getElementById("register-email").value
    const password = document.getElementById("register-password").value

    const { data, error } = await supabaseClient.auth.signUp({
        email: email,
        password: password
    })

    if(error){
        alert(error.message)
        return
    }

    alert("Register berhasil!")

    window.location.href = "/"
}

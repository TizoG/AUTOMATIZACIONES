##
# Envios de correos electrónicos
#
# biblioteca smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Ajuste del correo electrónico
remitente = ''
contraseña = ''
destinatario = ''
asunto = 'Prueba automatizacion de email'

# Configurar el cuerpo del email
mensaje = MIMEMultipart()
mensaje['De'] = remitente
mensaje['A'] = destinatario
mensaje['Asunto'] = asunto

body_message = 'Hola esto es un mensaje automatizado'

mensaje.attach(MIMEText(body_message, 'sencillo'))

# El servidor SMTP de su proveedor de email
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.starttls()


# Inicia sesión con la cuenta de email
smtp_server.login(remitente, contraseña)

# Enviar el email
texto_email = mensaje.as_string()
smtp_server.sendmail(remitente, destinatario, texto_email)

# Cerrar conexión
smtp_server.quit()

print("Email enviado exitosamente!!")

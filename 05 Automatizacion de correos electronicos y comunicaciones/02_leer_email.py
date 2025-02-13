##
# Leer emails
#
# biblioteca imaplib
#
import imaplib
import email
from email.header import decode_header

# Ajuste del email
name_user = ''
contraseña = ''
name_user = 'tucorreo'
contraseña = 'tucontraseña'

# Servidor IMAP de su proveedor de email
imap_server = imaplib.IMAP4_SSL('imap.gmail.com')

# Inicie sesión en su cuenta de email
imap_server.login(name_user, contraseña)

# Seleccionar cuadro de entrada
imap_server.select('bandeja de entrada')

# Buscar emails no leídos
resultado, message_ids = imap_server.search(None, 'NO VISTO')

# Recuperar ID de email
list_ids = message_ids[0].split()

# Iterar a través de ID y buscar emails
for email_id in list_ids:
    resultado, mensaje = imap_server.fetch(email_id, '(RFC822)')
    mensaje_bytes = mensaje[0][1]
    cadena_mensaje = mensaje_bytes.decode('utf-8')
    msg = email.message_from_string(cadena_mensaje)
    remitente = decode_header(msg['From'])[0]
    asunto = decode_header(msg['Asunto'])[0]

    print(f"Remitente: {remitente}")
    print(f"Asunto: {asunto}")


# Puedes acceder al cuerpo del email
msg.get_payload()

# Cerrar sesión
imap_server.logout()


"""
Que podemos hacer con la automatización de email?
Podemos enviar informes de manera automática,
responder automáticamente a mensajes específicos u organizar correos automáticamente
"""

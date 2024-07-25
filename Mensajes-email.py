from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

Correo_electronico = "anthonyluzon124@gmail.com"
Correo_pass = "fdyf llnx mvia xalf"
Correo_destino = "aluzonprueba@yopmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Correo_electronico, Correo_pass)

    # Configuración del correo electrónico
    asunto = 'Ejecución en Jenkins'
    cuerpo = 'Se realizo la ejecución de un proyecto de Jenkins'

    # Crear el objeto del mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = Correo_electronico
    mensaje['To'] = Correo_destino
    mensaje['Subject'] = asunto

    mensaje.attach(MIMEText(cuerpo, 'plain'))

    texto = mensaje.as_string()
    smtp.sendmail(Correo_electronico, Correo_destino, texto)  # Enviar el correo
    smtp.quit()  # Cerrar la conexión
    print("Correo enviado exitosamente")
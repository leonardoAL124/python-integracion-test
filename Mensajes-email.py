import smtplib

Correo_electronico = "anthonyluzon124@gmail.com"
Correo_pass = "fdyf llnx mvia xalf"
Correo_destino = "aluzonprueba@yopmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Correo_electronico, Correo_pass)

    asunto = "Ejecución de actividades en Jenkins"
    headers = f"From: {Correo_electronico}\r\nTo: {Correo_destino}\r\nSubject: {asunto}\r\n"
    msg = f"{headers}\r\nSe ha realizado una ejecución del proyecto desde Jenkins"
    mensaje = msg.replace(u'\xa0', u' ')

    smtp.sendmail(Correo_electronico, Correo_destino, mensaje)
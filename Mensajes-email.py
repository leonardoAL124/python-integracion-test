import smtplib

Correo_electrónico = "anthonyluzon124@gmail.com"
Correo_pass = "fdyf llnx mvia xalf"
Correo_destino = "aluzonprueba@yopmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Correo_electrónico, Correo_pass)

    asunto = "Ejecución de actividades en Jenkins"
    headers = f"From: {Correo_electrónico}\r\nTo: {Correo_destino}\r\nSubject: {asunto}\r\n"
    msg = f"{headers}\r\nSe ha realizado una ejecución del proyecto desde Jenkins"

    smtp.sendmail(Correo_electrónico, Correo_destino, msg)
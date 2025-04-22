""" Envia la Alerta de inicio de sesion de SSH a un correo electronico """

import smtplib
import os
import datetime
import socket
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========== CONFIGURACIÓN DEL CORREO ==========
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_FROM = 'tucorreo@gmail.com'
EMAIL_TO = 'tucorreo@gmail.com'  # puedes poner otro destino
EMAIL_PASSWORD = 'tu_contraseña_o_contraseña_app'  # Usa contraseña de aplicación si tienes 2FA

# ========== DATOS DE LA SESIÓN ==========
user = os.getenv("USER")
ip_address = os.popen("who | grep 'pts' | awk '{print $5}' | tr -d '()'").read().strip()
tty = os.popen("who am i | awk '{print $2}'").read().strip()
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
hostname = socket.gethostname()

# ========== GEOLOCALIZACIÓN DE LA IP ==========
try:
    geo_info = requests.get(f'https://ipinfo.io/{ip_address}/json', timeout=5).json()
    location = geo_info.get('city', '') + ', ' + geo_info.get('region', '') + ', ' + geo_info.get('country', '')
    isp = geo_info.get('org', 'Desconocido')
except:
    location = 'No disponible'
    isp = 'Desconocido'

# ========== MENSAJE DE CORREO ==========
body = f"""
🔐 Alerta de Conexión SSH

Usuario: {user}
Hora: {now}
Hostname: {hostname}
Terminal: {tty}
IP de origen: {ip_address}
Ubicación: {location}
ISP: {isp}
"""

msg = MIMEMultipart()
msg['From'] = EMAIL_FROM
msg['To'] = EMAIL_TO
msg['Subject'] = "🔐 Alerta de Conexión SSH Detectada"
msg.attach(MIMEText(body, 'plain'))

# ========== ENVÍO DEL CORREO ==========
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    server.quit()
except Exception as e:
    print("❌ Error al enviar correo:", e)

# notify_ssh
Alerta SSH por correo electrónico  Este proyecto contiene un script en Python que envía una alerta por correo electrónico cada vez que se detecta un inicio de sesión SSH en el sistema.
¡Por supuesto! Aquí tienes un README completo y profesional para tu proyecto de alerta SSH por correo electrónico:

---

# Alerta SSH por Correo Electrónico

Este proyecto contiene un script en Python que envía una alerta por correo electrónico cada vez que se detecta un inicio de sesión SSH en el sistema. La alerta incluye información relevante como usuario, hora, dirección IP, ubicación geográfica y proveedor de internet, ayudando a mejorar la seguridad y el monitoreo de accesos remotos.

---

## Características

- Detecta inicio de sesión SSH en sistemas Linux.
- Obtiene datos del usuario, terminal, IP, hostname y hora.
- Consulta la geolocalización y proveedor de internet de la IP de origen.
- Envía un correo electrónico con toda la información usando SMTP (compatible con Gmail).
- Fácil configuración y uso.

---

## Requisitos

- Python 3.6 o superior.
- Paquetes Python: `requests`.
- Acceso a un servidor SMTP para enviar correos (ejemplo: Gmail).
- (Opcional) Entorno virtual para aislar dependencias.

---

## Instalación

1. Clona este repositorio o descarga los archivos.

```bash
git clone https://github.com/tuusuario/notify_ssh.git
cd notify_ssh
```

2. (Opcional) Crea y activa un entorno virtual:

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## Configuración

Edita el archivo `ssh_correo.py` y modifica las variables de configuración del correo:

```python
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_FROM = 'tucorreo@gmail.com'
EMAIL_TO = 'destino@gmail.com'
EMAIL_PASSWORD = 'tu_contraseña_o_contraseña_app'
```

**Importante:** Si usas Gmail y tienes 2FA, crea una contraseña de aplicación para usar aquí.

---

## Uso

Ejecuta el script manualmente para probar el envío de la alerta:

```bash
python ssh_correo.py
```

Para automatizar la alerta en cada inicio de sesión SSH, puedes configurar que este script se ejecute al iniciar sesión, por ejemplo, agregándolo a:

- `/etc/profile`
- `/etc/ssh/sshrc`
- Un módulo PAM personalizado

---

## Seguridad

- No guardes contraseñas en texto plano en el script en entornos de producción.
- Usa variables de entorno o gestores de secretos para manejar credenciales.
- Asegúrate de proteger el acceso a este script y sus credenciales.


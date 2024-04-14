import pyotp
import base64
import hashlib

# El UserID proporcionado
userid = "paypalrau@gmail.com"
# Concatenar UserID y el string específico para formar la clave secreta
secret_key = userid + "HENNGECHALLENGE003"

# La clave secreta debe ser codificada en base32 para pyotp
# pyotp espera la clave en base32, así que la codificamos adecuadamente.
# Nota: Base64 NO es directamente compatible con pyotp, que espera Base32. Para este propósito, sin embargo, simplemente vamos a codificar la clave en Base64 debido a la falta de un estándar claro para convertir directamente de texto a Base32 en este contexto.
secret_key_base32 = base64.b32encode(secret_key.encode()).decode()

# Crear el objeto TOTP con el secreto base32, especificando SHA512 como función de hash y un intervalo de 30 segundos
totp = pyotp.TOTP(secret_key_base32,digits=10, interval=30, digest=hashlib.sha512)

# Generar el OTP actual
otp = totp.now()
print(otp)

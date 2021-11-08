# SoftGAC-backend

Repositorio para el backend de la aplicación SoftGAC
para la empresa Genios Aprende Jugando

# Instalación

** Requerimientos iniciales **

- Python 3
- MySQL
- pipenv
- make

** Dependencias **

Ejecute el siguiente comando para crear el ambiente virtual:

    pipenv shell

Luego instalar las dependencias usando:

    make setup

# Conexión con MySQL

Para configurar la conexión a la base de datos local a través de MySQL
debe usar variables de entorno para autenticarse con usuario y contraseña

No olvide crear la base de datos en su local llamada **softgac** y darle
los permisos respectivos:

Crear un archivo **.env** con las siguientes variables de entorno,
reemplace los valores según correspondan

    export DATABASE_USER=usuario
    export DATABASE_PASS=contraseña
    export DATABASE_PORT=3306

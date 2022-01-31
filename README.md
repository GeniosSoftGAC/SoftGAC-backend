# SoftGAC-backend

Repositorio para el backend de la aplicación SoftGAC
para la empresa Genios Aprende Jugando

# Instalación

**Requerimientos iniciales**

- Python 3
- MySQL
- pipenv
- make

**Dependencias**

Ejecute el siguiente comando para crear o entrar el ambiente virtual:

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

# Configurar MySQL y Ejecutar el servidor con la API

1. Entrar en MySQL:
```
    mysql -u nombredeusuario -p
```
2. Crear base de datos 'softgac'
``` sql   
    CREATE DATABASE softgac;
```
3. Dar privilegios a la base de datos para poder acceder a ella desde django:
``` sql
    GRANT ALL PRIVILEGES ON sofgac TO 'username'@'host'
```
1. Exportar variables de entorno del archivo .env
```
    source .env
```
5. Abrir proyecto de django y dentro de la carpeta SoftGAC, migrar los modelos para cada app o modulo
```   
    python manage.py makemigrations products
    python manage.py migrate products
```
6. Ejecutar el servidor:
```   
    python manage.py runserver
```




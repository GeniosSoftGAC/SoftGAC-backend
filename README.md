# SoftGAC-backend

Repositorio para el backend de la aplicación SoftGAC
para la empresa Genios Aprende Jugando

Para configurar la conexión a la base de datos local a través de MySQL
debe usar variables de entorno para autenticarse con usuario y contraseña

No olvide crear la base de datos en su local llamada **softgac** y darle
los permisos respectivos:

Crear un archivo **.env** con las siguientes variables de entorno,
reemplace los valores según correspondan

    export DATABASE_USER=usuario
    export DATABASE_PASS=contraseña
    export DATABASE_PORT=3306

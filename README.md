 GenOdoo

# Guía de instalación

## Instalar Docker
Para instalar la instación de GenOdoo vamos utilizar Docker y Docker-Compose. De esta manera nos aseguramos de que las dependencias son satisfechas y de que la instalación es tan sencilla como poner un comando.

Por lo tanto, lo primero que vamos a necesitar es instalar docker. Dependiendo de tu sistema operativo la instalación es de una forma o otra. Pinchando [aquí](https://docs.docker.com/install/) podras ver cual es la manera de instalarlo en tu ordenador.

También necesitaremos docker-compose, el cual nos permitirá levantar el contenedor de docker con las características necesarias para GenOdoo. Pinchando [aquí](https://docs.docker.com/compose/install/) podras ver cual es la manera de instalarlo en tu ordenador.  
   

## Levantar el contenedor

Para levantar el contenedor de Docker lo único que necesitamos es escribir el siguiente comando en el directorio raíz de nuestro sistema Odoo, donde tenemos nuestro archivo docker-compose.yml y nuestra carpeta de módulos.

```
docker-compose up -d
```

Si este te da problemas de permisos prueba a ejecutarlo como root.

## Últimos pasos

Ya tendríamos nuestro Odoo montado en la dirección http://localhost:8069/web

Creamos una BD con el nombre que queramos e instalamos el módulo del paquete que queramos aplicar. 
Recomendamos crear una base de datos distinta para cada módulo puesto que estos no están pensados para ser instalados al mismo tiempo en la misma instancia. Puedes hacerlo desde http://localhost:8069/web/database/manager


# Otros datos

## IBM Watson
correo: i72moprf@uco.es
pass: IBMWatson9
# blog_project
### Blog project for Coderhouse's final

### Instrucciones:
Instalar Python desde la [web oficial](https://www.python.org/downloads/)

Recomendacion: Generar un entorno virtual

1.  Clonar el proyecto o descargar el archivo comprimido.

2.  Instalar las dependencias del proyecto:  
    +  ***Automaticamente:***
        -    *pip install -r requirements.txt*

    + ***De forma manual:***
        -    *pip install django*
        -    *pip install Pillow*

3. Realizar las migraciones para generar la bd
    -    ***python manage.py makemigrations***
    -    ***python manage.py migrate***

4. Correr la aplicacion
    -    ***python manage.py runserver***

5. Ya puedes ingresar a web
    -    [http://localhost:8000/](http://localhost:8000/)  
    *puedes especificar el puerto que prefieras utilizar, por defecto es el puerto 8000*

***
  
### Acerca del Blog  

El proyecto trata de un blog dedicado a recomendaciones y experiencias de los miembros sobre turismo en las distintas ciudades del mundo.  
Los usuarios podrán observar la lista de los posteos y las promociones, pero para observar el detalle, **modificar**, **crear** o **eliminar** contenido deberán estar **logueados** o en su defecto, **registrarse**.  
Cada **post** consta de un título, contenido, autor y fecha de publicación (que se agrega automáticamente).  
Los posts se listan del más reciente al más antiguo.  
Apartado **promociones**: Aquí los usuarios ingresarán cupones, descuentos, promociones, etc
Cada promo consta de una categoría, una descripción donde se indica brevemente el beneficio, un detalle donde se ingresa la fuente, codigo de descuento, cupón, etc.
y una fecha de caducidad de la misma. Ordenándose desde la fecha más lejana a la más antigua

Cada **usuario** puede editar su perfil y agregar una imágen como avatar.  
Cada usuario consta de un numbre de usuario, contraseña y un email como datos obligatorios, y si así lo desean pueden agregar su nombre y apellido.  
En el perfil del usuario se lista además la fecha de su último ingreso y la fecha en la que se ha unido (registrado) al blog.  

Los datos de guardan en una base de datos de motor SQLite ya provisto por Django.  

#### Mensajería
Los usuarios cuentan con un sistema de mensajería a modo de mensaje directo.  
Los mensajes sólo los pueden ver los usuarios a los cuales están destinados y el usuario que envió el mismo.  
Dentro del perfil o desde la barra de navegación el usuario accederá a su **Inbox** donde verá su bandeja de entrada y su bandeja de salida.  
  
#### Layout
El blog cuenta con una **barra de navegación** a la cual se puede acceder a las distintas secciones del mismo. (Home, Posts, Promos y About).  
Además en el margen derecho podrás ingresar o crear un usuario.  
Al estar logueado en el margen derecho se muestra el nombre de usuario, y avatar si corresponde, con un menú desplegable donde se puede acceder al Perfil,
a sus mensajes y cerrar la sesión.


***
### Video explicativo

[https://youtu.be/45bJle669qw](https://youtu.be/45bJle669qw)

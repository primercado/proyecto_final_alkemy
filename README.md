# Documentación del Proyecto StockControl
## Descripción

StockControl es una aplicación web de Django diseñada para gestionar el inventario de productos y la información de proveedores. Permite a los usuarios realizar las siguientes acciones:

* Ver una lista de todos los productos y proveedores registrados.
* Agregar nuevos productos y proveedores.
* Acceder a una página de inicio que enlaza a las diferentes secciones de la aplicación.

## Configuración del Entorno
### Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

    Python 3.8 o superior
    Django 3.2 o superior
    pip (gestor de paquetes de Python)

### Instalación

* Clona el repositorio del proyecto:

    bash

git clone <url-del-repositorio>
cd StockControl


* Instala las dependencias del proyecto:

    pip install -r requirements.txt

## Configuración de la Base de Datos

Realiza las migraciones necesarias para preparar la base de datos:

python manage.py makemigrations
python manage.py migrate

## Superusuario

* usuario: admin
* contraseña: admin
* correo: admin@admin.com


## Ejecución del Proyecto

Para ejecutar el servidor de desarrollo, utiliza:

python manage.py runserver

Navega a http://localhost:8000/ en tu navegador web para acceder a la página de inicio.
Estructura del Proyecto

Descripción de los componentes principales del proyecto:

    compra/: Aplicación Django que contiene la lógica principal para gestionar productos y proveedores.
        models.py: Define los modelos Producto y Proveedor.
        views.py: Contiene las vistas para listar y agregar productos y proveedores.
        forms.py: Formularios para la entrada de datos de los modelos.
        admin.py: Configuración del panel de administración de Django para los modelos.
        urls.py: Rutas URL para las vistas de la aplicación.
        templates/: Plantillas HTML para la interfaz de usuario.
    StockControl/: Configuración global del proyecto Django.

## Funcionalidades
### Página de Inicio

* Ruta: /
* Descripción: Proporciona enlaces a todas las funcionalidades principales.

### Gestión de Productos

* Listar Productos
        Ruta: /compra/productos/
        Descripción: Muestra todos los productos en la base de datos.
* Agregar Producto
        Ruta: /compra/producto/agregar/
        Descripción: Formulario para ingresar un nuevo producto.

### Gestión de Proveedores

* Listar Proveedores
        Ruta: /compra/proveedores/
        Descripción: Muestra todos los proveedores en la base de datos.
* Agregar Proveedor
        Ruta: /compra/proveedor/agregar/
        Descripción: Formulario para ingresar un nuevo proveedor.

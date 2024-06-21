# ModaPick

Blog multiusuario para indumentaria de moda, creado con ```Django 5.0.6```


## Descripcion:

En el blog se van publicando diferentes estilos de indumentaria y los usuarios pueden votar si les gusta o no el diseño.


## Objetivo:

Conocer el comportamiento de eleccion de los usuarios para la creacion de futuros diseños de indumentaria de la compañia.


## Funcionalidades:

- Los usuarios acceden con usuario y contraseña.

- Los usuarios registrados pueden ver todos los posteos y en cada posteo puede elegir "like" o "dislike".

- Los usuarios registrados pueden elegir una sola opcion por posteo. Y puede cambiar de opinion luego de haber elegido una opcion.

- Los usuarios registrados pueden ver el detalle de su actividad en cada posteo.

- Los usuarios registrados y el personal "staff" pueden ver el "ranking" de cada posteo con sus estadisticas.

- Solamente el personal "staff" puede crear y eliminar posteos.

- Los usuarios anonimos pueden ver todos los posteos pero no pueden elegir "like" o "dislike".


## Instrucciones para instalar el proyecto en Windows:

- Abrir una carpeta donde quiero clonar el proyecto:
Ej: DjangoProjects

- Abrir terminal de Git Bash:
Boton derecho adentro de la carpeta "DjangoProjects" -> Git Bash Here

- Clonar el proyecto:
```
git clone https://github.com/awsmunarriz/ModaPick.git
```

- Desde la misma terminal de Git Bash acceder a la carpeta ModaPick:
```
cd ModaPick
```

- Desde la misma terminal de Git Bash abrir VSCode:
```
code .
```

- Abrir una terminal en VSCode:
Terminal -> Nuevo terminal

- Crear un entorno virtual:
```
python -m venv venv
```

- Activar el entorno virtual:
```
venv\Scripts\activate
```

- Instalar los requerimientos:
```
pip install -r requirements.txt
```


## Ejecutar el proyecto:
```
python manage.py runserver
```


## Credenciales de superuser:
- Usuario: mariano
- Contraseña: 123456


## Credenciales de usuario basico:
- Usuario: pepe
- Contraseña: Welcome/2024


## Pruebas realizadas:

Ver archivo "Casos-de-prueba.xlsx" en este mismo repositorio.

## Video demostracion:

-> ((Agregar link a Youtube))


Disfruta el sitio :)
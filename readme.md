Pasos para correr el proyecto localmente

1- Clonar el repositorio en un directorio convenientemente elegido con el comando 

git clone https://github.com/Nico-AR98/Challenge.git

2- En caso de no contar con las dependencias detalladas en el archivo requirements.txt, crear un entorno virtual -para lo cual podria emplearse virtualenv- y activarlo.
Una vez activado y posicionado en el directorio del proyecto, ejecutar el comando:

pip install -r requirements.txt

3 - Correr los comandos:

python manage.py makemigrations

python manage.py migrate

4 - Acto seguido, debemos levantar el servidor con el comando:

python manage.py runserver

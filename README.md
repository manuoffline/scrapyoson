# scrapyoson

Script hecho con scrapy que recoge el nombre de grupos de una página de conciertos, para tener un listado de grupos actuales de gira

## Getting Started

pip install requirements.txt

Aunque no lo he probado he creado el archivo requirements para poder instalar las librerías que se usan.

### Prerequisites

Tener instalado python e instalar el requirements.txt

### Installing

pip install requirements.txt

### Running

Existen 2 modos de ejecutarlo
scrapy crawl artist en la carpeta spiders dentro del proyecto, nos ejecutará nuestro archivo artist.py y nos creará el archivo groups.txt en el raiz del proyecto

La segunda es ejecutar dentro de la carpeta spiders el archivo main.py con python main.py. Esto nos creará en la misma carpeta el archivo groups.txt.

### Información

Genera el fichero groups.txt

### TODO

Mi intención es solo añadir más sitios, por el momento solo necesito que funcione como un script.

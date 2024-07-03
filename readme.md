# Predicción del Dengue


Este proyecto fue desarrollado como parte del programa [**‘Mil Mujeres IA’**](https://www.intel.la/content/www/xl/es/newsroom/news/intel-capacitara-1000-mujeres-en-ia.html#gs.bmwa0t), el cual tiene como objetivo empoderar a 1000 mujeres de América Latina mediante cursos especializados en inteligencia artificial, democratizando así el acceso a esta tecnología y su aplicación práctica en el ámbito laboral productivo. Para más información del programa consulte ['aquí'](https://milmujeresia.com/)

El equipo 9 desarrolló un modelo LSTM para predecir los casos de dengue en Medellín, utilizando los datos de los últimos 12 meses.


## Instalación

Para instalar y configurar el proyecto, sigue estos pasos:

1. Clona este repositorio en tu máquina local:

git clone <url-del-repositorio>
cd <nombre-del-proyecto>


2. Instala las dependencias utilizando pip y el archivo `requirements.txt`:
pip install -r requirements.txt

Nota: Es posible que se necesiten ajustes adicionales para sistemas operativos diferentes a macOS.

## Uso

Para utilizar la aplicación:

1. Ejecuta el archivo `app.py`:

python app.py


2. Abre tu navegador web y visita: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Archivos

- `app.py`: Archivo principal que inicia la aplicación FastAPI.
- `dengue_lstm_model.h5`: Modelo LSTM entrenado para predecir casos de dengue.
- `requirements.txt`: Lista de todas las librerías requeridas para ejecutar el proyecto.
- `static/`: Directorio que contiene archivos estáticos utilizados por la aplicación.
- `index.html`: Página web principal de la aplicación.
- `logo.png`: Archivo de imagen utilizado en la interfaz.
- `notebooks/`: Directorio que contiene el EDA y desarrollo del modelo.


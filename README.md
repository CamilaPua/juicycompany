# Proyecto Django JuicyCompany

Este proyecto tiene como objetivo implementar las mejores prácticas de desarrollo utilizando Django y el ORM de Django.

## Instalación

Asegúrate de tener Python y pip instalados en tu sistema. Luego, sigue estos pasos:

### Clonar el repositorio

Puedes clonar el repositorio utilizando HTTPS con el siguiente comando:

```bash
git clone https://github.com/CamilaPua/juicycompany.git
cd juicycompany/
```

o descárgalo desde https://github.com/CamilaPua/juicycompany

### Crear un entorno virtual (opcional pero recomendado)

```bash
pip install virtualenv
python -m venv env
source env/bin/activate  # En sistemas Unix/Linux
env\Scripts\activate  # En Windows
```

### Instalar las dependencias del proyecto:

```bash
pip install -r juicycompany/requirements.txt
```

## Configuración
No es necesario realizar ninguna configuración adicional para la base de datos si estás utilizando la configuración predeterminada de Django. La configuración se encuentra en el archivo juicycompany/juicycompany/settings.py y debería verse algo así:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

## Ejecución
Para ejecutar el proyecto, utiliza el siguiente comando:

```bash
python juicycompany/manage.py runserver # si estás en la carpeta padre
python manage.py runserver # si estás en la carpeta juicycompany
```

Una vez que el proyecto esté en ejecución, abre tu navegador y accede a la aplicación en http://localhost:8000.
```

Recuerda ajustar cualquier detalle adicional según la estructura específica de tu proyecto "JuicyCompany".
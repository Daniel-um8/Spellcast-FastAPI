# PROYECTO_SPELLCAST

Spellcast es una API construida con FastAPI y SQLAlchemy para la gestión de usuarios, bibliotecas y libros, con soporte para almacenamiento de archivos PDF y extracción de texto.

## Características

- **Usuarios**: Registro y gestión de usuarios.
- **Bibliotecas**: Cada usuario puede tener múltiples bibliotecas.
- **Libros**: Cada biblioteca puede contener múltiples libros, con soporte para almacenar la ruta de archivos PDF y su contenido extraído.
- **Migraciones**: Gestión de migraciones de base de datos con Alembic.
- **Variables de entorno**: Configuración segura mediante `.env`.

## Estructura del proyecto

```
PROYECTO_SPELLCAST/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   └── routers/
│       └── __init__.py
│
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── bc75384515ca_initial_tables.py
│
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
```

## Instalación

1. **Clona el repositorio**  
   ```sh
   git clone <url-del-repositorio>
   cd PROYECTO_SPELLCAST
   ```

2. **Crea y activa un entorno virtual**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno**  
   Edita el archivo `.env` con tu cadena de conexión a la base de datos PostgreSQL.

5. **Ejecuta las migraciones**  
   ```sh
   alembic upgrade head
   ```

6. **Inicia el servidor**  
   ```sh
   uvicorn app.main:app --reload
   ```

## Uso

Accede a la documentación interactiva de la API en:  
[http://localhost:8000/docs](http://localhost:8000/docs)

## Estructura de la base de datos

- **users**: Usuarios registrados.
- **libraries**: Bibliotecas asociadas a usuarios.
- **books**: Libros asociados a bibliotecas.

## Licencia

Este proyecto está bajo la licencia MIT.
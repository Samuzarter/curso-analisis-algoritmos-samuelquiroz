# Semana 02 — Configuración del entorno de trabajo

## Entorno virtual

Comandos usados para crear y activar el entorno virtual dentro de
`ejercicios-clase/semana-02/`:

```bash
python -m venv venv
source venv/Scripts/activate
```

Se verificó el prefijo `(venv)` en la terminal antes de instalar cualquier
dependencia, y se confirmó con `pip list` que el entorno estaba vacío.

## Dependencias

Se instaló `matplotlib` con el entorno activado y se generó el archivo de
dependencias con:

```bash
pip freeze > requirements.txt
```

## Cómo reproducir este entorno

Otra persona puede reproducir exactamente el mismo
entorno con:

```bash
python -m venv venv
source venv/Scripts/activate     
pip install -r requirements.txt
```

Esto instala las mismas versiones de las librerías registradas en
`requirements.txt`, sin necesidad de instalarlas manualmente una por una.
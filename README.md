# Practica DynamoDB con datos de cine
#### Josue Rojas Noble

### Idea:

Se creó una lambda_function en AWS para insertar datos de funciones de cine en una tabla de DynamoDB llamada "Peliculas_S3D2_xideral" (Oculto mediante una variable de env),
Esta función lambda recibe un objeto el cual puede tener datos o no, esto da dos casos de uso:

#### Caso 1:
Obtiene datos de la función (pelicula_id, fecha_hora en ISO format, nombre,sala,duracion,clasificacion),
esta información se verá en el log y se agregará en la tabla.

objeto de ejemplo:
{"pelicula_id": "36",
"fecha_hora": "2025-02-05T10:12:36.075352",
"nombre": "Spider-Man: No Way Home",
"sala": "7",
"duracion": "148",
"clasificacion": "B"}

#### Caso 2:
No se obtienen datos, por lo que se genera un registro automáticamente con los datos generados automáticamente.
Se registra el último pelicula_id + 1 y se agrega a las tablas.

objeto de ejemplo:
{}

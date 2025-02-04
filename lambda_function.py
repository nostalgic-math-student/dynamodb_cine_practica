import json
import boto3
import datetime
import random
from random import randint

# Funcion auxiliar para generar fecha al azar entre hoy y total_days 
# Output ISO 8601
def random_date(total_days):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=total_days)
    return (start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))).isoformat()


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Peliculas_S3D2_xideral')

    # Utilizamos dos casos: 
    # Caso 1: si se ejecuta lambda con información (pelicula_id, fecha_hora en ISO format, nombre,sala,duracion,clasificacion)
    # Caso 2: si se ejecuta lambda sin información nada de (pelicula_id, fecha_hora en ISO format, nombre,sala,duracion,clasificacion)
    try:
        # Caso 1
        if "pelicula_id" in event:
            item_event = {
                'pelicula_id': event['pelicula_id'],
                'fecha_hora': event['fecha_hora'],
                'nombre': event['nombre'],
                'sala': event['sala'],
                'duracion': event['duracion'],
                'clasificacion': event['clasificacion'],
            }
        # Caso 2
        else:
            movies = [
                "Avatar: The Way of Water",
                "Spider-Man: No Way Home",
                "Top Gun: Maverick",
                "Black Panther: Wakanda Forever",
                "Jurassic World: Dominion",
                "Minions: The Rise of Gru",
                "Doctor Strange in the Multiverse of Madness",
                "Fast & Furious 9",
                "Elvis",
                "Lightyear",
                "The Batman"
            ]
            clasificacion = ["AA", "A", "B", "B15", "C", "D"]

            response = table.scan(ProjectionExpression="pelicula_id")
            items = response.get("Items", [])
            max_id = max(int(item["pelicula_id"]) for item in items) if items else 0
            new_id = max_id + 1

            item_event = {
                'pelicula_id': str(new_id),
                'fecha_hora': random_date(7),
                'nombre': random.choice(movies),
                'sala': str(randint(1, 20)),
                'duracion': str(randint(60, 180)),
                'clasificacion': random.choice(clasificacion),
            }

        table.put_item(Item=item_event)
        return {
            'statusCode': 200,
            'body': json.dumps(item_event)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }


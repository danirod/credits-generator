# credits-generator

Estaba cansado de hacer esto a mano sacando Excels todas las semanas
así que he automatizado el proceso.

## Instrucciones

* Exportar el CSV de suscriptores desde el panel de control de Twitch
  y dejarlo en la carpeta twitch/ con el formato original.
* Exportar el CSV de miembros desde las opciones de monetización de
  YouTube Studio y dejarlo en la carpeta youtube/ con el formato
  original.
* Exportar la lista de suscripciones regaladas desde StreamLabs y
  dejarlo en la carpeta gift/.
* `python credits.py`

## Otras notas

Se concatenan todos los CSV que haya en la misma carpeta. Esto es bueno
porque así se pueden poner los CSV del día que sale un vídeo al early
y del día que sale un vídeo al público. Esto es importante para los
primes de Twitch porque no se renuevan automáticamente y puede que haya
vencido entre que se publica el early y el final.

En el CSV de Twitch va por defecto también el username del propio
streamer. Hay que hacer un filtro para no incluirlo.
# Euro 2020

## Limpieza de datos

### Dataset partidos
  - Fase: agrupamos en un solo valor todos los partidos de la primera fase.
  - Fechas: cambiamos al formato [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601).
  - Posesión y duelos ganados: Pasamos string de porcentaje a valor entre 0 y 1.
  - Penaltis en tanda: Pasamos a NULL el valor que está como false cuando el partido no se decide por tanda de penaltis.
  - Espacios en string: En todas las columnas categóricas eliminamos posibles espacios al principio y final.
  
### Dataset que generamos con los enventos

  - Para los eventos del tipo (PK) vemos que aparecen con datos event_result y event_player
  - Unificar event_result y event_player en tipo = PK (sustituyendo PK por PK-GOAL y PK-MISSED)
  - El valor de event_player en estos casos irá a action_player_1
  - Eliminamos columnas event_result, event_player
  - Event_time en type=PK se establecerá a 120 (tiempo del final de la prórroga)
  - Event_team almacenará el id del equipo en lugar de home/away. EL valor lo traerá de la tabla teams creada en 01_matches.ipynb
  - En action_player_2 aparecen datos no coherentes (Own goal, Penalty) iguales que en action_player_1

<hr>

## Generación de tablas

### Tabla Partidos
  - ID partido.
  - Fase.
  - Fecha.
  - Dedidido por penaltis.
  - ID equipo local.
  - ID equipo visitante.

### Tabla Partidos/Equipos
  - ID partido.
  - Penaltis marcados (tanda).
  - Nombre equipo.
  - Goles.
  - Posesión.
  - Disparos.
  - Disparos entre los 3 palos.
  - Duelos ganados.

### Tabla Equipos
  - ID equipo.
  - Nombre equipo.

### Tabla eventos
  - ID evento
  - ID equipo
  - Tiempo
  - Tipo
  - Jugador 1
  - Jugador 2
  - ID partido
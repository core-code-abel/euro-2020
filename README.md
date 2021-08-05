# Euro 2020

## Limpieza de datos
  - Fase: agrupamos en un solo valor todos los partidos de la primera fase.
  - Fechas: cambiamos al formato [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601).
  - Posesión y duelos ganados: Pasamos string de porcentaje a valor entre 0 y 1.
  - Penaltis en tanda: Pasamos a NULL el valor que está como false cuando el partido no se decide por tanda de penaltis.
  - Espacios en string: En todas las columnas categóricas eliminamos posibles espacios al principio y final.
  
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
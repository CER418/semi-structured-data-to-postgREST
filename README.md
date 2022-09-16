## JSON/CSV til database

Konverterer .json- eller .csv-filer til database (Postgresql), og oppretter RESTful API ved bruk av postgrest. 

### Installer dependencies

```shell
pip install -r requirements.txt
```

### Opprett Posetgresql database
Define schema og legg til bruker (krav for å ta i bruk postgrest)

```sql
grant usage on schema public to web_anon
grant select on public.cars to web_anon
```

### Kjør spørringer
[Dokumentasjon](https://postgrest.org/en/stable/api.html#resource-embedding)
```
http://localhost:3000/cars?Cylinders=eq.8
```

#### Todo
- Konverter alle tabellnavn til lowercase.
- SwaggerUI?
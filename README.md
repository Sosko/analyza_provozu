﻿# analyza_provozu
 
 Spuštění přes `docker-compose`
 
 Nachystané služby:
 
 * web - python-django - pro nahrávání souboru a jeho následné parsování (zatím se jen načtou pozice do db)
 * postgresql - databáze
 * swagger - pro náhled pro api - zatím k ničemu
 * swagger-editor - pro editování apoenapi
 * migration - pro nahrání struktur tabulek z django
 * pgadmin - pro přístup do databáze
 * grafana - zobrazování dat

Přístup k službám:
* web - http://localhost:8000
* pgadmin - http://localhost:8082
* swagger - http://localhost:8080
* swagger-editor - http://localhost:8081
* grafana - http://localhost:3000

Přihlašovací údaje:
* pgadmin - admin@admin.com:admin
* grafana - admin:admin
* postgresql - postgres:postgres


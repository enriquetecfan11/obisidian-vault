---
type: "resource"
tags:
  - postgresql
  - bases-de-datos
  - sql
  - devops
  - comandos
project: "none"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

# PostgreSQL

PostgreSQL, comúnmente conocido como Postgres, es un sistema de administración de bases de datos relacionales de código abierto y gratuito.

 Es posible que esté familiarizado con algunos otros sistemas de bases de datos similares, como MySQL, Microsoft SQL Server o MariaDB, que compiten con PostgreSQL.

Documentacion Postgre SQL → [https://www.postgresql.org/docs](https://www.postgresql.org/docs) || [https://www.educba.com/postgresql-cheat-sheet/](https://www.educba.com/postgresql-cheat-sheet/)

Tutoriales Postgre SQL → [https://www.postgresqltutorial.com/](https://www.postgresqltutorial.com/) 

PostgreSQL Cheat Sheet → [https://www.postgresqltutorial.com/postgresql-cheat-sheet/](https://www.postgresqltutorial.com/postgresql-cheat-sheet/)

Como instalar y utilizar PostgreSQL  → [https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-18-04-es](https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-18-04-es)

Postgres + Nodejs → [https://ed.team/blog/como-usar-bases-de-datos-postgres-con-nodejs](https://ed.team/blog/como-usar-bases-de-datos-postgres-con-nodejs)

### Comandos para hacer distintas acciones en las diferentes bases de datos:

- Para entrar en la base datos → sudo -i -u postgres
    - Y luego poner → psql (para poder entrar)
- Para entrar en una base de datos especifica → \c nombre de la base de datos
- List all databases from PostgreSQL server → \l+
- List all schema from PostgreSQL server → \dn+
- List all tablespaces from PostgreSQL server → \db+
- List all indexes from PostgreSQL server → \di+
- Para listar las tablas → \dt o \db+
- Para ver lo que hay dentro de una base de datos → \d+ nombre tabla
- Para ver lo que hay dentro de dicha tabla → TABLE nombre de tabla
- Eliminar tabla → DROP TABLE table name;
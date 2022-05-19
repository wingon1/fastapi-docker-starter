---
**bootstrapping our application**
```
docker-compose up -d --build
docker-compose up
```
---

**db 마이그레이션...** 
```
docker ps
docker exec -it {CONTAINER ID} bash
alembic upgrade head
```
---
db crate_main_tables 새로운 버젼 생성,...

```
docker ps
docker exec -it {CONTAINER ID} bash
alembic revision -m "create_main_tables"
```
---
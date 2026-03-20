# microservice-project

## Описание

2 Python HTTP-сервера + Nginx балансировщик нагрузки

## Запуск

```
git clone https://github.com/MihailMurdasov/microservice-project.git && cd microservice-project
```

```
sudo docker compose up --build
```

```
sudo docker compose ps
```

Ожидаемый вывод:
```
web1 Up (healthy)
web2 Up (healthy)
nginx-lb Up (healthy) 0.0.0.0:8080->80/tcp
```

```
curl http://localhost:8080/health # Ожидаемый вывод: OK
```

```
for i in {1..6}; do curl http://localhost:8080; echo; done
```

Ожидаемый вывод:
```
Hello from WEB1 (abc123...)
Hello from WEB2 (def456...)
Hello from WEB1 (abc123...)
```
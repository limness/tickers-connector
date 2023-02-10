# tickers-connector
Connector to an exchange to obtain quotes

### How to start 

``` bash
docker-compose up 
```

```bash
docker-compose up --build
``` 

### How to stop

```bash
docker-compose down 
```

### Container Logs

```bash
docker-compose logs --tail 777
```

* FastAPI: http://localhost:8000

---

#### Schema
```
.
└── Screener/
    ├── screener/
    │   ├── app/
    │   │   └── api.py
    │   ├── logs/
    │   │   └── .gitkeep
    │   ├── sockets/
    │   │   ├── base_ws.py
    │   │   ├── binance_ws.py
    │   │   └── okx_ws.py
    │   ├── constants.py
    │   ├── Dockerfile
    │   ├── feeds_factory.py
    │   ├── global_vars.py
    │   ├── req.txt
    │   ├── server.py
    │   └── utils.py
    ├── docker-compose.yml
    ├── .gitignore
    └── readme.md
```

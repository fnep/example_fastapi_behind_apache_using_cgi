# Run FastApi behind Apache with cgi

This is an example repository, to show how to run [FastAPI](https://fastapi.tiangolo.com/) behind [Apache HTTP Server](https://httpd.apache.org/) without reverse proxy, but using [mod_cgid](https://httpd.apache.org/docs/2.4/mod/mod_cgid.html) with a [venv](https://docs.python.org/3/library/venv.html) and the [WSGIMiddleware](https://github.com/abersheeran/a2wsgi) instead.

⚠️ This is definitely **not recommended** (for example because it's super slow), but in some cases, it is not an option or not wanted to run a separate server process (like using [Uvicorn](https://www.uvicorn.org/)) or to at least to [use wsgi](https://github.com/fnep/fastapi_behind_apache_using_wsgi). I just found it challenging to see if it works.

This example is in a [Docker container](https://www.docker.com/), so you can run it with:

```shell
> docker compose up
```

and check the result with:

```shell
> curl http://localhost:8080/api/
{"message":"Hello World 👋"}
```

… but it is more meant to be a documentation and one can install the same everywhere.

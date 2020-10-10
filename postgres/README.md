## Build instructions

Just build a regular Docker container, but you need to pass PostgreSQL's version number using the `PGVERSION` variable. Replace `<VERSION>` with the actual version number, such as `12` (default) or `13`.

```
$ docker build . -t postgres --build-arg PGVERSION=<VERSION>
```

Now tag the image appropriately, using the version number:

```
$ docker tag postgres postgres:<VERSION>
```

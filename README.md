# SteetSpectra App API backend

The API that powers StreetSpectra data services.

## Build instructions

Just build a regular Docker container.

```
$ docker build . -t streetspectra-app-api
```

Now tag the image appropriately, using the version number `<VERSION>`:

```
$ docker tag streetspectra-app-api streetspectra-app-api:<VERSION>
```

## Push instructions

If you want to push the image to your local microk8s repository:

```
$ docker save streetspectra-app-api:<VERSION> > /tmp/docker_image.tar
$ microk8s ctr image import /tmp/docker_image.tar

```

Or if you want to push the image to our ECR in AWS:

```
$ docker tag streetspectra-app-api:<VERSION> <COUNTID>.dkr.<AWSREGION>.amazonaws.com/streetspectra-app-api:<VERSION>
$ docker push <COUNTID>.dkr.<AWSREGION>.amazonaws.com/streetspectra-app-api:<VERSION>
```

# External access

## Preproduction
* api-pre.streetspectra.actionproject.eu

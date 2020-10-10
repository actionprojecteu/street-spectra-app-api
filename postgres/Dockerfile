LABEL maintainer="jgcasta@inspide.com"

ARG PGVERSION=12

FROM postgres:$PGVERSION

ARG PGVERSION=12

RUN apt-get update && apt-get install -y postgresql-$PGVERSION-postgis-3 postgresql-$PGVERSION-postgis-3-scripts pgxnclient build-essential postgresql-server-dev-$PGVERSION postgresql-common git cmake wget cron

RUN wget https://github.com/wal-g/wal-g/releases/download/v0.2.15/wal-g.linux-amd64.tar.gz && tar xvzf wal-g.linux-amd64.tar.gz -C /usr/local/bin && rm wal-g.linux-amd64.tar.gz

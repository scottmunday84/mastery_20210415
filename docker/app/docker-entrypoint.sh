#!/usr/bin/env bash
set -eo pipefail

pip install -r requirements.txt

if [ ! -f "/.db.setup" ]; then
  echo "Setup DB..."
  flask setupdb
  touch /.db.setup
  echo "DONE"
fi

echo "Starting up Flask..."
exec "$@"
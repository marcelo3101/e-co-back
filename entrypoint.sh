#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
  echo "loop"
done

echo "PostgreSQL started"

flask run -h 0.0.0.0
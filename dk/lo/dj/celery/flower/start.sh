#!/bin/bash

set -o errexit

set -o nounset

worker_ready(){
    celery -A real_estate inspect ping
}

until worker_ready; do
    >&2 echo 'Celery workers not available :-('
    sleep 1
done
>&2 echo 'Celery workers are available and ready... :-)'
sleep 1

flower \
    --app=real_estate \
    --broker="${CELERY_BROKER}"


#!/bin/bash
set -euo pipefail

case ${1:-} in
  jupyter)
  jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password=''
    ;;
  *)
    exec "$@"
    ;;
esac

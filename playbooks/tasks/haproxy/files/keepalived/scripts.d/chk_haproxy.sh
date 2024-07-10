#!/bin/bash
set -e

function do_ping() {
  wget -q -O /dev/null --server-response "http://127.0.0.1:9000/health" 2>&1 | awk '/^  HTTP/{print $2}'
}

ping_result=$(do_ping)
echo "Ping result: $ping_result"

if [ "$ping_result" = "200" ]; then
  exit 0
else
  exit 1
fi

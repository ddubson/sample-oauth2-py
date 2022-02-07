#!/bin/bash

JWT="$1"

curl --get -v --header "Authorization: Bearer ${JWT}" \
  "http://127.0.0.1:8001/messages" | \
  jq
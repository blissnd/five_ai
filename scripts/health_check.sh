#/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

while (true)
do
  output=$(curl localhost:5000 2>/dev/null)
  result=$?

  if [ $result -eq 0 ]; then
    echo  -e "${GREEN}Healthy"
  elif [ $result -ne 0 ]; then
    echo -e "${RED}Unhealthy!"
  fi
  echo -e "${NC}"  

  sleep 5
done


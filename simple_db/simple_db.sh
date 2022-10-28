#!/usr/bin/bash

db_set () {
    echo "$1, $2" >> database
}

db_get () {
    grep "^$1," database | sed -e "s/^$1,//" | tail -n 1    
}

"$@"

# ./simple_db.sh db_set 123456 '{"name":"London", "attractions":["Big Ben", "London Eye"]}'
# ./simple_db.sh db_get 123456
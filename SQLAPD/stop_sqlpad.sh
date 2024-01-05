#!/bin/bash

clear

#################################################
## Script to stop SQLPAD Container. From Jace ##
#################################################

echo "########################[ Warning ]#########################"
echo "# This is a script to stop SQLPAD. Do you want to proceed? #"
echo "############################################################"
echo ""

while true; do

        echo -n "Are you sure you want to stop SQLPAD? (Y/N) : "
        read Input

        case $Input in
                [Yy] )
                        echo ""
                        echo "Yes, exit SQLPAD."
                        echo ""
                        docker-compose down
                        echo ""
                        break
                        ;;
                [Nn] )
                        echo ""
                        echo "Yes, cancel exiting SQLPAD."
                        echo ""
                        break
                        ;;
                * )
                        echo ""
                        echo "Input Y or N"
                        echo ""
                        ;;
        esac
done
#!/bin/bash

clear

#################################################
## Script to start SQLPAD Container. From Jace ##
#################################################

## Environment Parameters ##
dockerComposeCount=$(docker-compose ps | wc -l)
logFileDate=$(date +%Y-%m-%d-%S)
sqlpadContainerLog="/log/sqlpad/sqlpad_output.log"
sqlpadContainerLogBak="/log/sqlpad/bak/sqlpad_output_$logFileDate.log"

echo "################################################"
echo "# This is a script that runs SQLPAD Container. #"
echo "################################################"
echo ""
echo "Before running SQLPAD, check the log file of SQLPAD."
echo "----------------------------------------------------"
echo ""
## Log Directory Check and Create ##
#if [ -e $sqlpadContainerLog ]; then
#       echo "The log file exists, and the file is backed up based on the current date."
#       mv /log/sqlpad/sqlpad_output.log /log/sqlpad/bak/sqlpad_output_$logFileMove.log
#       echo "Log file backup is complete, start SQLPAD..."
#       echo ""
#else
#       echo "Since the log file does not exist, the backup will be skipped and SQLPAD will be started."
#       echo ""
#fi

## Running SQLPAD Container ##
if [ ${dockerComposeCount} -le 2 ]; then
        echo "Run SQLPAD Container, and the log file location is $sqlpadContainerLog" 
        echo ""

        ## Log Directory Check and Create ##
        if [ -e $sqlpadContainerLog ]; then
                echo "The log file exists, and the file is backed up based on the current date."
                mv $sqlpadContainerLog $sqlpadContainerLogBak 
                echo "Log file backup is complete ($sqlpadContainerLogBak), start SQLPAD..."
                echo ""
        else
                echo "Since the log file does not exist, the backup will be skipped and SQLPAD will be started."
                echo ""
        fi

        docker-compose up -d
        echo ""
        nohup docker-compose logs -f sqlpad > /log/sqlpad/sqlpad_output.log 2>&1 &
        docker-compose ps
        echo ""
        exit 1
elif [ ${dockerComposeCount} -gt 2 ]; then
        echo "Since the SQLPAD Container is running, the script ends."
        echo ""
        docker-compose ps
        echo ""
        exit 1
fi
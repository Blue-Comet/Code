#!/bin/bash

## Create by Comet ##
## Zabbix Agent Auto Install Scripts ##

HOST=$(hostname)
PIP=$( curl -s 169.254.169.254/latest/meta-data/public-ipv4)

clear

sudo rpm -Uvh https://repo.zabbix.com/zabbix/5.2/rhel/8/x86_64/zabbix-release-5.2-1.el8.noarch.rpm

sudo dnf clean all

## SELinux Disabled
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

## Zabbix Agent Package Install
sudo dnf install zabbix-agent -y

## Zabbiz Agent Config File Backup
sudo cp /etc/zabbix/zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf_bak

## Swiching Zabbix Server Host 
## Example Zabbix Servr IP is 10.10.10.122
sudo sed -i 's/Server=127.0.0.1/Server=10.10.10.122/g' /etc/zabbix/zabbix_agentd.conf
sudo sed -i 's/ServerActive=127.0.0.1/ServerActive=10.10.10.122/g' /etc/zabbix/zabbix_agentd.conf

## Zabbix Auto Register Setting
sed -i 's/# HostMetadata=/HostMetadata=register/g' /etc/zabbix/zabbix_agentd.conf
sudo sed -i 's/# Hostname=/# Hostname=\n'Hostname=$PIP-VM-ASG'/g' /etc/zabbix/zabbix_agentd.conf
sudo sed -i 's/Hostname=Zabbix server/ /g' /etc/zabbix/zabbix_agentd.conf

## Enable Zabbix Agent
sudo systemctl enable zabbix-agent

## Reboot
sudo reboot

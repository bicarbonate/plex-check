import sys
import paramiko
import getpass


usr = 'plex'
passwd = 'password'
host = '192.168.15.212'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, username=usr, password=passwd)


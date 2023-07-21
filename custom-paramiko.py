import paramiko
import time

def  connect(server_ip, server_port, user, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=password, look_for_keys=False, allow_agent=False)
    
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout = 1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)
    
def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing the connection')
        ssh_client.close()


router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'user': 'naim', 'password': 'cisco'}        
client = connect(**router1)
shell = get_shell(client)

send_command(shell, 'enable')
send_command(shell, 'terminal length 0')
send_command(shell, 'show version')
send_command(shell, 'show ip interface brief')

output = show(shell)
print(output)
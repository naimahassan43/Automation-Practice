import paramiko
import time


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# creating dictionary for each device to connect to

router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'naim', 'password':'cisco'}
router2 = {'hostname': '10.1.1.20', 'port': '22', 'username': 'naim', 'password':'cisco'}
router3 = {'hostname': '10.1.1.30', 'port': '22', 'username': 'naim', 'password':'cisco'}

# creating a list of dictionaries (of devices)
routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["hostname"]}')

    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    # shell.send('cisco\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('show ip protocols\n')

    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)

    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
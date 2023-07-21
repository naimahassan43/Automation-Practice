import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'naim', 'password':'cisco'}
print(f'Connecting to {router["hostname"]}')

ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
shell = ssh_client.invoke_shell()


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
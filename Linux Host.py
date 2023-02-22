import paramiko

command = "ping -c 4 localhost"

cert = paramiko.RSAKey.from_private_key_file("redhat.cer")

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("54.146.210.46", username = "ec2-user", key_filename = "/Users/navaraj/PycharmProjects/Automation/redhat.cer" )
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()
del client, _stdin, _stdout, _stderr

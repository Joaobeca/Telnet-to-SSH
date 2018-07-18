
import telnetlib
from getpass import getpass

user = 'joao.beca'                      # Usuario utilizado para acessar o switch.
password = getpass()
host = ['1.1.1.1', '2.2.2.2']           # Lista de switches à alterar.
for i in host:
    telnet = telnetlib.Telnet(host=i)
    telnet.read_until(b'username: ')
    telnet.write(user.encode('ascii') + b'\n')
    telnet.read_until(b'password: ')                    # Pede o password para nao ser passado abertamente dentro do codigo.
    telnet.write(password.encode('ascii') + b'\n')
    hostname = telnet.write(b"conf t\n")                # Comandos passados ao switch.
    telnet.read_until(b"(config)#", timeout=5)
    telnet.write(b"ip domain name joaobeca.com\n")
    telnet.read_until(b"(config)#", timeout=5)
    telnet.write(b"crypto key generate rsa general-keys modulus 2048\n")
    telnet.read_until(b"(config)#", timeout=300)
    telnet.write(b"line vty 0 15\n")
    telnet.read_until(b"(config-line)#", timeout=5)
    telnet.write(b"transport input ssh\n")
    telnet.read_until(b"(config-line)#", timeout=5)
    telnet.write(b"exit\n")
    print(telnet.read_all().decode('ascii'))
    telnet.close()

print()
print("Execution finished!")

from ipaddress import ip_address
from subprocess import Popen, PIPE, STDOUT, call


def host_ping(hosts: iter) -> str:
    """
    Функция проверки доступности сетевых узлов.
    :hosts iter: объект, содержащий хосты или ip-адреса в строковом формате, которые необходимо проверить. Должен содержать метод __iter__
    :return: результат проверки
    """

    COMMAND = 'ping'
    for host in hosts:
        try:
            resp = call(f'{COMMAND} {ip_address(host)}', stdout=PIPE)
        except ValueError:
            resp = call(f'{COMMAND} {host}', stdout=PIPE)

        if resp == 0:
            print(f'Узел {host} доступен')
        else:
            print(f'Узел {host} недоступен')


if __name__ == '__main__':
    hosts = ('wikipedia.org', 'gb.ru', 'google.com', '192.168.100.1', '192.168.00.10')
    host_ping(hosts)

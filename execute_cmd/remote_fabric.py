# coding:utf8
# fabric:
#   website: https://www.fabfile.org/
#   install: pip install fabric

from fabric import Connection, SerialGroup


def fab1():
    """
    root用户，22端口，ssh 公钥访问
    """
    c = Connection("xxx.xxx.xxx.xxx")
    print(c.run("hostname").stdout.strip())


def fab2():
    """
    非root用户，非22端口，密码方式访问
    """
    c = Connection("xxx.xxx.xxx.xxx", user="abc", port=22000, connect_kwargs={"password": "xxxxxx"})
    print(c.run("hostname").stdout.strip())


def fab3():
    """
    多主机执行
    """
    result = SerialGroup('web1', 'web2').run('hostname')
    print(sorted(result.items()))


if __name__ == '__main__':
    fab1()
    fab2()
    fab3()

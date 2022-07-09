# coding:utf8
# https://docs.python.org/3.10/library/subprocess.html

import subprocess


def exec_cmd(cmd, output=False, ignore_error=False):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, shell=True)
    result = []
    for line in iter(p.stdout.readline, b""):
        result.append(line.decode("utf-8"))
        if output:
            print(line.decode("utf-8"))
        else:
            print("debug: {}".format(line.decode("utf-8")))

    p.stdout.close()
    p.wait()

    if p.returncode != 0 and not ignore_error:
        raise RuntimeError("[ERROR]")

    return result

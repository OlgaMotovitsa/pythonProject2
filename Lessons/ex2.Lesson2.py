import subprocess


def checkout(cmd, text):
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


if __name__ == '__main__':

        assert checkout("cat /etc/os-release", "22.04.1 LTS (Jammy Jellyfish)", print("FAIL"))






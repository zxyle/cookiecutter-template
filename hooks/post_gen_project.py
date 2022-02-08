import os


def remove_open_source_files():
    file_names = ["LICENSE"]
    for file_name in file_names:
        os.remove(file_name)

        
def git_init():
    cmd1 = 'git config --local user.name "{{ cookiecutter.author_name }}"'
    cmd2 = 'git config --local user.email "{{ cookiecutter.email }}"'
    try:
        os.system(cmd1)
        os.system(cmd2)
    except:
        pass


def main():
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()
    git_init()


if __name__ == "__main__":
    main()

#Dit is de main.py
from github import Github

def main():
    github = Github('https://github.com/laurensDSM/test_python.git')
    print(github.check_update())

if __name__ == "__main__":
    main()

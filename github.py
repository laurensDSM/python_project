import git
import os
import shutil

class Github():
    def __init__(self,repo_url):
        self.repo_url = repo_url

    def check_update(self):
        """Controleer de remote repo op een een config """
        local_directory = "temp_directory"
        repo = git.Repo.clone_from(self.repo_url, local_directory)
        response = None
        config_file_path = os.path.join(local_directory, "config", "config.txt")
        if os.path.exists(config_file_path):
            with open(config_file_path, "r") as file:
                response = file.read()
        repo.close()
        shutil.rmtree(local_directory)
        if response:
            return True
        else:
            return False
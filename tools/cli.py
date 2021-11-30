import os
import fire

from rich.console import Console
from git.cmd import Git

git = Git(os.getcwd())

console = Console()

class GitClient():
    """"""

    def git_status(self):
        """
        git status
        :return:
        """
        cmd = ['git', 'status']
        output = git.execute(cmd)
        console.log(output)
        # return output

    def git_push(self):
        """
        git push
        :return:
        """
        ...

    def git_log(self, *version_no):
        """
        git log
        :return:
        """
        ...



    def git_add(self, *args, **kwargs):
        """
        git add
        :return:
        """
        ...

    def git_diff(self, *version_no):
        """
        git diff
        :return:
        """
        cmd = ["git", "diff"]
        output = git.execute(cmd + list(version_no))
        console.print(output)


    def git_commit(self, *args, **kwargs):
        """
        git commit
        :return:
        """
        ...

    def git_stash(self, *args, **kwargs):
        """
        git stash
        :return:
        """
        ...

    def git_stash_pop(self, *args, **kwargs):
        """
        git stash pop
        :return:
        """
        ...

if __name__ == '__main__':
    fire.Fire(GitClient)


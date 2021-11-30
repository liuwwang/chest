import os
import fire

from git.cmd import Git
from rich.console import Console

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

    @classmethod
    def git_diff(cls, *args):
        """
        git diff
        :return:
        """
        cmd = ["git", "diff"]
        return git.execute(cmd + list(args) + ["--stat"])

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

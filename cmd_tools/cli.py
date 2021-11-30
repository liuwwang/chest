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
        return git.execute(cmd)

    def git_push(self, *args):
        """
        git push
        :return:
        """
        cmd = ['git', 'push']
        return git.execute(cmd + list(args))

    def git_log(self):
        """
        git log
        :return:
        """
        cmd = ['git', 'log']
        return git.execute(cmd)

    def git_add(self, *args):
        """
        git add
        :return:
        """
        cmd = ['git', 'add'] + list(args)
        return git.execute(cmd)

    @classmethod
    def git_diff(cls, *args):
        """
        git diff
        :return:
        """
        cmd = ["git", "diff"]
        return git.execute(cmd + list(args) + ["--stat"])

    def git_commit(self, message):
        """
        git commit
        :return:
        """
        cmd = ['git', 'commit', '-m', message]
        return git.execute(cmd)

    def git_stash(self):
        """
        git stash
        :return:
        """
        cmd = ['git', 'stash']
        return git.execute(cmd)


    def git_stash_pop(self):
        """
        git stash pop
        :return:
        """
        cmd = ['git', 'stash', 'pop']
        return git.execute(cmd)

if __name__ == '__main__':
    fire.Fire(GitClient)

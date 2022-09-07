import os
import fire

from git.cmd import Git
from rich.console import Console

git = Git(os.getcwd())

console = Console()


class GitClient:
    """"""
    @staticmethod
    def git_status():
        """
        git status
        :return:
        """
        cmd = ['git', 'status']
        return git.execute(cmd)

    @staticmethod
    def git_push(*args):
        """
        git push
        :return:
        """
        cmd = ['git', 'push']
        return git.execute(cmd + list(args))

    @staticmethod
    def git_log():
        """
        git log
        :return:
        """
        cmd = ['git', 'log']
        return git.execute(cmd)

    @staticmethod
    def git_add(*args):
        """
        git add
        :return:
        """
        cmd = ['git', 'add'] + list(args)
        return git.execute(cmd)

    @staticmethod
    def git_diff(*args):
        """
        git diff
        :return:
        """
        cmd = ["git", "diff"]
        return git.execute(cmd + list(args) + ["--stat-width=200"])

    @staticmethod
    def git_commit(message):
        """
        git commit
        :return:
        """
        cmd = ['git', 'commit', '-m', message]
        return git.execute(cmd)

    @staticmethod
    def git_stash():
        """
        git stash
        :return:
        """
        cmd = ['git', 'stash']
        return git.execute(cmd)

    @staticmethod
    def git_stash_pop():
        """
        git stash pop
        :return:
        """
        cmd = ['git', 'stash', 'pop']
        return git.execute(cmd)


if __name__ == '__main__':
    fire.Fire(GitClient)

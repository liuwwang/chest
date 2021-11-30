import os
import fire
import shutil
import tarfile

from conf import config
from cli import GitClient
from utils import cal_time, console

dir_path = os.getcwd()


class IncrementLoader:
    """
    增量制作
    """

    def main(self, *args):
        """
        主入口
        :return:
        """
        console.log("Start to Deal")
        new_dir = config.get("target_path")
        self.check_dir_exists(new_dir)

        with cal_time("Execute git diff"):
            df_files = GitClient.git_diff(*args)
            console.log(df_files)
            change_list = [i.split(" ")[1] for i in df_files.split("\n") if
                           i.split(" ")[1] not in config.get("ignore_files")]
            change_list.pop()
            change_file_list = list((map(lambda x: new_dir + "/" + x, change_list)))

        with cal_time("Check new file exists"):
            for change_file in change_file_list:
                file_path, _ = change_file.rsplit("/", 1)
                self.check_dir_exists(file_path)

        with cal_time("Cp file to target dir"):
            for file_name in change_list:
                try:
                    shutil.copyfile(file_name, new_dir + "/" + file_name)
                except Exception as e:
                    if os.path.exists(file_name):
                        console.log(f"Error log: failed to cp file, reason<{e}>")

        with cal_time("Make tar package"):
            self.make_tar("upgrade.tar", new_dir)

        console.log("Make package done")

    @staticmethod
    def check_dir_exists(file_path):
        """
        检测dir是否存在
        :param file_path:
        :return:
        """
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        return

    @staticmethod
    def make_tar(tar_name, source_dir):
        with tarfile.open(tar_name, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        return


if __name__ == '__main__':
    fire.Fire(IncrementLoader)

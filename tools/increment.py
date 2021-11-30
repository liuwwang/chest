"""
制作本地增量包
深度搜索目标文件夹目录
对比目标文件与原文件是否相同，如果不同，将目标文件移入对应升级包目录中
TIPS:
    可能存在相同名称的文件，导致搜索的文件路径不同，搜寻目标文件时，需要填写目标文件基于项目根目录的相对路径
    本地有可能存在改动的文件，不需要提交的，需要提前设置忽略文件，如配置文件等。
"""
from conf import config

import os
import fire
import shutil
import filecmp
from rich import print

DIR_PATH = os.getcwd()


class UpgradeIncrementPackage(object):
    """
    制作增量升级包
    """

    @staticmethod
    def deal_file_path(rf_path, nf_path, file_name):
        """

        :return:
        """
        return (rf_path + file_name, nf_path + file_name)

    # 检测两个文件是否不同
    @staticmethod
    def check_file(raw_file: str, new_file: str):
        try:
            is_file_diff = filecmp.cmp(raw_file, new_file)
        except Exception as e:
            is_file_diff = False
            print(f"cmp fail, reason:{e}")
        return is_file_diff

    @staticmethod
    def check_dir_or_file_exists(file_cwd):
        """
        检测文件夹或文件是否存在
        :return:
        """
        # 递归检测
        dir_list = file_cwd.split("/")

    def main(self, split_cwd):
        """
        主方法入口
        :return:
        """
        rf_path, nf_path, sf_path, ignore_files = config.values()

        select_path_list = [self.deal_file_path(rf_path, nf_path, _) for _ in sf_path]
        for _ in select_path_list:
            rf, nf = _[0], _[1]
            is_diff = self.check_file(rf, nf)
            if not is_diff:
                continue
            file_cwd, file_pwd = rf.rsplit(split_cwd, 1)
            self.check_dir_or_file_exists(file_pwd)

    @staticmethod
    def move_file_target_dir(file_name, target_file):
        """
        移动文件至目标文件夹下
        :return:
        """
        shutil.move(file_name, target_file)
        ...

    def select_file(self, raw_file, new_file):
        """扫描文件"""
        ...

    def make_catalogue_tree(self):
        """扫描原文件夹，生成目录树"""
        ...


if __name__ == '__main__':
    fire.Fire(UpgradeIncrementPackage)

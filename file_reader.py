import os
import pyperclip
from common import Common
from prompt_toolkit import print_formatted_text # prompt_toolkitでprintするため

class FileReader(object):
    """
    テンプレートを呼び出しクリップボードにコピーする
    """

    @classmethod
    def copy_template_to_clip_board(cls, template_name) -> None:
        """
        指定したテンプレートのテンプレーをクリップボードにコピーする
        """
        # テンプレートを取得し、クリップボードにコピー
        txt = cls.get_template(template_name)
        print_formatted_text("***************copied***************")
        print_formatted_text(txt)
        print_formatted_text("************************************")
        pyperclip.copy(txt)

    @classmethod
    def get_template(cls, template_name: str) -> str:
        """
        指定したテンプレートの文章を取得
        """
        with open(os.path.join(Common.TEMPLATE_PATH, template_name + ".txt"), 'r', encoding="utf-8") as f:
            txt = f.read()
        return txt



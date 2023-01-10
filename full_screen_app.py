import os
import re
from file_reader import FileReader
from common import Common
from typing import List
from prompt_toolkit import Application
from prompt_toolkit.application import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout import Layout, FormattedTextControl
from prompt_toolkit.layout.dimension import LayoutDimension
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text

from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous

class FullScreenApp(object):
    """
    全画面アプリケーションクラス
    """
    # テンプレートのディレクトリ

    # キーバインディング
    kb = KeyBindings()

    # フォント
    text_style = Style.from_dict({
        "main": '#FF9D00 underline bold',
    })

    @classmethod
    def get_file_name(cls):
        """
        template/配下の.txtのファイル名を取得
        """
        file_names: List[str] = []
        regex = re.compile(r'(.txt)$')
        for file in os.listdir(Common.TEMPLATE_PATH):
            if os.path.isfile(os.path.join(Common.TEMPLATE_PATH, file)):
                file_name, ext = os.path.splitext(file)
                if ext == ".txt":
                    file_names.append(file_name)
        return file_names

    # テンプレート一覧を取得(仮)
    @classmethod
    def get_templates_list(cls) -> List[Window]:
        template_names: List[str] = cls.get_file_name()
        templates: List[Window] = []
        for template_name in template_names:
            obj = Window(height=LayoutDimension.exact(1), content=FormattedTextControl(template_name, focusable=True))
            templates.append(obj)
        return templates

    @classmethod
    def get_windows(cls) -> List[Window]:
        windows:List[Window] = []

        main_str = Window(height=LayoutDimension.exact(1), content=FormattedTextControl("Select Template(Use arrow keys to move and press Enter to select)", focusable=False), style="class:main")
        windows.append(main_str)
        windows.extend(cls.get_templates_list())
        return windows


    # テンプレの一覧表示
    @classmethod
    def get_root_container(cls) -> HSplit:
        return HSplit(cls.get_windows())

    # 実行関数
    @classmethod
    def run(cls):
        app = Application(
            layout=Layout(cls.get_root_container()),
            key_bindings=cls.kb,
            full_screen=True,
            style=cls.text_style
        )
        app.run()

    ## [Ctrl + Q]アプリケーション終了
    @kb.add(Keys.ControlC)
    def exit_(event):
        """
        Pressing Ctrl-C will exit the user interface.

        Setting a return value means: quit the event loop that drives the user
        interface and return this value from the `Application.run()` call.
        """
        event.app.exit()
        print_formatted_text('exit app')

    ## [↑キー]カーソルを上に移動
    @kb.add(Keys.Up)
    def move_cursor_up_(event):
        """
        Pressing key up will focus previous item.
        """
        get_app().layout.focus_previous()

    ## [↓キー]カーソルを下に移動
    @kb.add(Keys.Down)
    def move_cursor_down_(event):
        """
        Pressing key up will focus next item.
        """
        get_app().layout.focus_next()

    ## [Enter]クリップボードにテンプレートをコピー
    @kb.add(Keys.Enter)
    def copy_template_to_clipboard_(event):
        """
        Pressing enter key will focus next item.
        """
        # 選択されたテンプレート名文字列を取得
        current_template = get_app().layout.current_window.content.text
        FileReader.copy_template_to_clip_board(current_template)
        print_formatted_text('copied templatename: {0}'.format(current_template))
        event.app.exit()
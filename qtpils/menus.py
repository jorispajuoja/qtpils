"""Module to create a PyQt menus"""
from qtpy.QtWidgets import QAction, QMainWindow, QMenu, QMenuBar


class Menu(QMenu):
    """Create Qmenu, add it to QMenuBar"""

    def __init__(self, menu_name: str, menu_bar: QMenuBar, **properties):
        """Create a QMenu, add it to a QMenuBar

        Args:
            menu_name (str): Set menu name and set object name menu_nameMenu
            menu_bar (QMenuBar): Add menu to this QMenuBar
        """
        super().__init__(**properties)
        self.setObjectName(f"{menu_name}Menu")
        self.setTitle(menu_name)
        menu_bar.addAction(self.menuAction())


class MenuAction(QAction):
    """Create a QAction, add it to QMenu"""

    def __init__(self, action_name: str, parent_menu: QMenu, **properties):
        """Create a QAction, add it to QMenu, connect a funtion

        Args:
            action_name (str): Menu text, also set object name action_nameAction
            parent_menu (QMenu): Menu to which to add the MenuAction
        """
        super().__init__(**properties)
        self.setObjectName(f"{action_name}Action")
        self.setText(action_name)
        parent_menu.addAction(self)


class MenuBar(QMenuBar):
    """Create a menubar, add it to QMainWindow"""

    def __init__(self, target: QMainWindow, **properties):
        """Create a QMenuBar

        Args:
            target (QMainWindow): set Menubar to this QMainwindow
        """
        super().__init__(**properties)
        target.setMenuBar(self)

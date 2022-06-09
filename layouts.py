"""Module to create and apply QLayout versions to a Qwidget"""
from typing import Optional
from qtpy.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QLayout,
    QVBoxLayout,
    QGroupBox,
    QGridLayout,
    QStackedLayout,
    QStackedWidget,
    QWidget,
)
from .construct import add_widget_to_layout


class CentralWidget(QWidget):
    """set a central widget to a QMainWindow"""

    def __init__(self, target: QMainWindow):
        """Set a central widget to a QMainWindow

        Args:
            target (QMainWindow): Set central widget to this QMainWindow instance
        """
        super().__init__()
        target.setCentralWidget(self)


class GridLayout(QGridLayout):
    """apply a gridlayout to target widget"""

    def __init__(self, layout_name: str, target: QWidget, **properties):
        """Apply QGridLayout to target widget

        Args:
            layout_name (str): set object name to layout_nameGridLayout
            target (QWidget): target to which apply the layout
        """
        super().__init__(**properties)
        self.setObjectName(f"{layout_name}GridLayout")
        target.setLayout(self)


class GroupBox(QGroupBox):
    def __init__(
        self,
        group_box_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        **properties,
    ):
        super().__init__(**properties)
        self.setObjectName(f"{group_box_name}GroupBox")
        add_widget_to_layout(self, target_layout, position)


class HBoxLayout(QHBoxLayout):
    """Apply QHBoxLayout to target widget"""

    def __init__(self, layout_name: str, target: QWidget, **properties):
        """Apply QHBoxLayout to target widget

        Args:
            layout_name (str): set object name to layout_nameHBoxLayout
            target (QWidget): target to which apply the layout
        """
        super().__init__(**properties)
        self.setObjectName(f"{layout_name}HBoxLayout")
        target.setLayout(self)


class StackedLayout(QStackedLayout):
    """Apply QStackedLayout to target widget"""

    def __init__(self, layout_name: str, target: QWidget, **properties):
        """Apply QStackedLayout to target widget

        Args:
            layout_name (str): set object name to layout_nameStackedLayout
            target (QWidget): target to which apply the layout
        """
        super().__init__(**properties)
        self.setObjectName(f"{layout_name}StackedLayout")
        target.setLayout(self)


class StackedWidget(QStackedWidget):
    def __init__(
        self,
        stack_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        **properties,
    ):
        super().__init__(**properties)
        self.setObjectName(f"{stack_name}StackedWidget")
        add_widget_to_layout(self, target_layout, position)


class VBoxLayout(QVBoxLayout):
    """Apply QVBoxLayout to target widget"""

    def __init__(self, layout_name: str, target: QWidget, **properties):
        """Apply QVBoxLayout to target widget

        Args:
            layout_name (str): set object name to layout_nameVBoxLayout
            target (QWidget): target to which apply the layout
        """
        super().__init__(**properties)
        self.setObjectName(f"{layout_name}VBoxLayout")
        target.setLayout(self)

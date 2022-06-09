""""Module to create a QWidgets and add them to a layout"""
from typing import Optional

from qtpy.QtCore import QDateTime, QRegExp, Qt
from qtpy.QtGui import QRegExpValidator
from qtpy.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDoubleSpinBox,
    QLabel,
    QLayout,
    QLCDNumber,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QTableWidget,
)

from .construct import add_item_to_layout, add_widget_to_layout


class Button(QPushButton):
    """Create a QPushButton and add it to a layout"""

    def __init__(
        self,
        button_text: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        **properties,
    ):
        """Create a QPushButton, add it to a layout, connect a function

        Args:
            button_text (str): set button text, and set object name as textButton
            target_layout (QLayout): set layout to which the button should be added
            function (Callable): add a function to clicked, button_text is passed as an argument by default
            position (Optional[list], optional): when using QGridLayout add the position [y,x,yspan,xspan]. Defaults to None.
            func_args (Optional[list], optional): add extra arguments that should be passed to the function. Defaults to None.
            text_arg (bool, optional): set to False if button_text should not be passed as an argument. Defaults to True.
            custom_class (Type, optional): add an optional custom QPushButton class. Defaults to None.
        """
        super().__init__(**properties)
        self.setObjectName(f"{button_text}Button")
        self.setText(button_text)
        add_widget_to_layout(self, target_layout, position)


class ComboBox(QComboBox):
    """Create a QComboBox"""

    def __init__(
        self,
        box_name: str,
        target_layout: QLayout,
        item_list: list,
        position: Optional[list] = None,
        **properties,
    ):
        """Create a QComboBox, add to layout, set list, add function to textActivated

        Args:
            box_name (str): Object name as box_nameComboBox
            target_layout (QLayout): add ComboBox to this layout
            item_list (list): list of items in ComboBox
            position (Optional[list], optional): When using QGridLayout add position [y,x,yspan,xspan]. Defaults to None.
            function (Optional[Callable], optional): add function with textActivated, pass current text as argument. Defaults to None.
            func_args (Optional[list], optional): add other arguments to be passed to the function. Defaults to None.
            text_arg (bool, optional): set to False in case currentText() should not be passed as an argument. Defaults to True.
        """
        super().__init__(**properties)
        self.setObjectName(f"{box_name}ComboBox")
        for i in item_list:
            self.addItem(i)
        add_widget_to_layout(self, target_layout, position)


class DateEdit(QDateEdit):
    """Create a QDateEdit, add it to layout"""

    def __init__(
        self,
        date_edit_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        **properties,
    ):
        """Create a QDateEdit, add it to layout, optionally connect a function to dateChanged

        Args:
            date_edit_name (str): set object name to date_edit_nameDateEdit
            target_layout (QLayout): add DateEdit to this layout
            position (Optional[list], optional): When using QGridLayout [y,x,yspan,xspan]. Defaults to None.
            function (Optional[Callable], optional): Connect function to dateChanged, pass date() as argument. Defaults to None.
            func_args (Optional[list], optional): add other arguments to funcion. Defaults to None.
            text_arg (bool, optional): set to False if date() should not be passed as argument. Defaults to True.
        """
        super().__init__(**properties)
        self.setObjectName(f"{date_edit_name}DateEdit")
        self.setCalendarPopup(True)
        self.setDateTime(QDateTime.currentDateTime())
        add_widget_to_layout(self, target_layout, position)


class DoubleSpinBox(QDoubleSpinBox):
    """Create a QDoubleSpinBox, add it to layout"""

    def __init__(
        self,
        spinbox_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        single_step: float = 0.1,
        decimals: int = 1,
        maximum: int = 999,
        **properties,
    ):
        """Create a QDoubleSpinBox, add it to layout

        Args:
            spinbox_name (str): set object name to spinbox_nameDoubleSpinBox
            target_layout (QLayout): add DoubleSpinBox to layout
            single_step (float, optional): set single step. Defaults to 0.1.
            decimals (int, optional): set amount of decimals. Defaults to 1.
            maximum (int, optional): set maximum number. Defaults to 999.
            position (Optional[list], optional): when using QGridLayout [y,x,yspan,xspan]. Defaults to None.
        """
        super().__init__(**properties)
        self.setObjectName(f"{spinbox_name}DoubleSpinBox")
        self.setSingleStep(single_step)
        self.setDecimals(decimals)
        self.setMaximum(maximum)
        add_widget_to_layout(self, target_layout, position)


class Label(QLabel):
    """Create QLabel, add it to layout"""

    def __init__(
        self,
        label_text: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        alignment: str = "left",
        **properties,
    ):
        """Create a QLabel, add it to layout

        Args:
            label_text (str): label text, and set object name label_textLabel
            target_layout (QLayout): add Label to this layout
            alignment (str, optional): set Label alignment as left | l or center | c or right | r. Defaults to "left".
            position (Optional[list], optional): when using QGridLayout [y,x,yspan,xspan]. Defaults to None.
        """
        super().__init__(**properties)
        self.setObjectName(f"{label_text}Label")
        self.setText(label_text)
        match alignment.lower():
            case "left" | "l":
                self.setAlignment(Qt.AlignLeft)
            case "right" | "r":
                self.setAlignment(Qt.AlignRight)
            case "center" | "c":
                self.setAlignment(Qt.AlignCenter)
        add_widget_to_layout(self, target_layout, position)


class LCD(QLCDNumber):
    """Create a QLCDNumner, add it to layout"""

    def __init__(
        self,
        lcd_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        **properties,
    ):
        """Create a QLCDNumber widget, add it to layout

        Args:
            lcd_name (str): set object name lcd_nameLCD
            target_layout (QLayout): add LCD to layout
            position (Optional[list], optional): When using QGridLayout [y,x,yspan,xspan]. Defaults to None.
        """
        super().__init__(**properties)
        self.setObjectName(f"{lcd_name}LCD")
        add_widget_to_layout(self, target_layout, position)


class LineEdit(QLineEdit):
    """Create QLineEdit, add it to layout"""

    def __init__(
        self,
        line_edit_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        regex_rule: str = None,
        **properties,
    ):
        """Create QLineEdit, add it to layout, add an optional regex validator

        Args:
            line_edit_name (str): set object name line_edit_nameLineEdit
            target_layout (QLayout): add LineEdit to layout
            regex_rule (str, optional): add regex validator, enter regex as string. Defaults to None.
            position (Optional[list], optional): when using QgridLayout [y,x,yspan,xspan]. Defaults to None.
        """
        super().__init__(**properties)
        self.setObjectName(f"{line_edit_name}LineEdit")
        if regex_rule:
            regex = QRegExp(regex_rule)
            validator = QRegExpValidator(regex)
            self.setValidator(validator)
        add_widget_to_layout(self, target_layout, position)


class SpacerItem(QSpacerItem):
    """Create a QSpacerItem, add it to layout"""

    def __init__(
        self,
        target_layout: QLayout,
        position: Optional[list] = None,
        h_size: int = 1,
        v_size: int = 1,
        h_expand: bool = False,
        v_expand: bool = False,
    ):
        """Create a QSpacerItem, add it to layout

        Args:
            target_layout (QLayout): add to layout
            h_size (int, optional): horizontal size. Defaults to 1.
            v_size (int, optional): vertical size. Defaults to 1.
            h_expand (bool, optional): expand horizontally. Defaults to False.
            v_expand (bool, optional): expand vertically. Defaults to False.
            position (Optional[list], optional): when using QGridLayout [y,x,yspan,xspan]. Defaults to None.
        """
        arguments = [h_size, v_size, QSizePolicy.Minimum, QSizePolicy.Minimum]
        if h_expand:
            arguments[2] = QSizePolicy.Expanding
        if v_expand:
            arguments[3] = QSizePolicy.Expanding
        super().__init__(*arguments)
        add_item_to_layout(self, target_layout, position)


class SpinBox(QSpinBox):
    """Create a QSpinBox, add it to layout"""

    def __init__(
        self,
        spinbox_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        **properties,
    ):
        """Create a QSpinBox, add it to layout

        Args:
            spinbox_name (str): set object name spinbox_nameSpinBox
            target_layout (QLayout): add to layout
            maximum (int, optional): maximum number. Defaults to 999.
            position (Optional[list], optional): when using QGridLayout [y,x,yspan,xspan]. Defaults to None.
        """
        super().__init__(**properties)
        self.setObjectName(f"{spinbox_name}SpinBox")
        add_widget_to_layout(self, target_layout, position)


class TableWidget(QTableWidget):
    """Create a QTableWidget, add it to layout"""

    def __init__(
        self,
        table_widget_name: str,
        target_layout: QLayout,
        position: Optional[list] = None,
        **properties,
    ):
        """Create a QTableWidget, add it to layout

        Args:
            table_widget_name (str): set object name table_widget_nameTableWidget
            target_layout (QLayout): add to layout
            position (Optional[list], optional): when using QGridLayout [y,x,yspan,xspan]. Defaults to None.
        """
        super().__init__(**properties)
        self.setObjectName(table_widget_name)
        add_widget_to_layout(self, target_layout, position)

"""module for functions that are used to build the QWidgets."""

from typing import Optional

from qtpy.QtWidgets import QLayout, QWidget


def add_widget_to_layout(
    widget: QWidget, layout: QLayout, position: Optional[list]
) -> None:
    """Add widget to target layout

    Args:
        widget (QWidget): Widget to be added to target QLayout
        layout (QLayout): Target QLayout that the widget is added to
        position (Optional[list]): when using QGridLayout add the position [y,x,yspan,xspan].

    Returns:
        None: adds widget to layout
    """
    if position:
        final_position = [0, 0, 1, 1]
        for index, value in enumerate(position):
            final_position[index] = value
        return layout.addWidget(
            widget,
            final_position[0],
            final_position[1],
            final_position[2],
            final_position[3],
        )
    return layout.addWidget(widget)


def add_item_to_layout(
    widget: QWidget, layout: QLayout, position: Optional[list]
) -> None:
    """add an QItem to target layout

    Args:
        widget (QWidget): Item to be added to target QLayout
        layout (QLayout): Target QLayout that the item is added to
        position (Optional[list]): when using QGridLayout add the position [y,x,yspan,xspan].

    Returns:
        None: adds item to layout
    """
    if position:
        final_position = [0, 0, 1, 1]
        for index, value in enumerate(position):
            final_position[index] = value
        return layout.addItem(
            widget,
            final_position[0],
            final_position[1],
            final_position[2],
            final_position[3],
        )
    return layout.addItem(widget)

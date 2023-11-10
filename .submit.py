import os
import time
import ipywidgets as widgets
from IPython.display import display, Javascript


if __name__ == "__main__":
    # Submit button code
    link_view = widgets.Output()

    @link_view.capture(clear_output=True)
    def callback(url):
        display(Javascript(data=f'window.open("{url.tooltip}");'))

    button = widgets.Button(
        description="Submit Exercise",
        tooltip='https://openjupyter-demox.xopic.de/services/grading-service/',
        button_style='success'
    )
    button.on_click(callback)
    display(button, link_view)

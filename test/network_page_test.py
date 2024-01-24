import pathlib

from pytestqt.qtbot import QtBot

from main_window import MainWindow
from client import send_flow


def describe_network_page():
    def it_displays_a_flow_received(qtbot: QtBot):  # type: ignore
        main_window = MainWindow(pathlib.Path("./assets"))
        send_flow()

        main_window.show()
        qtbot.waitExposed(main_window)
        # TODO: Instead should wait for the signal to be received
        qtbot.wait(500)

        table_model = main_window.network_page.ui.flowTableContainer.table_model
        assert table_model.rowCount() == 1
        assert table_model.data(table_model.index(0, 0)) == "1234"
        assert table_model.data(table_model.index(0, 1)) == "http"
        assert table_model.data(table_model.index(0, 2)) == "192.168.0.2"
        assert table_model.data(table_model.index(0, 3)) == "192.168.0.1"
        assert table_model.data(table_model.index(0, 4)) == "TODO"
        assert table_model.data(table_model.index(0, 5)) == "TODO"

        main_window.about_to_quit()
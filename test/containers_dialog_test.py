from PySide6 import QtCore, QtWidgets
from unittest.mock import patch
from pytestqt.qtbot import QtBot
from event_bus_global import EventBusGlobal

from network.widgets.containers_dialog import ContainersDialog
from factories.container_factory import ContainerFactory


def describe_containers_dialog():
    def it_displays_the_containers(qtbot: QtBot):  # type: ignore
        # Setup
        container1 = ContainerFactory.build()
        container2 = ContainerFactory.build(intercepted=True)

        # Subject
        with patch("network.widgets.containers_dialog.ContainerRepo") as MockContainerRepo:
            mock_repo = MockContainerRepo.return_value
            mock_repo.get_all.return_value = [container1, container2]
            widget = ContainersDialog()
        widget.about_to_quit()

        # Assert
        table_model = widget.table_model
        check_state = QtCore.Qt.ItemDataRole.CheckStateRole
        assert table_model.rowCount() == 2
        assert table_model.data(table_model.index(0, 0)) == container1.short_id
        assert table_model.data(table_model.index(0, 1)) == container1.image
        assert table_model.data(table_model.index(0, 2)) == container1.ip
        assert table_model.data(table_model.index(0, 3)) == container1.name
        assert table_model.data(table_model.index(0, 4)) == container1.status
        assert table_model.data(table_model.index(0, 5), check_state) == QtCore.Qt.CheckState.Unchecked

        assert table_model.data(table_model.index(1, 0)) == container2.short_id
        assert table_model.data(table_model.index(1, 1)) == container2.image
        assert table_model.data(table_model.index(1, 2)) == container2.ip
        assert table_model.data(table_model.index(1, 3)) == container2.name
        assert table_model.data(table_model.index(1, 4)) == container2.status
        assert table_model.data(table_model.index(1, 5), check_state) == QtCore.Qt.CheckState.Checked

    def it_sends_the_selected_container_ids_to_the_agent(qtbot: QtBot):  # type: ignore
        # Setup
        container1 = ContainerFactory.build()
        container2 = ContainerFactory.build()

        with patch("network.widgets.containers_dialog.ContainerRepo") as MockContainerRepo:
            mock_repo = MockContainerRepo.return_value
            mock_repo.get_all.return_value = [container1, container2]
            widget = ContainersDialog()

        # select a container from the table
        cell_center = get_table_cell_center(widget.ui.containersTable, 1, 5)
        qtbot.mouseClick(widget.ui.containersTable.viewport(), QtCore.Qt.MouseButton.LeftButton, pos=cell_center)

        container_ids_from_signal = []

        def capture_signal(container_ids: list[str]) -> bool:
            nonlocal container_ids_from_signal
            container_ids_from_signal = container_ids
            return True

        # Subject
        signal = EventBusGlobal.get().intercept_containers
        with qtbot.waitSignal(signal, timeout=1000, check_params_cb=capture_signal):
            button = widget.ui.saveButton
            qtbot.mouseClick(button, QtCore.Qt.MouseButton.LeftButton, pos=button.rect().center())

        # Assert
        assert container_ids_from_signal == [container2.short_id]
        widget.about_to_quit()


def get_table_cell_center(table_view: QtWidgets.QTableView, row: int, column: int):
    cell_rect = table_view.visualRect(table_view.model().index(row, column))
    return cell_rect.center()

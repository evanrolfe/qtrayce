import typing
from PyQt6 import QtCore, QtWidgets, QtGui, Qsci

from network.ui_network_page import Ui_NetworkPage


class NetworkPage(QtWidgets.QWidget):
    send_flow_to_editor = QtCore.pyqtSignal(object)
    send_flow_to_fuzzer = QtCore.pyqtSignal(object)

    def __init__(self, *args: typing.Any, **kwargs: typing.Any):
        super(NetworkPage, self).__init__(*args, **kwargs)

        self.ui = Ui_NetworkPage()
        self.ui.setupUi(self)

        # Theme colours
        default_bg = "#1E1E1E"
        default_color = "#EEFFFF"
        # darker_color = "#545454"
        # key_color = "#C792EA"
        # value_color = "#C3E88D"
        # number_color = "#FF5370"
        # operator_color = "#569CD6"
        # invalid_color = "#f14721"
        # selected_secondary_color = "#4E5256"
        # other_color = "#FFCB6B"
        # bg_dark = "#252526"
        # bg_input = "#404040"
        # bg_input_hover = "#3A3A3A"

        self.ui.requestText.setPaper(QtGui.QColor(default_bg))
        self.ui.requestText.setColor(QtGui.QColor(default_color))
        self.ui.requestText.setCaretForegroundColor(QtGui.QColor(default_color))
        self.ui.requestText.setMarginsForegroundColor(QtGui.QColor(default_color))
        self.ui.requestText.setMarginsBackgroundColor(QtGui.QColor(default_bg))

        self.ui.responseText.setPaper(QtGui.QColor(default_bg))
        self.ui.responseText.setColor(QtGui.QColor(default_color))
        self.ui.responseText.setCaretForegroundColor(QtGui.QColor(default_color))
        self.ui.responseText.setMarginsForegroundColor(QtGui.QColor(default_color))
        self.ui.responseText.setMarginsBackgroundColor(QtGui.QColor(default_bg))

        self.ui.requestText.setUtf8(True)
        self.ui.requestText.setAutoIndent(True)
        self.ui.requestText.setIndentationsUseTabs(False)
        self.ui.requestText.setIndentationWidth(4)
        self.ui.requestText.setIndentationGuides(True)
        self.ui.requestText.setBackspaceUnindents(True)
        self.ui.requestText.setEdgeColumn(79)
        self.ui.requestText.setMarginWidth(0, 0)
        self.ui.requestText.setBraceMatching(Qsci.QsciScintilla.BraceMatch.SloppyBraceMatch)
        # ui.requestText->setMarginLineNumbers(0, true);

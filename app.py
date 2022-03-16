from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from keyrandom import Randomizer
from util import clean
import constants


class AboutTab(QtWidgets.QWidget):
    def __init__(self, p):
        super(AboutTab, self).__init__(p)
        self.vlay = QtWidgets.QVBoxLayout(self)
        self.vlay.setContentsMargins(55, 55, 55, 55)
        self.vlay.setAlignment(Qt.AlignHCenter)

        self.keyrandomizer = QtWidgets.QLabel("KeyRandomizer v1.0", self)
        self.keyrandomizer.setObjectName("app-about-title")
        self.keyrandomizer.setAlignment(Qt.AlignCenter)

        self.author = QtWidgets.QLabel("by Kevin Putra Satrianto (vinrato)")
        self.author.setObjectName("app-about-author")
        self.author.setAlignment(Qt.AlignCenter)

        self.support = QtWidgets.QLabel('<a href="https://www.paypal.me/kevinrubycon">Support Me!</a>')
        self.support.setObjectName("app-about-paypal")
        self.support.setOpenExternalLinks(True)
        self.support.setAlignment(Qt.AlignCenter)

        self.vlay.addWidget(self.keyrandomizer)
        self.vlay.addWidget(self.author)
        self.vlay.addWidget(self.support)


class GeneratorTab(QtWidgets.QWidget):
    def __init__(self, p):
        super(GeneratorTab, self).__init__(p)
        self.vlay = QtWidgets.QVBoxLayout(self)
        self.controller_lay = QtWidgets.QHBoxLayout()
        self.generator_button_lay = QtWidgets.QVBoxLayout()
        self.generator_button_lay.setContentsMargins(35, 35, 35, 35)
        self.generator_group_lay = QtWidgets.QVBoxLayout()
        self.text_input_lay = QtWidgets.QFormLayout()

        self.generated_display = QtWidgets.QTextBrowser(self)
        self.generated_display.setPlaceholderText("Generated key(s) will be displayed here.")

        self.char_gen_lay = QtWidgets.QVBoxLayout()
        self.char_gen_group = QtWidgets.QGroupBox("Generated Types", self)
        self.char_gen_group.setLayout(self.char_gen_lay)
        self.lttr_check = QtWidgets.QCheckBox("Letters", self)
        self.uppr_check = QtWidgets.QCheckBox("Uppercase Letters", self)
        self.nums_check = QtWidgets.QCheckBox("Numbers", self)
        self.spec_check = QtWidgets.QCheckBox("Special Characters", self)
        self.char_gen_lay.addWidget(self.lttr_check)
        self.char_gen_lay.addWidget(self.uppr_check)
        self.char_gen_lay.addWidget(self.nums_check)
        self.char_gen_lay.addWidget(self.spec_check)

        self.generator_settings_lay = QtWidgets.QVBoxLayout()
        self.generator_settings_group = QtWidgets.QGroupBox("Generator Settings", self)
        self.generator_settings_group.setLayout(self.generator_settings_lay)
        self.length_input = QtWidgets.QLineEdit(self)
        self.length_input.setPlaceholderText("Generated key length")
        self.batch_input = QtWidgets.QLineEdit(self)
        self.batch_input.setPlaceholderText("Number of batch generated keys")
        self.seed_input = QtWidgets.QLineEdit(self)
        self.seed_input.setPlaceholderText("Seed")
        self.generator_settings_lay.addWidget(self.length_input)
        self.generator_settings_lay.addWidget(self.batch_input)
        self.generator_settings_lay.addWidget(self.seed_input)
        self.generator_settings_lay.addWidget(self.char_gen_group)

        self.generate_button = QtWidgets.QPushButton("Generate", self)
        self.generate_button.setObjectName("generator-button")
        self.batch_generate_button = QtWidgets.QPushButton("Batch Generate", self)
        self.batch_generate_button.setObjectName("generator-button")
        self.clear_display_button = QtWidgets.QPushButton("Clear generated keys", self)
        self.clear_display_button.setObjectName("generator-button")
        self.generator_button_lay.addWidget(self.generate_button)
        self.generator_button_lay.addWidget(self.batch_generate_button)
        self.generator_button_lay.addWidget(self.clear_display_button)

        self.controller_lay.addLayout(self.generator_button_lay)
        self.controller_lay.addWidget(self.generator_settings_group)

        self.generator_group = QtWidgets.QGroupBox("Generator", self)
        self.generator_group.setAlignment(Qt.AlignCenter)
        self.generator_group.setLayout(self.generator_group_lay)
        self.generator_group_lay.addLayout(self.controller_lay)

        self.vlay.addWidget(self.generated_display)
        self.vlay.addWidget(self.generator_group)

        self.lttr_check.stateChanged.connect(self.on_letter_check)
        self.uppr_check.stateChanged.connect(self.on_upper_check)
        self.nums_check.stateChanged.connect(self.on_number_check)
        self.spec_check.stateChanged.connect(self.on_specials_check)

        for lineedit in self.findChildren(QtWidgets.QLineEdit):
            lineedit.setFixedHeight(25)

        self.characters_widget: QtWidgets.QTextEdit = self.parent().char_tab.characters

    def on_letter_check(self):
        const = constants.LETTERS
        if self.lttr_check.isChecked():
            if self.characters_widget.toPlainText() == "":
                self.characters_widget.setText(const)
            else:
                self.characters_widget.setText(self.characters_widget.toPlainText() + f", {const}")
        else:
            self.characters_widget.setText(clean(self.characters_widget.toPlainText().replace(f"{const}", "")))

    def on_upper_check(self):
        const = constants.UPPER_LTRS
        if self.uppr_check.isChecked():
            if self.characters_widget.toPlainText() == "":
                self.characters_widget.setText(const)
            else:
                self.characters_widget.setText(self.characters_widget.toPlainText() + f", {const}")
        else:
            self.characters_widget.setText(clean(self.characters_widget.toPlainText().replace(f"{const}", "")))

    def on_number_check(self):
        const = constants.NUMBERS
        if self.nums_check.isChecked():
            if self.characters_widget.toPlainText() == "":
                self.characters_widget.setText(const)
            else:
                self.characters_widget.setText(self.characters_widget.toPlainText() + f", {const}")
        else:
            self.characters_widget.setText(clean(self.characters_widget.toPlainText().replace(f"{const}", "")))

    def on_specials_check(self):
        const = constants.SPECIALS
        if self.spec_check.isChecked():
            if self.characters_widget.toPlainText() == "":
                self.characters_widget.setText(const)
            else:
                self.characters_widget.setText(self.characters_widget.toPlainText() + f", {const}")
        else:
            self.characters_widget.setText(clean(self.characters_widget.toPlainText().replace(f"{const}", "")))


class CharactersTab(QtWidgets.QWidget):
    def __init__(self, p):
        super(CharactersTab, self).__init__(p)
        self.vlay = QtWidgets.QVBoxLayout(self)

        self.characters = QtWidgets.QTextEdit(self)
        self.label = QtWidgets.QLabel("*Separate each character with a comma.")

        self.vlay.addWidget(self.characters)
        self.vlay.addWidget(self.label)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Key Randomizer v1.0")
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(4, 4, 4, 4)
        self.resize(615, 575)

        self.char_tab = CharactersTab(self)
        self.gen_tab = GeneratorTab(self)
        self.about_tab = AboutTab(self)

        for checkbox in self.gen_tab.findChildren(QtWidgets.QCheckBox):
            checkbox.setChecked(True)

        self.tab = QtWidgets.QTabWidget(self)
        self.tab.addTab(self.gen_tab, "Generator")
        self.tab.addTab(self.char_tab, "Generator Characters")
        self.tab.addTab(self.about_tab, "About")

        self.main_layout.addWidget(self.tab)

        self.generator = Randomizer(self.char_tab.characters.toPlainText())

        self.gen_tab.generate_button.clicked.connect(self.on_generate)
        self.gen_tab.batch_generate_button.clicked.connect(self.on_batch_generate)
        self.gen_tab.clear_display_button.clicked.connect(self.on_clear)

    def on_clear(self):
        self.gen_tab.generated_display.clear()

    def on_generate(self):
        self.generator.set_chars(self.char_tab.characters.toPlainText())
        length = self.gen_tab.length_input.text()
        seed = self.gen_tab.seed_input.text()
        if not length:
            length = 8
        else:
            length = int(length)
        if not seed:
            seed = None
        self.gen_tab.generated_display.setText(self.generator.generate(length, seed))

    def on_batch_generate(self):
        self.generator.set_chars(self.char_tab.characters.toPlainText())
        self.gen_tab.generated_display.clear()
        n_batch = self.gen_tab.batch_input.text()
        length = self.gen_tab.length_input.text()
        if not length:
            length = 8
        else:
            length = int(length)
        if not n_batch:
            n_batch = 5
        else:
            n_batch = int(n_batch)
        for key in self.generator.batch_generate(n_batch, length):
            self.gen_tab.generated_display.append(key)

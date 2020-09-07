#! work in progress
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.temp_number = []
        self.keypad()
        self.show()
    def stringNumber(self, character):
        self.temp_number.append(character)
        return ''.join(self.temp_number)
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        
        self.text_field = qtw.QLineEdit()
        button_list = [
                            ("Enter", (1, 0, 1, 2)),
                            ("Clear", (1, 2, 1, 2)),
                            ('7', (2, 0)),
                            ('8', (2, 1)),
                            ('9', (2, 2)),
                            ('+', (2, 3)),
                            ('4', (3, 0)),
                            ('5', (3, 1)),
                            ('6', (3, 2)),
                            ('-', (3, 3)),
                            ('1', (4, 0)),
                            ('2', (4, 1)),
                            ('3', (4, 2)),
                            ('*', (4, 3)),
                            ('0', (5, 0, 1, 3)),
                            ('÷', (5, 3))
                                                    ]
        # Create text field 
        from_row = 0; from_column = 0; row_span = 1; column_span = 4
        container.layout().addWidget(self.text_field, from_row, from_column, row_span, column_span)
        # Create button input   
        for button in button_list:
            text = button[0]
            parameter = button[1]
            button_text = qtw.QPushButton(text, clicked = lambda: self.text_field.setText(self.stringNumber(text)))
            # This use for handling function overloading
            if len(parameter) == 4:
                p1, p2, p3, p4 = parameter
                # void QGridLayout::addWidget(QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0)
                container.layout().addWidget(button_text, p1, p2, p3, p4)
            elif len(parameter) == 2:
                p1,p2 = parameter
                # void QGridLayout::addWidget(QWidget * widget, int row, int column, Qt::Alignment alignment = 0)
                container.layout().addWidget(button_text, p1, p2)
            else:
                raise Exception("Parameter error")

        self.layout().addWidget(container)
    
                
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()


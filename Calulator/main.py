#! work in progress
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.temp_number = []
        self.ans = "0"
        self.button_unlock = True
        self.keypad()
        self.show()
    def keypadPress(self, key):
        if key in "0123456789+-*/." and self.button_unlock:
            self.temp_number.append(key)
            self.text_field.setText(self.getEqn())
        elif key is '=' and self.button_unlock:
            value = self.getValue(self.getEqn())
            self.text_field.setText(value)
            if value != "ERROR Press Clear to continue":
                self.ans = value
        elif key is "Del" and self.button_unlock:
            if self.getEqn() != '':
                self.temp_number.pop()
                self.text_field.setText(self.getEqn())
        elif key is "Ans" and self.button_unlock:
            self.temp_number.append(self.ans)
            self.text_field.setText(self.getEqn())
        elif key is "Clear":
            self.temp_number = []
            self.button_unlock = True
            self.text_field.setText(self.getEqn())

    def getEqn(self):
        return ''.join(self.temp_number)
    def getValue(self, eqn):
        try:
            if self.getEqn() != '':
                answer = eval(eqn)
                return str(answer)
        except:
            self.button_unlock = False
            return "ERROR Press Clear to continue"
            
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        
        self.text_field = qtw.QLineEdit()
        button_list = [
                            #####                               Display                                      ####
                            ('7', (1, 0)),      ('8', (1, 1)), ('9', (1, 2)),   ("Del", (1, 3)), ("Clear", (1, 4)),
                            ('4', (2, 0)),      ('5', (2, 1)), ('6', (2, 2)),   ('*', (2, 3)),   ('/', (2, 4)),    
                            ('1', (3, 0)),      ('2', (3, 1)), ('3', (3, 2)),   ('+', (3, 3)),   ('-', (3, 4)),    
                            ('0', (4, 0, 1, 2)),               ('.', (4, 2)),   ('Ans', (4, 3)), ('=', (4, 4))     
                            #====================================================================================#
                                                                                                                    ]
        # Create text field 
        from_row = 0; from_column = 0; row_span = 1; column_span = 5
        container.layout().addWidget(self.text_field, from_row, from_column, row_span, column_span)
        self.text_field.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        # Create button input   
        for button in button_list:
            text = button[0]
            parameter = button[1]
            button_text = qtw.QPushButton(text, clicked =(lambda f, t = text: self.keypadPress(t)) )
            button_text.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
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
app.setStyle('Oxygen')
mw = MainWindow()
app.exec_()
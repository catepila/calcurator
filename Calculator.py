from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (400, 600)

class CalculatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display_value = '0'
        self.previous_value = ''
        self.operation = ''
        self.should_reset_display = False

    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Display
        self.display = TextInput(
            text='0',
            font_size='48sp',
            readonly=True,
            halign='right',
            multiline=False,
            size_hint_y=0.2
        )
        main_layout.add_widget(self.display)
        
        # Buttons layout
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint_y=0.8)
        
        buttons = [
            ('AC', self.on_clear),
            ('DEL', self.on_delete),
            ('÷', lambda x: self.on_operation('÷')),
            ('', None),
            
            ('7', lambda x: self.on_number('7')),
            ('8', lambda x: self.on_number('8')),
            ('9', lambda x: self.on_number('9')),
            ('×', lambda x: self.on_operation('×')),
            
            ('4', lambda x: self.on_number('4')),
            ('5', lambda x: self.on_number('5')),
            ('6', lambda x: self.on_number('6')),
            ('-', lambda x: self.on_operation('-')),
            
            ('1', lambda x: self.on_number('1')),
            ('2', lambda x: self.on_number('2')),
            ('3', lambda x: self.on_number('3')),
            ('+', lambda x: self.on_operation('+')),
            
            ('0', lambda x: self.on_number('0')),
            ('.', lambda x: self.on_number('.')),
            ('=', self.on_equals),
            ('', None),
        ]
        
        for btn_text, callback in buttons:
            if btn_text == '':
                buttons_layout.add_widget(Button(disabled=True))
            else:
                btn = Button(text=btn_text, font_size='24sp')
                
                # 색상 구분
                if btn_text == 'AC':
                    btn.background_color = (1, 0, 0, 1)  # 빨강
                elif btn_text == 'DEL':
                    btn.background_color = (1, 0.5, 0, 1)  # 주황
                elif btn_text in ('÷', '×', '-', '+'):
                    btn.background_color = (0, 0.5, 1, 1)  # 파랑
                elif btn_text == '=':
                    btn.background_color = (0, 1, 0, 1)  # 초록
                
                btn.bind(on_press=callback)
                buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def on_number(self, number):
        if self.should_reset_display:
            self.display_value = number
            self.should_reset_display = False
        else:
            if self.display_value == '0':
                self.display_value = number
            else:
                self.display_value += number
        self.display.text = self.display_value
    
    def on_operation(self, op):
        if self.previous_value == '':
            self.previous_value = self.display_value
        elif not self.should_reset_display:
            self.previous_value = str(self.calculate(
                float(self.previous_value),
                float(self.display_value),
                self.operation
            ))
            self.display_value = self.previous_value
            self.display.text = self.display_value
        
        self.operation = op
        self.should_reset_display = True
    
    def on_equals(self, instance):
        if self.previous_value != '' and self.operation != '':
            result = self.calculate(
                float(self.previous_value),
                float(self.display_value),
                self.operation
            )
            self.display_value = str(result)
            self.display.text = self.display_value
            self.previous_value = ''
            self.operation = ''
            self.should_reset_display = True
    
    def on_clear(self, instance):
        self.display_value = '0'
        self.previous_value = ''
        self.operation = ''
        self.should_reset_display = False
        self.display.text = '0'
    
    def on_delete(self, instance):
        if len(self.display_value) > 1:
            self.display_value = self.display_value[:-1]
        else:
            self.display_value = '0'
        self.display.text = self.display_value
    
    @staticmethod
    def calculate(prev, curr, op):
        if op == '+':
            return prev + curr
        elif op == '-':
            return prev - curr
        elif op == '×':
            return prev * curr
        elif op == '÷':
            return prev / curr if curr != 0 else 0
        return curr

if __name__ == '__main__':
    CalculatorApp().run()

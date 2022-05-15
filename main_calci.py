import kivy
kivy.require('2.1.0')       # Minimum Version

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder       # To attach .kv file
from kivy.core.window import Window

# Attaching .kv file...
Builder.load_file('calci.kv')

# Window Size...
Window.size = (370, 550)


class CalciLayouts(Widget):
    A = ''        # Operand 1...
    Symbol = ''       # Last Operator...
    B = ''       # Operand 2...
    Current = 'A'       # To know where the number to insert(A/B)...

    # Clear function to clear everything from screen...
    def clear(self):
        self.ids.screen.text = '0'
        self.ids.screen2.text = ''
        self.A = ''  # Operand 1...
        self.Symbol = ''  # Last Operator...
        self.B = ''  # Operand 2...
        self.Current = 'A'  # To know where the number to insert(A/B)...

    def backspace(self):
        pre_num = self.ids.screen.text
        pre_num = pre_num[:-1]
        if pre_num != '':
            self.ids.screen.text = pre_num
        else:
            self.ids.screen.text = '0'

    def num_btn_fn(self, num):
        try:
            self.ids.screen2.font_size = 38
            screen1_pre_value = self.ids.screen.text
            screen2_pre_value = self.ids.screen2.text

            if screen1_pre_value == '0' and (screen2_pre_value == '' or screen2_pre_value == 'Can\'t divide by 0' or screen2_pre_value == 'Can\'t start with (+,-,*,/)'):
                self.A = str(num)
                self.ids.screen.text = str(num)
                self.ids.screen2.text = str(num)
            else:
                dupli_s1_pre_value = screen1_pre_value
                s1_list = list(dupli_s1_pre_value)
                last_in_list = s1_list[-1]
                if ((last_in_list.isnumeric()) == True) and (self.Current == 'A'):
                    self.A = self.A + str(num)
                    self.ids.screen.text = f'{screen1_pre_value}{str(num)}'
                    self.ids.screen2.text = str(eval(self.A))
                elif ((last_in_list.isnumeric()) == False) and (self.Current == 'B'):
                    self.B = str(num)
                    answer = self.A + self.Symbol + self.B
                    ans = eval(answer)
                    self.ids.screen.text = f'{screen1_pre_value}{str(num)}'
                    self.ids.screen2.text = str(ans)
                elif ((last_in_list.isnumeric()) == True) and (self.Current == 'B'):
                    self.B = self.B + str(num)
                    answer = self.A + self.Symbol + self.B
                    ans = eval(answer)
                    self.ids.screen.text = f'{screen1_pre_value}{str(num)}'
                    self.ids.screen2.text = str(ans)
        except ZeroDivisionError:
            self.ids.screen2.font_size = 18
            self.ids.screen2.text = 'Can\'t divide by 0'
            self.ids.screen.text = '0'
            self.A = ''  # Operand 1...
            self.Symbol = ''  # Last Operator...
            self.B = ''  # Operand 2...
            self.Current = 'A'  # To know where the number to insert(A/B)...

    def math_sign(self, sign):
        if self.ids.screen.text == '0':
            self.ids.screen2.font_size = 18
            self.ids.screen2.text = 'Can\'t start with (+,-,*,/)'
            self.A = ''  # Operand 1...
            self.Symbol = ''  # Last Operator...
            self.B = ''  # Operand 2...
            self.Current = 'A'  # To know where the number to insert(A/B)...
        else:
            self.A = self.ids.screen2.text
            self.B = ''
            self.Current = 'B'
            self.Symbol = sign
            pre_num = self.ids.screen.text
            self.ids.screen.text = f'{pre_num}{sign}'


    def dot(self):
        pre_num = self.ids.screen.text
        if '.' in pre_num:
            pass
        else:
            pre_num = f'{pre_num}.'
            self.ids.screen.text = pre_num

'''    def equal(self):
        try:
            pre_num = self.ids.screen.text

            # Doing calculation using Math...
            answer = eval(pre_num)
            self.ids.screen2.text = str(answer)
        except ZeroDivisionError:
            self.ids.screen2.text = 'Can\'t divide by 0'
            self.ids.screen.text = '0'
        except:
            self.ids.screen2.text = 'Error!'
            self.ids.screen.text = '0'
'''

class CalculatorApp(App):
    def build(self):
        return CalciLayouts()


if __name__ == '__main__':
    CalculatorApp().run()

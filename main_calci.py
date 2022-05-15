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
    Aop = ['']        # Operand 1...
    Symbol_lst = ['']       # Last Operator...
    Bop = ['']       # Operand 2...
    Current = ['A']       # To know where the number to insert(A/B)...
    math_signs = ['+', '-', '*', '/']

    # Clear function to clear everything from screen...
    def clear(self):
        self.ids.screen.text = '0'
        self.ids.screen2.text = ''
        self.Aop.clear()
        self.Aop.append('')
        self.Symbol_lst.clear()
        self.Symbol_lst.append('')
        self.Bop.clear()
        self.Bop.append('')
        self.Current = ['A']

    def backspace(self):
        pre_num = self.ids.screen.text
        rem = self.ids.screen.text[:-1]
        to_del = pre_num[-1]
        if rem == ['']:
            self.Aop.pop()
            self.ids.screen.text = '0'
            self.ids.screen2.text = ''
        elif (to_del.isnumeric() == True) and (self.Current[-1] == 'A'):
            self.Aop.pop()
            self.ids.screen.text = rem
            answer = f'{self.Aop[-1]}{self.Symbol_lst[-1]}{self.Bop[-1]}'
            ans = eval(str(answer))
            self.ids.screen2.text = str(ans)
        elif (to_del.isnumeric() == True) and (self.Current[-1] == 'B'):
            self.Bop.pop()
            self.ids.screen.text = rem
            answer = self.Aop[-1] + self.Symbol_lst[-1] + self.Bop[-1]
            ans = eval(str(answer))
            self.ids.screen2.text = str(ans)
        elif to_del in self.math_signs:
            self.Aop.pop()
            self.Bop.pop()
            self.Symbol_lst.pop()
            self.Current.pop()
            self.ids.screen.text = rem
            answer = self.Aop[-1] + self.Symbol_lst[-1] + self.Bop[-1]
            ans = eval(str(answer))
            self.ids.screen2.text = str(ans)


    def num_btn_fn(self, num):
        try:
            self.ids.screen2.font_size = 38
            screen1_pre_value = self.ids.screen.text
            screen2_pre_value = self.ids.screen2.text

            if screen1_pre_value == '0' and (screen2_pre_value == '' or screen2_pre_value == 'Can\'t divide by 0' or screen2_pre_value == 'Can\'t start with (+,-,*,/)'):
                self.Aop.append(str(num))
                self.ids.screen.text = str(num)
                self.ids.screen2.text = str(num)
            else:
                dupli_s1_pre_value = screen1_pre_value
                last_in_list = screen1_pre_value[-1]
                if ((last_in_list.isnumeric()) == True) and (self.Current == 'A'):
                    temp_A = f'{self.Aop[-1]}{num}'
                    self.Aop.append(temp_A)
                    self.ids.screen.text = f'{screen1_pre_value}{str(num)}'
                    answer = self.Aop[-1] + self.Symbol_lst[-1] + self.Bop[-1]
                    ans = eval(str(answer))
                    self.ids.screen2.text = str(ans)
                elif (last_in_list in self.math_signs) and (self.Current == 'B'):
                    self.Bop.append(str(num))
                    answer = self.Aop[-1] + self.Symbol_lst[-1] + self.Bop[-1]
                    ans = eval(str(answer))
                    self.ids.screen.text = f'{screen1_pre_value}{str(num)}'
                    self.ids.screen2.text = str(ans)
                elif (last_in_list.isnumeric() == True) and (self.Current == 'B'):
                    temp_B = f'{self.Bop[-1]}{str(num)}'
                    self.Bop.append(temp_B)
                    answer = self.Aop[-1] + self.Symbol_lst[-1] + self.Bop[-1]
                    ans = eval(str(answer))
                    self.ids.screen.text = f'{screen1_pre_value}{str(num)}'
                    self.ids.screen2.text = str(ans)
        except ZeroDivisionError:
            self.ids.screen2.font_size = 18
            self.ids.screen2.text = 'Can\'t divide by 0'
            self.ids.screen.text = '0'
            self.Aop.clear()
            self.Aop.append('')
            self.Symbol_lst.clear()
            self.Symbol_lst.append('')
            self.Bop.clear()
            self.Bop.append('')
            self.Current = ['A']

    def math_sign(self, sign):
        if self.ids.screen.text == '0':
            self.ids.screen2.font_size = 18
            self.ids.screen2.text = 'Can\'t start with (+,-,*,/)'
            self.Aop.clear()
            self.Aop.append('')
            self.Symbol_lst.clear()
            self.Symbol_lst.append('')
            self.Bop.clear()
            self.Bop.append('')
            self.Current = ['A']
        else:
            self.Aop.append(self.ids.screen2.text)
            self.Bop.append('')
            self.Current.append('B')
            self.Symbol_lst.append(sign)
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

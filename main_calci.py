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
    # Clear function to clear everything from screen...
    def clear(self):
        self.ids.screen.text = '0'

    def backspace(self):
        pre_num = self.ids.screen.text
        pre_num = pre_num[:-1]
        if pre_num != '':
            self.ids.screen.text = pre_num
        else:
            self.ids.screen.text = '0'

    def num_btn_fn(self, num):
        # Variable to store pre-entered values...
        pre_num = self.ids.screen.text

        # Checking is '0' in screen...
        if pre_num == '0':
            self.ids.screen.text = ''
            self.ids.screen.text = str(num)
        else:
            self.ids.screen.text = f'{pre_num}{str(num)}'

    def math_sign(self, sign):
        pre_num = self.ids.screen.text
        self.ids.screen.text = f'{pre_num}{sign}'

    def dot(self):
        pre_num = self.ids.screen.text
        if '.' in pre_num:
            pass
        else:
            pre_num = f'{pre_num}.'
            self.ids.screen.text = pre_num

    def equal(self):
        pre_num = self.ids.screen.text

        # Addition Stuff...
        if '+' in pre_num:
            num_list = pre_num.split('+')
            ans = 0
            for num in num_list:
                ans += float(num)

            self.ids.screen2.text = f'{str(ans)}  '

class CalculatorApp(App):
    def build(self):
        return CalciLayouts()


if __name__ == '__main__':
    CalculatorApp().run()

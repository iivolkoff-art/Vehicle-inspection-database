from Lib_and_sql.library import *


class Error():
    @staticmethod
    def error(e):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text=str(e), font_size=11))
        button = Button(text='Закрыть', background_color='#825b00',size_hint = (1, 0.3),background_normal='')
        layout.add_widget(button)
        popup = Popup(title='Ошибка', background_color='#825b00', content=layout, size_hint=(None, None),
                      size=(400, 400))
        button.bind(on_press=popup.dismiss)
        popup.open()

    @staticmethod
    def count_error():
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text= 'Инспектор не может проверять больше 10 машин в день', font_size=11))
        button = Button(text='Закрыть', background_color='#825b00', size_hint=(1, 0.3), background_normal='')
        layout.add_widget(button)
        popup = Popup(title='Ошибка', background_color='#825b00', content=layout, size_hint=(None, None),
                      size=(400, 400))
        button.bind(on_press=popup.dismiss)
        popup.open()
from Lib_and_sql.library import *
#окно сотрудника гаи
class history(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gl_engine_number_history = TextInput(hint_text='Введите номер двигателя', text = '', multiline=False, size_hint=(0.5, 0.05))
        self.gl_date_history = Label(text='Дата прохождения')
        self.gl_result_history = Label(text='Результат')
        bl = BoxLayout(orientation='horizontal', spacing=1)
        gl = GridLayout(cols=2, rows=3, spacing=1)
        gl.add_widget(Label(size_hint=(0.5, 0.1)))
        gl.add_widget(Button(text='В меню', size_hint=(0.5, 0.1), background_color='#825b00', background_normal='', on_press=self.click_for_move))
        gl.add_widget(self.gl_date_history)
        gl.add_widget(self.gl_result_history)
        gl.add_widget(self.gl_engine_number_history)
        gl.add_widget(Button(text='Просмотр', size_hint=(0.5, 0.1), background_color='#edb021', background_normal='', on_press=self.request))
        self.add_widget(gl)

    def click_for_move(self, *args): #переход в меню
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

    def request(self, instance):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT inspection.date, inspection.result FROM inspection INNER JOIN owner ON inspection.government_number = owner.government_number WHERE owner.engine_number = '{self.gl_engine_number_history.text}'")
            data_from_db = cursor.fetchall()
            self.add_data_to_label(data_from_db)
        except Exception as e:
            print(e)
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")

    def add_data_to_label(self, data):
        self.gl_date_history.text = ''
        self.gl_result_history.text = ''
        for i in range(len(data)):
            self.gl_date_history.text += str(data[i][0]) + '\n'
            self.gl_result_history.text += str(data[i][1]) + '\n'


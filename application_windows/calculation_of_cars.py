from Lib_and_sql.library import *
#окно сотрудника гаи
class calculation_of_car(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gl_start_date = TextInput(hint_text='Введите начальную дату', text = '', multiline=False, size_hint=(0.5, 0.05))
        self.gl_end_date = TextInput(hint_text='Введите конечную дату', text = '', multiline=False, size_hint=(0.5, 0.05))
        self.gl_count = Label(text='Количество авто', size_hint=(0.5, 0.3))
        self.gl_date = Label(text='Дата', size_hint=(0.5, 0.3))
        bl = BoxLayout(orientation='horizontal', spacing=1)
        gl = GridLayout(cols=2, rows=3, spacing=1)
        gl.add_widget(self.gl_start_date)
        gl.add_widget(self.gl_end_date)
        gl.add_widget(self.gl_count)
        gl.add_widget(self.gl_date)
        gl.add_widget(Button(text='Просмотр', size_hint=(0.5, 0.1), background_color='#edb021', background_normal='', on_press=self.request))
        gl.add_widget(Button(text='В меню', size_hint=(0.5, 0.1), background_color='#825b00', background_normal='', on_press=self.click_for_move))
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
            cursor.execute(f"SELECT government_number, date FROM inspection WHERE date BETWEEN '{self.gl_start_date.text.replace('.', '')[:1] + str(int(self.gl_start_date.text.replace('.', '')[1]) - 1) + self.gl_start_date.text.replace('.', '')[2:]}' AND '{(self.gl_end_date.text).replace('.', '')}'")
            data_from_db = cursor.fetchall()
        except Exception as e:
            print(e)
            Error.error(e)  # почему оно работает?
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")
            self.add_data_to_label(data_from_db)

    def add_data_to_label(self, data):
        self.gl_count.text = ''
        self.gl_date.text = ''
        non_recurring_dates = []
        count_dates = []
        for i in range(len(data)):
            if data[i][1] not in non_recurring_dates:
                non_recurring_dates.append(data[i][1])
        for i in range(len(non_recurring_dates)):
            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                cursor = connection.cursor()
                cursor.execute(f"SELECT count(government_number) FROM inspection WHERE date = '{non_recurring_dates[i]}'")
                data_of_count = cursor.fetchall()
                count_dates.append(data_of_count)
            except Exception as e:
                Error.error(e)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    print("Connection closed")
        for i in range(len(count_dates)):
            self.gl_count.text += str(count_dates[i])[2:3] + '\n'
            self.gl_date.text += non_recurring_dates[i] + '\n'



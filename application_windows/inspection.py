from Lib_and_sql.library import *
#окно осмотра
class inspection(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gl_government_number_name_inspection = TextInput(hint_text='Введите госномер автомобиля и фамилию сотрудника через пробел', text='', height=30)
        self.gl_row_name_inspection = TextInput(hint_text='Введите названия столбца', text='', height=30)
        self.gl_data_inspection = TextInput(hint_text='Введите содержимое', text='', height=30) # переменные которые используются в функциях

        bl = BoxLayout(orientation='vertical', spacing=1)
        gl = GridLayout(cols=2, spacing=1, size_hint=(1, 2))

        gl.add_widget(self.gl_government_number_name_inspection)
        gl.add_widget(
            Button(text='В меню', background_color='#825b00', background_normal='', on_press=self.click_for_move))
        gl.add_widget(self.gl_row_name_inspection)
        gl.add_widget(Label(text = 'government_number, name, result, result_inspection, date', font_size=10))
        gl.add_widget(self.gl_data_inspection)
        gl.add_widget(Label(text = 'Добавить - создает новую запись \nРедактировать - осуществяет замену данных в одной из ячеек \nУдалить - удаляет запись', font_size = 10))
        bl.add_widget(gl)
        gl1 = GridLayout(cols=3, rows=2, spacing=1)
        gl1.add_widget(Button(text='Добавить', background_color='#edb021', background_normal='', on_press=self.add))
        gl1.add_widget(Button(text='Редактировать', background_color='#edb021', background_normal='', on_press=self.update))
        gl1.add_widget(Button(text='Удалить', background_color='#edb021', background_normal='', on_press=self.delete))

        bl.add_widget(gl1)
        self.add_widget(bl)

    def click_for_move(self, *args):  # переход в меню
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

    def delete(self, instance):  # удаляет запись
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM inspection WHERE government_number = '{(self.gl_government_number_name_inspection.text).split()[0]}'")
            connection.commit()
        except Exception as e: #выводит ошибку в консоль(после окончания работы, можно закомментировать)
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")

    def update(self, instance): # редактирует запись
        if self.gl_row_name_inspection.text == 'date':
            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                cursor = connection.cursor()
                cursor.execute(f"SELECT COUNT(date) FROM inspection WHERE name = '{(self.gl_government_number_name_inspection.text).split()[0]}' AND date = '{self.gl_data_inspection.text}'")  # ошибка
                data_of_count = cursor.fetchall()
                if data_of_count[0][0] >= 10:
                    Error.count_error()
                else:
                    cursor.execute(f"UPDATE inspection SET {self.gl_row_name_inspection.text} = '{self.gl_data_inspection.text}' Where government_number = '{(self.gl_government_number_name_inspection.text).split()[0]}'")  # ошибка
                    connection.commit()
            except Exception as e:
                Error.error(e)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    print("Connection closed")
        else:
            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                cursor = connection.cursor()
                cursor.execute(
                    f"UPDATE inspection SET {self.gl_row_name_inspection.text} = '{self.gl_data_inspection.text}' Where government_number = '{(self.gl_government_number_name_inspection.text).split()[0]}'")  # ошибка
                connection.commit()
            except Exception as e:
                Error.error(e)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    print("Connection closed")

    def add(self, instance): # добавляет запись
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO inspection (government_number, name, result, result_inspection, date) VALUES ('{(self.gl_government_number_name_inspection.text).split()[0]}', '{(self.gl_government_number_name_inspection.text).split()[1]}', Null, Null, Null)")
            connection.commit()
        except Exception as e:
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")
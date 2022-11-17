from Lib_and_sql.library import *
#окно сотрудника гаи
class list_of_officer(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gl_date_of_inspection = TextInput(hint_text='Введите дату', text = '', multiline=False, size_hint=(0.5, 0.05))
        self.gl_name_of_inspector = Label(text='ФИО', size_hint=(0.5, 0.3))
        self.gl_rank_of_inspector = Label(text='Звание сотрудника', size_hint=(0.5, 0.3))
        self.gl_government_number_inspector = Label(text='Госномера автомобилей', size_hint=(0.5, 0.3))
        bl = BoxLayout(orientation='horizontal', spacing=1)
        gl = GridLayout(cols=3, rows=2, spacing=1)
        gl.add_widget(self.gl_name_of_inspector)
        gl.add_widget(self.gl_rank_of_inspector)
        gl.add_widget(self.gl_government_number_inspector)
        gl.add_widget(Button(text='Просмотр', size_hint=(0.5, 0.1), background_color='#edb021', background_normal='', on_press=self.request))

        gl.add_widget(self.gl_date_of_inspection)
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
            cursor.execute(f"SELECT inspection.name, rank, government_number FROM inspection INNER JOIN police ON inspection.name = police.name WHERE date = '{self.gl_date_of_inspection.text}'")
            data_from_db = cursor.fetchall()
            self.add_data_to_label(data_from_db)
        except Exception as e:
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")

    def add_data_to_label(self, data):
        self.gl_name_of_inspector.text = ''
        self.gl_rank_of_inspector.text = ''
        self.gl_government_number_inspector.text = ''
        for i in range(len(data)):
            self.gl_name_of_inspector.text += str(data[i][0]) + '\n'
            self.gl_rank_of_inspector.text += str(data[i][1]) + '\n'
            self.gl_government_number_inspector.text += str(data[i][2]) + '\n'


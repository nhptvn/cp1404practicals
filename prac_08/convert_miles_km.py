from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    message = StringProperty()

    def build(self):
        Window.size = (1280, 720)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type a number in the field & press Enter"
        return self.root

    def calculate(self):
        number = self.get_valid_miles()
        result = number * MILES_TO_KM
        self.root.ids.km_text.text = f"{result:.2f}km"

    def handle_increment(self, increment_value):
        number = self.get_valid_miles() + increment_value
        self.root.ids.input_miles.text = str(number)
        self.calculate()

    def get_valid_miles(self):
        try:
            number = float(self.root.ids.input_miles.text)
            return number
        except ValueError:
            return None


ConvertMilesKmApp().run()

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app greeting message."""
    def build(self):
        """Build the Kivy app from kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greeting message upon call."""
        # print('greet')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle clearing texts upon call."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()

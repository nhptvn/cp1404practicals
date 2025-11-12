from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Program that dynamically create labels from a list of names."""
    def __init__(self, **kwargs):
        """Initialise the app with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Bob", "Peter", "Paul"]

    def build(self):
        """Build the Kivy app from kv file and add labels dynamically."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root


DynamicLabelsApp().run()



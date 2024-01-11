from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from pydub import AudioSegment
from pydub.playback import play

class GateCodeMemorizer(App):
    def build(self):
        self.code_sequence = ['Törlése', '5', '1', '8', '9', '9', 'Törlése']  # Example code sequence
        self.entered_code = []

        self.sound_del = SoundLoader.load('./soundeffects/beep-08b.mp3')
        self.sound_num = SoundLoader.load('./soundeffects/beep-07a.mp3')
        self.sound_correct = AudioSegment.from_file('./soundeffects/beep-09.mp3')
        self.sound_bad = SoundLoader.load('./soundeffects/beep-10.mp3')

        layout = BoxLayout(orientation='vertical', spacing=10)

        for row in [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['Törlése', '0', 'Csengő']]:
            row_layout = BoxLayout(spacing=10)
            for button_text in row:
                button = Button(text=button_text, on_press=self.on_button_press)
                row_layout.add_widget(button)
            layout.add_widget(row_layout)

        return layout

    def on_button_press(self, instance):
        button_text = instance.text
        if button_text == 'Törlése':
            self.entered_code.append(button_text)
            if self.sound_del:
                self.sound_del.play()
            if self.entered_code == ['Törlése', 'Törlése']:
                self.entered_code = ['Törlése']
            if len(self.entered_code) >= 2 :
                self.check_code()
                self.entered_code.clear()
        else:
            self.entered_code.append(button_text)
            if self.sound_num:
                self.sound_num.play()

        print(self.entered_code)

    def check_code(self):
        if self.entered_code == self.code_sequence:
            if self.sound_correct:
                play(self.sound_correct * 3)
        else:
            if self.sound_bad:
                self.sound_bad.play()

if __name__ == '__main__':
    GateCodeMemorizer().run()
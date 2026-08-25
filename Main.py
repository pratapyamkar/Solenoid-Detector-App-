from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import compass

class SolenoidDetectorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.title_label = Label(
            text="SOLENOID DETECTOR", 
            font_size='22sp', 
            bold=True
        )
        self.status_label = Label(
            text="INACTIVE", 
            font_size='36sp', 
            bold=True, 
            color=(1, 0, 0, 1)  # Red when inactive
        )
        self.value_label = Label(
            text="0 μT", 
            font_size='48sp'
        )
        
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.value_label)
        
        return self.layout

    def on_start(self):
        try:
            compass.enable()
            Clock.schedule_interval(self.update_sensor, 0.1)
        except Exception as e:
            self.status_label.text = "SENSOR ERROR"

    def update_sensor(self, dt):
        try:
            val = compass.orientation
            if val and any(val):
                x, y, z = val[0] or 0, val[1] or 0, val[2] or 0
                magnitude = (x**2 + y**2 + z**2)**0.5
                self.value_label.text = f"{int(magnitude)} μT"
                
                if magnitude > 120:
                    self.status_label.text = "⚡ ENERGIZED"
                    self.status_label.color = (0, 1, 0, 1)  # Green
                else:
                    self.status_label.text = "❌ INACTIVE"
                    self.status_label.color = (1, 0, 0, 1)  # Red
        except Exception:
            pass

    def on_stop(self):
        try:
            compass.disable()
        except Exception:
            pass

if __name__ == '__main__':
    SolenoidDetectorApp().run()
  

class Device:

    def __init__(self, name: str, status: bool = False):
        self.name = name
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def get_status(self):
        return "Ein" if self.status else "Aus"

    def __str__(self):
        return f"Gerät: {self.name} | Status: {self.get_status()}"


class Lamp(Device):
    
    def __init__(self, name: str, brightness: int = 0):
        super().__init__(name)
        self.brightness = brightness

    def set_brightness(self, value: int):
        if self.status:
            self.brightness = max(0, min(100, value))
        else:
            print("Lampe ist aus. Bitte zuerst einschalten.")

    def __str__(self):
        return f"Lampe: {self.name} | Status: {self.get_status()} | Helligkeit: {self.brightness}%"


class Thermostat(Device):
    
    def __init__(self, name: str, temperature: float = 20.0):
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, value: float):
        if self.status:
            self.temperature = value
        else:
            print("Thermostat ist aus. Bitte zuerst einschalten.")

    def __str__(self):
        return f"Thermostat: {self.name} | Status: {self.get_status()} | Temperatur: {self.temperature}°C"


class Speaker(Device):
    
    def __init__(self, name: str, volume: int = 50):
        super().__init__(name)
        self.volume = volume

    def set_volume(self, value: int):
        if self.status:
            self.volume = max(0, min(100, value))
        else:
            print("Lautsprecher ist aus. Bitte zuerst einschalten.")

    def play_music(self, track: str):
        if self.status:
            print(f"Spiele Musik: {track}")
        else:
            print("Lautsprecher ist aus. Bitte zuerst einschalten.")

    def __str__(self):
        return f"Lautsprecher: {self.name} | Status: {self.get_status()} | Lautstärke: {self.volume}%"


# Objekte erstellen und testen
lamp = Lamp("Wohnzimmerlampe")
thermostat = Thermostat("Heizung")
speaker = Speaker("Soundbox")

# Geräte einschalten und konfigurieren
lamp.turn_on()
lamp.set_brightness(80)

thermostat.turn_on()
thermostat.set_temperature(22.5)

speaker.turn_on()
speaker.set_volume(70)
speaker.play_music("Jazz Playlist")

# Ausgabe
print(lamp)
print(thermostat)
print(speaker)
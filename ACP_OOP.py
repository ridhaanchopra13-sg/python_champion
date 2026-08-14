from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def show_device(self):
        print("Device:", self.__class__.__name__)
    @abstractmethod
    def turn_on(self):
        pass
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Light is on.")
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Fan is on.")
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Speaker is on.")
light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()
for device in [light, fan, speaker]:
    device.show_device()
    device.turn_on()
class SecurityCamera:
    def check_status(self):
        print("Camera is working.")
class DoorLock:
    def check_status(self):
        print("Door is locked.")
for device in [SecurityCamera(), DoorLock()]:
    device.check_status()
import pyb
import micropython
micropython.alloc_emergency_exception_buf(100)


# Futaba PPM decoder
# http://diydrones.com/profiles/blogs/705844:BlogPost:38393
class Decoder():

    def __init__(self, pin: str):
        self.pin = pin
        self.current_channel = -1
        self.channels = [0] * 10 # up to 10 channels
        self.timer = pyb.Timer(2, prescaler=83, period=0x3fffffff)
        self.timer.counter(0)
        # clear any previously set interrupt
        pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_NONE, None)
        self.ext_int = pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_NONE, self._callback)

    def _callback(self, line) -> None:
        ticks = self.timer.counter()
        if ticks > 5000:
            self.current_channel = 0
        elif self.current_channel > -1:
            self.channels[self.current_channel] = ticks
            self.current_channel += 1
        self.timer.counter(0)

    def get_channel_value(self, channel: int) -> int:
        return self.channels[channel]

    def enable(self):
        self.ext_int.enable()

    def disable(self):
        self.ext_int.disable()



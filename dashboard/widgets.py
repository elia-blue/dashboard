class ClockWidget():
    def __init__(self):
        self.name = "Clock"
        self.template = "widget_clock.html"

class PingWidget():
    def __init__(self, addrs: list):
        self.name = "Ping"
        self.template = "widget_ping.html"
        self.addrs = addrs
        self.targets = self.addrs
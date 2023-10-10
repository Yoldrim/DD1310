class TV:
    def __init__(self, tv_name, max_channels, current_channel, max_volume, current_volume):
        self.tv_name = tv_name
        self.max_channels = max_channels
        self.current_channel = current_channel
        self.max_volume = max_volume
        self.current_volume = current_volume

    def increase_volume(self):
        if self.current_volume < self.max_volume:
            self.current_volume += 1
            return True
        return False

    def decrease_volume(self):
        if self.current_volume > 0:
            self.current_volume -= 1
            return True
        return False

    def change_channel(self, new_channel):
        if new_channel > 0 and new_channel < self.max_channels:
            self.current_channel = new_channel
            return True
        return False

    def __str__(self):
        return f"{self.tv_name}, channel: {self.current_channel}, volume: {self.current_volume}"

    def str_for_file(self):
        return f"{self.tv_name},{self.max_channels},{self.current_channel},{self.max_volume},{self.current_volume}"

    
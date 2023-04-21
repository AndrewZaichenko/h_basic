import time


class MediaPlayer:
    player_state = 'Initial'
    quality_settings = ['144', '240', '360', '480', '720', '1080', '2160']
    volume_settings = 0
    interface_lang = 'English'
    interface_theme = 'Light'
    start_time = None
    stop_time = None
    movie_path = ''

    def __init__(self, movie_path):
        self.movie_path = movie_path

    def play(self):
        if self.movie_path and self.player_state != 'Running':
            current_time = time.ctime()
            self.start_time = time.time()
            self.player_state = 'Running'
            print(f"Starts {self.player_state} at {current_time}")
        else:
            print('Unable to run. Incorrect path')

    def pause(self):
        if self.player_state == 'Running':
            self.stop_time = time.time()
            delta_time = self.start_time - self.stop_time
            self.player_state = 'Paused'
            minutes, seconds = divmod(delta_time, 60)
            print(f"{self.player_state} at {minutes:.0f} min {seconds:.0f} sec")
        else:
            print('Already stopped')

    def change_quality(self):
        user_quality = input("Please choose a quality from range [144, 240, 360, 480, 720, 1080, 2160] >>> ").strip()
        if user_quality in self.quality_settings:
            self.quality_settings = user_quality
            print("The quality is changed to ", self.quality_settings)
        else:
            print("You've entered an incorrect value. Please try again.")

    def volume_increase(self):
        if self.volume_settings == 10:
            print("You've reached the max value")
        else:
            self.volume_settings += 1
            print("Volume =", self.volume_settings)

    def volume_decrease(self):
        if self.volume_settings == 0:
            print("You've reached the min value")
        else:
            self.volume_settings -= 1
            print("Volume =", self.volume_settings)

    def volume_mute(self):
        if self.volume_settings == 0:
            print("Already muted")
        else:
            self.volume_settings = 0
            print("Muted")

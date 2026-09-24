class Camera:
    def take_photo(self):
        print("Taking photograph...")


class Phone:
    def make_call(self):
        print("Making phone call...")


class Smartphone(Camera, Phone):
    def use_apps(self):
        print("Using smartphone apps...")


s = Smartphone()
s.take_photo()
s.make_call()
s.use_apps()
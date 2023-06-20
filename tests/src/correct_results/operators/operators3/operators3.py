# operators3 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.say(self.calculate("abs", -15.0))
    self.wait(1.0)
    self.say(self.calculate("floor", 1.9))
    self.wait(1.0)
    self.say(self.calculate("ceiling", 1.1))
    self.wait(1.0)
    self.say(self.calculate("sqrt", 15.0))
    self.wait(1.0)
    self.say(self.calculate("sin", 90.0))
    self.wait(1.0)
    self.say(self.calculate("cos", 90.0))
    self.wait(1.0)
    self.say(self.calculate("tan", 45.0))
    self.wait(1.0)
    self.say(self.calculate("asin", 1.0))
    self.wait(1.0)
    self.say(self.calculate("acos", 0.0))
    self.wait(1.0)
    self.say(self.calculate("atan", 1.0))
    self.wait(1.0)
    self.say(self.calculate("ln", 1.0))
    self.wait(1.0)
    self.say(self.calculate("log", 0.01))
    self.wait(1.0)
    self.say(self.calculate("e ^", 1.0))
    self.wait(1.0)
    self.say(self.calculate("10 ^", 2.0))
    self.wait(1.0)

sprite1.when_program_starts(when_program_starts_1)

stage.play()

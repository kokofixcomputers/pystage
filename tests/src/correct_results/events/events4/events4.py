# events4 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('blue_sky')
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

def when_backdrop_switches_to_1(self):
    self.say("Switched backdrop to blue sky")

sprite1.when_backdrop_switches_to("Blue Sky", when_backdrop_switches_to_1)

def when_program_starts_2(self):
    self.switch_backdrop_to("backdrop1")
    self.wait(1.0)
    self.switch_backdrop_to("blue_sky")

sprite1.when_program_starts(when_program_starts_2)

stage.play()

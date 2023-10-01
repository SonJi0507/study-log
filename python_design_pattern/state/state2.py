# --- state ---
class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Current:", self, " => switched to new state", state.name)
            self.__class__ = state
        else :
            print("Current:" ,self, " => switching to", state.name, "not possible.")

    def __str__(self):
        return self.name
    
# --- concrete state ---
class Off(ComputerState):
    name = "off"
    allowed = ["on"]


class On(ComputerState):
    name = "on"
    allowed = ["off", "suspend", "hibernate"]


class Suspend(ComputerState):
    name = "suspend"
    allowed = ["on"]


class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ["on"]


# --- context ---
class Computer(object):
    def __init__(self, model="HP"):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == "__main__":
    comp = Computer()
    # 전원을 켠다.
    comp.change(On)
    # 전원을 끈다.
    comp.change(Off)

    # 전원을 다시 켠다.
    comp.change(On)
    # 일시 중지
    comp.change(Suspend)
    # 절전 모드로 변경할 수 없다.
    comp.change(Hibernate)
    # 전원을 다시 켠다.
    comp.change(On)
    # 전원을 끈다.
    comp.change(Off)


"""
Current: off  => switched to new state on
Current: on  => switched to new state off
Current: off  => switched to new state on
Current: on  => switched to new state suspend
Current: suspend  => switching to hibernate not possible.
Current: suspend  => switched to new state on
Current: on  => switched to new state off
"""
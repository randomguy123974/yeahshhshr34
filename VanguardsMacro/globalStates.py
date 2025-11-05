class GlobalState:
    def __init__(self):
        self.state = {}
        self.listener = {}

    def set(self, key, value): #KV pair of state
        old_val = self.state.get(key) # get old value
        self.state[key] = value
        #Check if change in value
        if old_val != value:
            for callback in self.listener.get(key, []):
                callback(value)
    def watch(self, key, callback):
        self.listener.setdefault(key, []).append(callback)


global_state = GlobalState()

global_state.set("state", False)
global_state.set("task", None)
global_state.set("rewards", 0)
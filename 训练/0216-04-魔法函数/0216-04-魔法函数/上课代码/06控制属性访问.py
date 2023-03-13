class AccessCounter(object):
    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)  # self.counter = 0
        super(AccessCounter, self).__setattr__('value', val)  # self.value = val

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # Make this unconditional.
        # If you want to prevent other attributes to be set, raise AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)


ac = AccessCounter(100)
ac.value = 10  # 给 ac 赋值 就会触发 __setattr__
ac.value = 10  # 给 ac 赋值 就会触发 __setattr__
ac.name = '正心'  # 给 ac 赋值 就会触发 __setattr__
print(ac.counter)
print(ac.value)

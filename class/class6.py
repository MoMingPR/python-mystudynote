class new_class():
    variable_a = 1000
    variable_b = 2000

    @classmethod
    def new_function(cls):
        print(cls.variable_a)
        print(cls.variable_b)

new_class.new_function()
#类
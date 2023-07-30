x_global = 0
y_global = 0
z_global = 0

def test_function():
    global x_global
    global y_global
    global z_global

    x_global = 5
    y_global = 5
    z_global = 5
    print(x_global, y_global, z_global)

def test_function2():
    global x_global
    global y_global
    global z_global

    x_global = 7
    y_global = 7
    z_global = 7

    print(x_global, y_global, z_global)

test_function()
test_function2()
x_global = 4
y_global = 0
z_global = 0
print(x_global, y_global, z_global)
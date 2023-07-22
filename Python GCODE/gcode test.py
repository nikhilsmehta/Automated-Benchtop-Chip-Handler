import mecode
g = mecode.G(direct_write=True, direct_write_mode="serial", printer_port="/dev/tty.usbmodem1411", baudrate=115200)

g.move(x=10, y=10, z=0, F=500)
g.current_position()

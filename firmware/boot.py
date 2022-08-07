import storage
import usb_cdc
import usb_midi
import board
import digitalio
import supervisor

#button = digitalio.DigitalInOut(board.GP28)
#button.pull = digitalio.Pull.UP
#
## remove jumper at GPIO28 to enable py upload
#if not button.value:
#    # see https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial
#    storage.disable_usb_drive()
#    usb_cdc.disable()
#    usb_midi.disable()
#
#button.deinit()

# supposedly enables keyboard use before OS load
# see http://kmkfw.io/docs/boot
usb_hid.enable(boot_device=1)

# from kmk boot.py
supervisor.set_next_stack_limit(4096 + 4096)

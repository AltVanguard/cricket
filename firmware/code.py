import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = \
    (board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0)
keyboard.row_pins = (board.GP12, board.GP13, board.GP10, board.GP11, board.GP8, board.GP9, board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESCAPE, KC.A,   KC.KP_SLASH,      KC.UP,   KC.KP_ASTERISK,     KC.S,
     KC.SPACE,  KC.NO,  KC.LSFT(KC.TAB),  KC.DOWN, KC.TAB,          KC.Z,
        KC.D,  KC.NO,  KC.G, KC.H, KC.J,  KC.NO,
     KC.X, KC.C,    KC.V, KC.B, KC.N, KC.M,
        KC.N2, KC.N3,  KC.NO,  KC.N5, KC.N6, KC.N7,
     KC.Q,  KC.W,  KC.E,    KC.R,  KC.T,  KC.Y,
         KC.NO,  KC.N9, KC.N0,  KC.NO,       KC.EQUAL,   KC.NO,
     KC.U,    KC.I,  KC.O,  KC.P,    KC.LBRACKET,  KC.RBRACKET]
] 

#keyboard.debug_enabled = True
if __name__ == '__main__':
    keyboard.go()

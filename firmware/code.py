import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

def FoldKeymap(unfolded_keymap, num_unfolded_columns: int, num_folded_columns: int):
    if num_unfolded_columns % num_folded_columns != 0:
        raise ValueError("num_unfolded_columns must be divisible by num_folded_columns")
        
    folded_layers = []
    for layer in unfolded_keymap:
        folded_layer = []
        layer_size = len(layer)
        block_size = (layer_size / num_unfolded_columns) * num_folded_columns
        for i in range(0, layer_size):
            row_offset = (int(i / num_folded_columns) * num_unfolded_columns) % layer_size
            block_offset = int(i / block_size) * num_folded_columns
            column_offset = i % num_folded_columns
            folded_layer.append(layer[row_offset + block_offset + column_offset])
        folded_layers.append(folded_layer)
    return folded_layers
    

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = \
    (board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0)
keyboard.row_pins = (board.GP12, board.GP13, board.GP10, board.GP11, board.GP8, board.GP9, board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

unfolded_keymap = [
    [KC.ESCAPE, KC.A,      KC.KP_SLASH,     KC.UP,   KC.KP_ASTERISK,     KC.S, KC.D,  KC.NO,  KC.G, KC.H, KC.J,  KC.NO,  KC.N2, KC.N3,  KC.NO,  KC.N5, KC.N6, KC.N7,  KC.NO,  KC.N9, KC.N0,  KC.NO,       KC.EQUAL,   KC.NO,
     KC.SPACE,  KC.MO(1),  KC.LSFT(KC.TAB), KC.DOWN, KC.TAB,          KC.Z, KC.X, KC.C,    KC.V, KC.B, KC.N, KC.M,    KC.Q,  KC.W,  KC.E,    KC.R,  KC.T,  KC.Y,  KC.U,    KC.I,  KC.O,  KC.P,    KC.LBRACKET,  KC.RBRACKET],
    [KC.LCTL(KC.BSLASH), KC.BSLASH,  KC.KP_MINUS,      KC.UP,   KC.KP_PLUS,     KC.F13, KC.F14,  KC.NO,  KC.F15, KC.F16, KC.F17,  KC.NO,  KC.F18, KC.F19,  KC.NO,  KC.SCROLLLOCK, KC.GRAVE, KC.LALT(KC.T),  KC.NO,  KC.LCTL(KC.Y), KC.LCTL(KC.Z),  KC.NO, KC.DELETE, KC.NO,
     KC.LSFT(KC.SPACE), KC.NO,     KC.LSFT(KC.TAB), KC.DOWN, KC.TAB,          KC.N0, KC.N1, KC.N2,    KC.N3, KC.N4, KC.N5, KC.N6,    KC.N7,  KC.N8,  KC.N9,    KC.A,  KC.B,  KC.C,  KC.D,    KC.E,  KC.F,  KC.LALT(KC.F3), KC.LALT(KC.F4), KC.LALT(KC.F5)],
]

keyboard.keymap = FoldKeymap(unfolded_keymap, 24, 6)

#keyboard.debug_enabled = True
if __name__ == '__main__':
    keyboard.go()

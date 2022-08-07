# Cricket: a keyboard for music trackers

*This is a Work In Progress project. 3D models, firmware code and documentation are incomplete.*

The **Cricket** is a 3D printable DIY special purpose keyboard for tracker style Digital Audio Workstation software, chiefly for use with [Renoise](https://www.renoise.com/). Once built, it is completly Plug-and-Play, no drivers or computer setup. The computer detects it as a regular computer USB keyboard and in fact the **Cricket**'s note keys will type letters and numbers in any software (e.g. Notepad) other than music trackers. **Cricket**'s firmware doesn't offer MIDI functionality yet, and the keys have no velocity sensitivity.

Other music tracker software also commonly use alphanumeric keys for note input, thus **Cricket** probably works with them as well. Control keys (toggling edit mode, play-pause, note-off, etc.) are only set up for Renoise, but feel free to adjust the key assignmets and firmware to your liking, adapt it to your favorite tracker.

The **Cricket** uses a raspberry pi pico microcontroller and its firmware is implemented with KMK (CircuitPython). The top plate is designed to accept Cherry MX style keyswitches.

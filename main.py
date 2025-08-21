import pyglet

from Keyboard_Module import Keyboard_Module as Key

def main():
    window = pyglet.window.Window(800, 500)
    keys = Key.Keyboard_Module(window, ["Q", "W", "E", "R", "T", "Y", ["LCTRL", "left ctrl"]])
    
    
    
    labels = []
    for iv in range(0, 4):
        labels.append([])
        for ih in range(0, keys.codes_len):
            if iv == 0:
                text = keys.active_codes[ih]
            else:
                text = "test"
            labels[iv].append(pyglet.text.Label(
                text = text,
                font_name = "Times New Roman",
                font_size = 32,
                x = 100 + ih * 100,
                y = 400 - iv * 100,
                anchor_x = "center",
                anchor_y = "center",
                color = (255, 255, 255)
            ))



    # ESC無効化
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            return True
    window.push_handlers(on_key_press)

    def update(dt):
        keys.Update()
        for ih in range(0, keys.codes_len):
            labels[1][ih].text = str(keys.pressed[ih])
            labels[2][ih].text = str(keys.active[ih])
            labels[3][ih].text = str(keys.inactive[ih])

    @window.event
    def on_draw():
        window.clear()
        for buffer in labels:
            for label in buffer:
                label.draw()

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()

if __name__ == '__main__':
    main()

from glem.pyglet.gtk3 import PygletWidget


def run():
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    win = Gtk.Window()

    widget = PygletWidget()

    @widget.event
    def on_draw():
        print("widget.on_draw")

    win.add(widget)
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    run()

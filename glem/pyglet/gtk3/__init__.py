from gi.repository import Gtk
from pyglet.window import EventDispatcher
from pyglet import gl, graphics


class PygletWidget(EventDispatcher, Gtk.Box):
    def __init__(self, *args, **kwargs):
        EventDispatcher.__init__(self)
        Gtk.Box.__init__(self, *args, **kwargs)
        gl_area = Gtk.GLArea()
        gl_area.show()
        gl_area.realize()

        def connect(signal, f, args_index=None, kwargs_keys=None):
            rearrange_args = args_index != None
            rearrange_kwargs = kwargs_keys != None

            def run(*args, **kwargs):
                if rearrange_args:
                    args = [args[i] for i in args_index]

                if rearrange_kwargs:
                    kwargs = {k: kwargs for k in kwargs_keys}

                f(*args, **kwargs)
                return True

            gl_area.connect(signal, run)

        connect('render', self.on_draw, [])
        connect('resize', self.on_resize, [1, 2])

        self.pack_end(gl_area, True, True, 0)

    def on_draw(self):
        print("self, on_draw")
        gl.glClearColor(128, 64, 0, 128)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    def on_resize(self, width, height):
        """A default resize event handler.

        This default handler updates the GL viewport to cover the entire
        window and sets the ``GL_PROJECTION`` matrix to be orthogonal in
        window space.  The bottom-left corner is (0, 0) and the top-right
        corner is the width and height of the window in pixels.

        Override this event handler with your own to create another
        projection, for example in perspective.
        """
        print("self, on_resize")
        # XXX avoid GLException by not allowing 0 width or height.
        gl.glViewport(0, 0, width, height)
        # gl.glMatrixMode(gl.GL_PROJECTION)
        # gl.glLoadIdentity()
        # gl.glOrtho(0, width, 0, height, -1, 1)
        # gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glClearColor(0, 0, 0, 128)

        #gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        return True

    def set_fullscreen(self, fullscreen=True, screen=None, mode=None,
                       width=None, height=None):
        raise NotImplemented()

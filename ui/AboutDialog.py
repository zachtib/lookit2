import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class AboutDialog(Gtk.AboutDialog):
    def _init(self, *args, **kwargs):
        super()._init(*args, **kwargs)
        self.show_all()
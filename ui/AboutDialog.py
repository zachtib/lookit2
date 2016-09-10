import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

import config

class AboutDialog(Gtk.AboutDialog):
    def _init(self, *args, **kwargs):
        super()._init(*args, **kwargs)

        self.set_program_name(config.program_name)
        self.set_version(config.program_version)
        self.set_copyright(config.copyright_string)
        self.set_authors([config.program_author])
        self.set_website(config.program_website)
        self.set_website_label(config.program_website_label)

        self.show_all()
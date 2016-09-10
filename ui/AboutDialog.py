import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class AboutDialog(Gtk.AboutDialog):
    def _init(self, *args, **kwargs):
        super()._init(*args, **kwargs)

        self.set_program_name('Lookit')
        self.set_version('2.0.0')
        self.set_copyright('(c) 2016 Zach Tibbitts')
        self.set_authors(['Zach Tibbitts'])
        self.set_website('https://github.com/zachtib/lookit2')
        self.set_website_label('Lookit2 on GitHub')

        self.show_all()
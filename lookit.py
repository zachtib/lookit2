import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Gio
from os.path import dirname

import sys

from ui.AboutDialog import AboutDialog
from ui.MainWindow import MainWindow
from upload.PluginLoader import PluginLoader

class Lookit(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id='com.zachtib.lookit',
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
                         **kwargs)

        self.loader = PluginLoader()
        self.loader.load_from_directory(dirname(__file__) + '/upload/plugins/');

        for plugin in self.loader.get_plugin_names():
            print(self.loader.get_plugin(plugin).do_upload("Test"))

        self.window = None
        self.about_dialog = None

        self.add_main_option('test', ord('t'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.NONE, "Command line test", None)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        menu = Gio.Menu()
        menu.append("About", "app.about")
        menu.append("Quit", "app.quit")
        self.set_app_menu(menu)

        # option "about"
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_about)
        self.add_action(about_action)

        # option "quit"
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit)
        self.add_action(quit_action)

    def do_activate(self):
        if not self.window:
            self.window = MainWindow(application=self, title="Lookit Settings")

        self.window.present()

    def do_command_line(self, command_line):
        options = command_line.get_options_dict()

        if options.contains("test"):
            # This is printed on the main instance
            print("Test argument recieved")

        self.activate()
        return 0

    def on_about(self, action, parameter):
        if not self.about_dialog:
            self.about_dialog = AboutDialog(self.window, application=self, title="About Lookit")

        self.about_dialog.present()

    def on_quit(self, action, parameter):
        self.quit()

if __name__=='__main__':
    app = Lookit()
    app.run(sys.argv)
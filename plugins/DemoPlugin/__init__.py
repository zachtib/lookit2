#DemoPlugin
class DemoPlugin:
    def __init__(self):
        pass

    def do_upload(self, filename):
        """Upload filename and return the result"""
        return filename

def get_plugin():
    return DemoPlugin()
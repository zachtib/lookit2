class TestPlugin:
    def __init__(self):
        super().__init__()

    def get_descriptive_name(self):
        return "Example Lookit Plugin"

    def do_upload(self, filename):
        """Upload filename and return a url"""
        return filename

def get_plugin():
    return TestPlugin()
from test_app.task_four.app import App


class TestMarkers:
    def setup(self):
        self.app = App()
        self.app.start()
        self.main = self.app.goto_main()

    # def teardown(self):
    #     self.app.stop()


    def test_marker(self):
        toast = self.main.goto_markers().goto_searchs().search()



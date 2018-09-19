import unittest
import starterbot

class TestingCauseYouToldMeToo(unittest.TestCase):

    def setUp(self):
        pass

    def test_commands(self):
        self.assertIn(starterbot.handle_command("just_joined", starterbot.event["channel"]), "Hello")


if __name__ == "__main__":
    unittest.main()
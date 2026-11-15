import builtins
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import main


class DisplayLanguageTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.language_file = Path(self.temp_dir.name) / "language.json"
        self.language_file_patch = patch.object(main, "LANGUAGE_FILE", self.language_file)
        self.language_file_patch.start()
        self.addCleanup(self.language_file_patch.stop)
        self.addCleanup(self.temp_dir.cleanup)

    def test_missing_setting_defaults_to_korean(self):
        self.assertEqual(main.load_language(), "ko")

    def test_language_setting_persists(self):
        main.save_language("en")

        self.assertEqual(main.load_language(), "en")
        self.assertEqual(json.loads(self.language_file.read_text(encoding="utf-8")), {"language": "en"})

        def test_invalid_language_setting_uses_default(self):
        self.language_file.write_text('{"language": "fr"}', encoding="utf-8")
        output = StringIO()

        with redirect_stdout(output):
            self.assertEqual(main.load_language(), "ko")

        self.assertIn("한국어로 시작합니다", output.getvalue())

    def test_broken_json_uses_default(self):
        self.language_file.write_text('{broken json', encoding="utf-8")

        with redirect_stdout(StringIO()):
            self.assertEqual(main.load_language(), "ko")

    def test_invalid_structure_uses_default(self):
        for settings in [[], {}, {"language": []}, {"language": None}]:
            with self.subTest(settings=settings):
                self.language_file.write_text(
                    json.dumps(settings),
                    encoding="utf-8",
                )

                with redirect_stdout(StringIO()):
                    self.assertEqual(main.load_language(), "ko")

    def test_read_error_uses_default(self):
        with patch.object(
            Path,
            "open",
            side_effect=PermissionError("읽기 불가"),
        ):
            with redirect_stdout(StringIO()):
                self.assertEqual(main.load_language(), "ko")

    def test_menu_language_change_applies_and_persists(self):
        output = StringIO()
        with patch.object(builtins, "input", side_effect=["5", "2", "6"]):
            with redirect_stdout(output):
                main.run_game()

        self.assertIn("Display language set to English.", output.getvalue())
        self.assertIn("My Quiz Game", output.getvalue())
        self.assertEqual(main.load_language(), "en")

    def test_english_input_validation(self):
        output = StringIO()
        with patch.object(builtins, "input", side_effect=["", "abc", "0", "2"]):
            with redirect_stdout(output):
                value = main.read_int("Select: ", 1, 2, "en")

        self.assertEqual(value, 2)
        self.assertIn("Input is empty.", output.getvalue())
        self.assertIn("That is not a valid integer.", output.getvalue())
        self.assertIn("between 1 and 2", output.getvalue())


if __name__ == "__main__":
    unittest.main()

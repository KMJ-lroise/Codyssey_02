import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main


class StateFileErrorTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.state_file = Path(folder.name) / "state.json"

        state_patch = patch.object(main, "STATE_FILE", self.state_file)
        state_patch.start()
        self.addCleanup(state_patch.stop)

        language_patch = patch.object(main, "load_language", return_value="ko")
        language_patch.start()
        self.addCleanup(language_patch.stop)

        data = {
            "quizzes": [q.to_dict() for q in main.create_default_quizzes()],
            "best_score": 80,
        }
        self.state_file.write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )
        self.original = self.state_file.read_bytes()

    def test_read_error_blocks_saving(self):
        with patch.object(Path, "open", side_effect=PermissionError("read denied")):
            game = main.QuizGame()

        self.assertFalse(game.can_save)
        self.assertEqual(len(game.quizzes), 5)
        self.assertIsNone(game.best_score)
        self.assertFalse(game.save_state())
        self.assertEqual(self.state_file.read_bytes(), self.original)

    def test_write_error_preserves_saved_data(self):
        game = main.QuizGame()
        game.best_score = 100

        with patch.object(Path, "open", side_effect=PermissionError("write denied")):
            result = game.save_state()

        self.assertFalse(result)
        self.assertEqual(self.state_file.read_bytes(), self.original)

    def test_replace_error_preserves_saved_data(self):
        game = main.QuizGame()
        game.best_score = 100

        with patch.object(Path, "replace", side_effect=OSError("replace failed")):
            result = game.save_state()

        self.assertFalse(result)
        self.assertEqual(self.state_file.read_bytes(), self.original)

    def test_backup_error_preserves_broken_file(self):
        self.state_file.write_text("{broken json", encoding="utf-8")
        broken = self.state_file.read_bytes()

        with patch.object(Path, "rename", side_effect=PermissionError("backup denied")):
            game = main.QuizGame()

        self.assertFalse(game.can_save)
        self.assertFalse(game.save_state())
        self.assertEqual(self.state_file.read_bytes(), broken)


if __name__ == "__main__":
    unittest.main()
    
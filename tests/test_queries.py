import unittest
import subprocess
import os
from pathlib import Path
import sys


class TestQueries(unittest.TestCase):
    def test_execute_scripts(self):
        root = Path(__file__).resolve().parent.parent
        # directory containing all the queries
        execute_dir = root / "execute"

        env = os.environ.copy()
        env["PYTHONPATH"] = str(root)

        for script_path in execute_dir.glob("*.py"):
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                env=env,
                cwd=root,
                check=False,
                shell=False,
            )
            self.assertEqual(
                result.returncode,
                0,
                f"Script {script_path} failed with error: {result.stderr}",
            )

#!/usr/bin/env python3
"""
Unit Test Execution Script for Maya HTT GTM Toolkit
Runs every module script as a subprocess and verifies it exits cleanly.
"""
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).parent

def discover_scripts():
    return sorted(REPO_ROOT.glob("*.py"))

class TestMayaHTTToolkit(unittest.TestCase):
    pass

def make_test(script_path):
    def test(self):
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True, text=True, timeout=30
        )
        self.assertEqual(
            result.returncode, 0,
            msg=f"{script_path} failed:\n{result.stderr}"
        )
    return test

for script in discover_scripts():
    if script.name == "test_toolkit.py":
        continue
    test_name = f"test_{script.stem}"
    setattr(TestMayaHTTToolkit, test_name, make_test(script))

if __name__ == "__main__":
    print("=== RUNNING MAYA HTT TOOLKIT SUITE VERIFICATION ===")
    scripts = [s for s in discover_scripts() if s.name != "test_toolkit.py"]
    print(f"[+] Discovered {len(scripts)} module scripts\n")
    unittest.main(verbosity=2)

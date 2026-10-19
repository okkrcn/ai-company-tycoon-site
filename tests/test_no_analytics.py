"""Public support pages no longer collect visits or mount analytics permission UI."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DeselectedAnalyticsTests(unittest.TestCase):
    def test_public_pages_do_not_load_counter_or_permission_ui(self):
        for name in ("index.html", "gizlilik.html", "destek.html"):
            with self.subTest(page=name):
                html = (ROOT / name).read_text()
                self.assertNotIn('src="moskai-visitor.js"', html)
                self.assertNotIn('href="moskai-consent.css"', html)
        self.assertFalse((ROOT / "moskai-visitor.js").exists())
        self.assertFalse((ROOT / "moskai-consent.css").exists())

    def test_privacy_copy_describes_current_non_tracking_site_in_both_languages(self):
        text = (ROOT / "gizlilik.html").read_text()
        self.assertIn("Bu sitede ziyaretçi analitiği kapalıdır.", text)
        self.assertIn("Visitor analytics is disabled on this website.", text)
        self.assertNotIn("“Ölçüm tercihi”", text)
        self.assertNotIn("“Measurement preference”", text)


if __name__ == "__main__":
    unittest.main()

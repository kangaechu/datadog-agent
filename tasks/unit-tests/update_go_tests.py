import unittest

from tasks.update_go import (
    PATTERN_MAJOR_MINOR,
    PATTERN_MAJOR_MINOR_BUGFIX,
    _get_major_minor_version,
    _get_pattern,
    _update_go_mods,
    _update_references,
)


class TestUpdateGo(unittest.TestCase):
    def test_get_minor_version(self):
        self.assertEqual(_get_major_minor_version("1.2.3"), "1.2")

    def test_get_pattern(self):
        self.assertEqual(_get_pattern("p+e", "p.st", is_bugfix=True), rf'(p\+e){PATTERN_MAJOR_MINOR_BUGFIX}(p\.st)')
        self.assertEqual(_get_pattern("p(re)", "p*st", is_bugfix=False), rf'(p\(re\)){PATTERN_MAJOR_MINOR}(p\*st)')

    def test_file_patterns(self):
        _update_references(warn=False, version="1.2.3", dry_run=True)

    def test_go_mods(self):
        _update_go_mods(warn=False, minor="1.2", include_otel_modules=True, dry_run=True)

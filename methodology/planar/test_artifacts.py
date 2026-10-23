"""Portable artifact checks; does not run or certify FEM."""
from pathlib import Path
import hashlib
import json
import re
import unittest
from export_formulas import extract

ROOT = Path(__file__).resolve().parent

class ArtifactTests(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(extract(r'\begin{equation}x=1\label{eq:x}\end{equation}'),
                         [{'sequence': 1, 'labels': ['eq:x'], 'latex': r'x=1\label{eq:x}'}])
        self.assertEqual(extract('plain text'), [])

    def test_formula_export(self):
        source = ROOT / 'Metodika_planarnyh_drosseley_i_transformatorov.tex'
        index = json.loads((ROOT / 'formulas/index.json').read_text(encoding='utf8'))
        self.assertEqual(index['sha256'], hashlib.sha256(source.read_text(encoding='utf8').encode('utf8')).hexdigest())
        self.assertEqual(index['equations'], extract(source.read_text(encoding='utf8')))
        self.assertEqual(index['count'], 45)

    def test_references(self):
        text = (ROOT / 'Metodika_planarnyh_drosseley_i_transformatorov.tex').read_text(encoding='utf8')
        labels = re.findall(r'\\label\{([^}]+)\}', text)
        refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', text)
        self.assertEqual(len(labels), len(set(labels)))
        self.assertTrue(set(refs) <= set(labels))
        self.assertIn(r'\psi', text)
        self.assertNotIn(r'\lambda', text)
        self.assertNotIn(r'\baseeq', text)

    def test_review_inventory(self):
        rows = json.loads((ROOT / 'sources_review.json').read_text(encoding='utf8'))
        self.assertEqual(len(rows), 89)
        self.assertEqual(len({r['id'] for r in rows}), 89)
        self.assertEqual(sum(r['read_status']=='blocked_no_fulltext' for r in rows), 65)
        self.assertEqual(sum(r['read_status']=='not_fully_read' for r in rows), 10)

    def test_recorded_build_checks(self):
        report = json.loads((ROOT / 'independent_verification.json').read_text(encoding='utf8'))
        self.assertTrue(all(report['checks'].values()))
        self.assertEqual(report['pages'], 60)

if __name__ == '__main__':
    unittest.main(verbosity=2)

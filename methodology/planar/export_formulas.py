"""Export exact numbered equation environments, not lossy PDF text. No solver needed."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
TEX = ROOT / 'Metodika_planarnyh_drosseley_i_transformatorov.tex'


def extract(text):
    equations = re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}', text, re.S)
    return [{'sequence': i, 'labels': re.findall(r'\\label\{([^}]+)\}', body),
             'latex': body.strip()} for i, body in enumerate(equations, 1)]


def main():
    data = extract(TEX.read_text(encoding='utf8'))
    if not data:
        raise ValueError('No equations found')
    out = ROOT / 'formulas'
    out.mkdir(exist_ok=True)
    manifest = {'source': TEX.name, 'sha256': hashlib.sha256(TEX.read_text(encoding='utf8').encode('utf8')).hexdigest(),
                'hash_convention': 'UTF-8 text with LF newlines',
                'count': len(data), 'scope': 'Numbered equation environments only; inline math remains in source. Sequence is extraction order, not a guaranteed printed equation number.',
                'equations': data}
    (out / 'index.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
    lines = ['# Формулы самостоятельной методики', '', 'Точный LaTeX из исходника. Это не независимая физическая верификация. Номер ниже — порядок извлечения; для ссылок используйте метки. Встроенные формулы остаются в полном документе.', '']
    for eq in data:
        lines += [f'## {eq["sequence"]}: '+', '.join(eq['labels']), '', '```latex', eq['latex'], '```', '']
    (out / 'INDEX.md').write_text('\n'.join(lines), encoding='utf8')
    print(f'Exported {len(data)} equations')


if __name__ == '__main__':
    main()

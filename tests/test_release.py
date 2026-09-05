import json
import zipfile
from pathlib import Path

from notebooklm_hub.release import build_release


def test_build_release_creates_full_and_component_archives(tmp_path: Path):
    root = tmp_path / 'repo'
    (root / 'research').mkdir(parents=True)
    (root / 'docs').mkdir()
    (root / 'src' / 'notebooklm_hub').mkdir(parents=True)
    (root / 'packages' / 'publisher').mkdir(parents=True)
    (root / 'packages' / 'skills' / 'research').mkdir(parents=True)
    (root / 'README.md').write_text('# Hub\n', encoding='utf-8')
    (root / 'CHANGELOG.md').write_text('# Changelog\n', encoding='utf-8')
    (root / 'research' / 'a.md').write_text('research', encoding='utf-8')
    (root / 'docs' / 'a.md').write_text('docs', encoding='utf-8')
    (root / 'src' / 'notebooklm_hub' / '__init__.py').write_text('', encoding='utf-8')
    (root / 'packages' / 'publisher' / 'pub.py').write_text('', encoding='utf-8')
    (root / 'packages' / 'skills' / 'research' / 'SKILL.md').write_text('skill', encoding='utf-8')

    out = tmp_path / 'dist'
    manifest = build_release(root, out, version='0.1.0')

    expected = {
        'notebooklm-hub-0.1.0-full.zip',
        'notebooklm-hub-0.1.0-research.zip',
        'notebooklm-hub-0.1.0-runtime.zip',
        'notebooklm-hub-0.1.0-publisher.zip',
        'notebooklm-hub-0.1.0-skills.zip',
        'notebooklm-hub-0.1.0-docs.zip',
    }
    assert expected <= {p.name for p in out.glob('*.zip')}
    assert manifest['version'] == '0.1.0'
    assert set(manifest['archives']) == expected
    saved = json.loads((out / 'release-manifest.json').read_text(encoding='utf-8'))
    assert saved['archives'].keys() == manifest['archives'].keys()
    for name in expected:
        with zipfile.ZipFile(out / name) as zf:
            assert zf.namelist()

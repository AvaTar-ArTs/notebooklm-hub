import json
from pathlib import Path

from notebooklm_hub.cli import main


def test_doctor_reports_repository_capabilities(tmp_path: Path, capsys):
    (tmp_path / 'research').mkdir()
    (tmp_path / 'src' / 'notebooklm_hub').mkdir(parents=True)
    (tmp_path / 'tests').mkdir()
    rc = main(['doctor', '--root', str(tmp_path), '--json'])
    assert rc == 1
    data = json.loads(capsys.readouterr().out)
    assert data['research'] is True
    assert data['runtime'] is True
    assert data['tests'] is True
    assert data['provenance'] is False


def test_doctor_fails_when_repository_is_incomplete(tmp_path: Path):
    assert main(['doctor', '--root', str(tmp_path), '--json']) == 1


def test_release_command_builds_archives(tmp_path: Path):
    (tmp_path / 'README.md').write_text('# Hub\n', encoding='utf-8')
    rc = main(['release', '--root', str(tmp_path), '--out', str(tmp_path / 'dist'), '--version', '0.1.0'])
    assert rc == 0
    assert (tmp_path / 'dist' / 'notebooklm-hub-0.1.0-full.zip').exists()

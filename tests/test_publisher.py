from pathlib import Path

from packages.publisher.notebooklm_hub_publisher import publish


def test_publish_copies_artifacts_and_uses_internal_relative_links(tmp_path: Path):
    archive = tmp_path / 'archive'
    source = archive / 'Research Notebook' / 'source.txt'
    source.parent.mkdir(parents=True)
    source.write_text('evidence', encoding='utf-8')

    output = tmp_path / 'site'
    build = publish(archive, output)

    copied = build / 'artifacts' / 'Research Notebook' / 'source.txt'
    page = build / 'notebooks' / 'research-notebook.html'
    assert copied.read_text(encoding='utf-8') == 'evidence'
    page_text = page.read_text(encoding='utf-8')
    assert 'href="../artifacts/Research%20Notebook/source.txt"' in page_text

from notebooklm_hub.models import SourceRecord, EvidenceRecord, ArtifactManifest


def test_source_record_keeps_provider_out_of_identity():
    source = SourceRecord(id='src-1', title='Paper', kind='pdf', provider='notebooklm')
    assert source.id == 'src-1'
    assert source.provider == 'notebooklm'
    assert source.to_dict()['title'] == 'Paper'


def test_evidence_record_requires_classification():
    evidence = EvidenceRecord(id='ev-1', claim='Notebook is bounded', classification='OFFICIAL_CURRENT', source_ids=['src-1'])
    assert evidence.classification == 'OFFICIAL_CURRENT'
    assert evidence.source_ids == ['src-1']


def test_artifact_manifest_tracks_lineage():
    artifact = ArtifactManifest(id='art-1', kind='audio', source_ids=['src-1'], parent_artifact_ids=['art-0'], format='mp3')
    data = artifact.to_dict()
    assert data['source_ids'] == ['src-1']
    assert data['parent_artifact_ids'] == ['art-0']

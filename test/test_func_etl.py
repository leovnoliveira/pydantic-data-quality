from app.etl import load_settings, exctracao, transformacao, load


def test_config():
    assert load_settings() is not None

from app.etl_inferschema import load_settings


def test_config():
    assert load_settings() is not None

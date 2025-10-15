from app.etl import configuracao, exctracao, transformacao, load


def  test_config():
    assert configuracao is not None
    
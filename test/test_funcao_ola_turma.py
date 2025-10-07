from app.funcao import ola_turma


def test_funcao_ola_turma_retorna_ola_jornada():
    ouput = ola_turma()
    gabarito = "ola jornada"
    assert ouput == gabarito
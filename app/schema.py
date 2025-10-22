import pandera as pa
from pandera import Column


def ProdutoSchema() -> pa.DataFrameSchema:
    """Schema para validação dos dados de produtos"""
    schema = pa.DataFrameSchema({
        "id_produto": Column(int, checks=pa.Check.gt(0)),
        "nome": Column(str, checks=[pa.Check.str_length(min_value=20, max_value=200)]),
        "preco": Column(float, checks=pa.Check.in_range(5.0, 120.0)),
        "quantidade": Column(float, checks=pa.Check.in_range(0.0, 1000.0)),
        "categoria": Column(str, checks=pa.Check.str_length(min_value=3, max_value=50)),
    })
    return schema
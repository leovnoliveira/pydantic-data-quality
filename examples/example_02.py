import numpy as np
import pandas as pd
import pandera.pandas as pa

df = pd.DataFrame({"column1": [5, 1, np.nan]})

non_null_schema = pa.DataFrameSchema({
    "column1": pa.Column(float, pa.Check(lambda x: x > 0))
})

try:
    non_null_schema.validate(df)
except pa.errors.SchemaError as exc:
    print(exc)

null_schema = pa.DataFrameSchema({
    "column1": pa.Column(float, pa.Check(lambda x: x > 0), nullable=True)
})

null_schema.validate(df)
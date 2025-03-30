import pandas as pd
from pathlib import Path

import cryptnumpy as crp

test_dir = Path(__file__).parent.parent / 'tests'
out_path = test_dir / 'file.crypt'

df = pd.DataFrame({"A": [1, 2, 3], "B": ["foo", "bar", "baz"]})

crp.to_encrypted(df, password='somePassword', path=out_path)
decrpyted_df = crp.read_encrypted(
    out_path,
    password='somePassword',
    use_pandas=True
)

print(decrpyted_df.equals(df))

out_path.unlink()

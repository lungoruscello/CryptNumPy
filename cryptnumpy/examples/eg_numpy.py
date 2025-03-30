import numpy as np
from pathlib import Path

import cryptnumpy as crp

test_dir = Path(__file__).parent.parent / 'tests'
out_path = test_dir / 'file.crypt'

# regular numpy array
my_array = np.arange(25).reshape(5, 5)

crp.to_encrypted(my_array, password='APassWord', path=out_path)
decrypted_array = crp.read_encrypted(out_path, password='APassWord')

print(np.all(my_array == decrypted_array))


# dictionary of numpy arrays
my_array_dict = dict(
    arry1=np.array(['foo', 'bar', 'baz']),
    arry2=np.array(['qux', 'quux'])
)

crp.to_encrypted(my_array_dict, password='APassWord', path=out_path)
decrypted_dict = crp.read_encrypted(out_path, password='APassWord')

for name, original_array in my_array_dict.items():
    decrypted_array = decrypted_dict[name]
    print(np.all(original_array == decrypted_array))

out_path.unlink()

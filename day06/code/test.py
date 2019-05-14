from module1 import foo
foo()

from module2 import foo
foo()

from module2 import foo
from module1 import foo
foo()

import module1 as module1
import module2 as module2
module1.foo()
module2.foo()
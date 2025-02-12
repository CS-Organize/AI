# Package

## `__init__.py`
`__init__.py` 파일은 해당 디렉터리가 패키지의 일부임을 알려 주는 역할을 한다. 

```bash
../
export PYTHONPATH=$PYTHONPATH:$(pwd)
python3.12
```

```python
import package
package.print_version_info() # package/__init__.py
# The version of this game is 3.12.

import package.sound.echo as echo
echo.echo_test() # package/sound/echo.py
# I'm sound/echo.py

import graphic.render as render
render.render_test() # package/graphic/render.py
# I'm graphic/render.py

from package.sound import echo
echo.echo_test() # package/sound/echo.py 
# require __init__.py w
```

# This is an auto-generated file created by virtualenv for activating a virtual environment.
# It can be used to activate this virtual environment without directly sourcing the activate script.

import os
import site
import sys

try:
    __file__
except NameError:
    raise AssertionError("You must use this with exec(open(this_file).read(), {'__file__': this_file})")

# Path to the virtual environment
venv_path = os.path.dirname(os.path.abspath(__file__))
venv_path = os.path.dirname(venv_path)  # Go up one directory to get the virtual environment root

# Activate the virtual environment
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')

with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

# Update sys.path to include the virtual environment's site-packages
site_packages = os.path.join(venv_path, 'lib', 'python{}.{}'.format(*sys.version_info[:2]), 'site-packages')
prev_sys_path = list(sys.path)

# We add the venv's site-packages directories to sys.path
site.addsitedir(site_packages)

# We move the added items to the front of sys.path to prioritize them
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
sys.path[:] = new_sys_path + prev_sys_path

function clean-pyc { # Remove build artifacts
  find . -name '*.pyc' -exec rm --force {} +
  find . -name '*.pyo' -exec rm --force {} +
  find . -name '*~' -exec rm --force  {} +
}

function clean-build { #
  rm --force --recursive build/
  rm --force --recursive dist/
  rm --force --recursive *.egg-info
}

function activate { # Activate or install then activate
  if [ -e ./venv/ ]
  then
    echo activate
    source venv/bin/activate
    # python3 -m pip install --upgrade -r requirements.txt
  else
    python3 -m pip install --upgrade pip
  	python3 -m venv venv
  	activate
  	python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade -r requirements.txt
  fi
}

function lint { # PEP8
  activate
  flake8
}

function test { #
#test: clean-pyc
  py.test --verbose --color=yes $(TEST_PATH)
}


function requirements { #
	activate
	python3 -m pip install --upgrade -r requirements.txt
}

function jupyterlab { #
	activate
	jupyter serverextension enable --py jupyterlab --sys-prefix
	jupyter lab
}

function jupyterlablan { #
  activate
  jupyter serverextension enable --py jupyterlab --sys-prefix
	jupyter lab --ip=0.0.0.0 --port=80
}

function jupyter { #
	activate
	jupyter nbextension enable --py widgetsnbextension --sys-prefix
	jupyter notebook
}

function serialterm { # Serial Terminal
	activate
	python3 venv/scripts/miniterm.py
}

function visainfo { # PyVISA info
	activate
	python3 -m visa info # | less
}

function visashell { # PyVISA Shell
	activate
	echo http://pyvisa.readthedocs.io/en/stable/shell.html
	python3 -m visa shell
}

function runmain { #
	activate
	python3 main.py
}

function codestandards { #
	activate
	python3 -m py.test --flakes --pep8 --ignore=venv --ignore=Legacy
}
function editor { # Editor
	activate
	python3 -m idlelib
}

function menu { # list functions
  grep function "$0" | sort -d  | cut -d' ' -f2- | head -n-1 |  sed 's/{ #/██/'
}
menu

read repl
echo "$repl"
"$repl"

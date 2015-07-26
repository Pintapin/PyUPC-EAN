#!/usr/bin/env bash

bashexec="$(command -v bash)"
if hash realpath 2>/dev/null; then
 pyrealpath="$(command -v realpath)"
 uscriptdir="$(${pyrealpath} $(dirname $(readlink -f $0))/../../ubuntu/python3/)"
else
 pythonexec="$(command -v python3)"
 scriptdir="$(dirname $(readlink -f $0))"
 pyrealpath="${pythonexec} ${scriptdir}/realpath.py"
 scriptdir="$(${pyrealpath} ${scriptdir})"
 pyrealpath="${pythonexec} ${scriptdir}/realpath.py"
 uscriptdir="$(${pyrealpath} $(dirname $(readlink -f $0/))/../../ubuntu/python3)"
fi
pyscriptfile="${uscriptdir}/pydeb-gen.py"
pyshellfile="${uscriptdir}/pydeb-gen.sh"
codename="trusty"

if [ $# -eq 0 ]; then
 ${bashexec} "${pyshellfile}"
fi
if [ $# -gt 0 ]; then
 if [ $# -gt 1 ]; then
  codename="${2}"
 fi
 ${bashexec} "${pyshellfile}" "${1}" "${codename}"
fi

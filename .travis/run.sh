#!/bin/bash

set -e
set -x

TEMPDIR=${TMPDIR:-/tmp}
. $TEMPDIR/conan_bootstrap.sh

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

python build.py --build=missing --build=conan-arduino-toolchain

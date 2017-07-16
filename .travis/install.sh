#!/usr/bin/env bash

set -e
set -x

if [[ $TRAVIS == true ]]; then
    if [[ "$(uname -s)" == 'Darwin' ]]; then
        brew update || brew update
        brew outdated pyenv || brew upgrade pyenv
        brew install pyenv-virtualenv
        brew install cmake || true

        # brew tap caskroom/versions
        brew cask install java
        brew cask install arduino

        if which pyenv > /dev/null; then
            eval "$(pyenv init -)"
        fi

        pyenv install 2.7.10
        pyenv virtualenv 2.7.10 conan
        pyenv rehash
        pyenv activate conan
    fi
fi

# pip install conan --upgrade
# pip install conan_package_tools

echo "=============="
set
echo "=============="

TMP=$(mktemp -d)
git clone -b develop https://github.com/anton-matosov/conan.git $TMP/conan.git
git clone -b develop https://github.com/conan-io/conan-package-tools.git $TMP/conan-package-tools.git

pip install -r "$TMP/conan.git/conans/requirements.txt"


TEMPDIR=${TMPDIR:-/tmp}
echo -n """#!/usr/bin/env bash

export PYTHONPATH="$TMP/conan.git:$TMP/conan-package-tools.git:$PYTHONPATH"
export PATH="$TMP:$PATH"

""" > $TEMPDIR/conan_bootstrap.sh

. $TEMPDIR/conan_bootstrap.sh

echo -n """#!/usr/bin/env python

import sys
sys.path.append('$TMP/conan')

from conans.conan import main
main(sys.argv[1:])
""" > $TMP/conan
chmod +x $TMP/conan



conan user


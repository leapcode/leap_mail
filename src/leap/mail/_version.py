
IN_LONG_VERSION_PY = True
# This file helps to compute a version number in source trees obtained from
# git-archive tarball (such as those provided by githubs download-from-tag
# feature). Distribution tarballs (build by setup.py sdist) and build
# directories (produced by setup.py build) will contain a much shorter file
# that just contains the computed version number.

version_version = '0.3.9-rc1'
version_full = 'd361056ac3eb740e7eb9b5de85a82b2ceeb7a82b'


def get_versions(default={}, verbose=False):
        return {'version': version_version, 'full': version_full}

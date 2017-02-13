class BaseBackend(object):
    """
    Base class for all asset_versions backends
    """

    def version_short(self):
        """
        Return a short version of the version string - for example, in GIT it
        would be the first 6 characters of a commit hash.

        :return: Short version of the version string
        :rtype: str
        """
        raise NotImplementedError

    def version_long(self):
        """
        Return a long version of the version string - for example, in GIT it
        would be the full hash of a commit.

        :return:
        :rtype:
        """
        raise NotImplementedError

from django.conf import settings
from git import Repo

from asset_versions.backends import BaseBackend


class Git(BaseBackend):
    """
    GIT Backend for asset versions.
    """

    def __init__(self):
        """
        Git backend constructor.
        """
        repo_dir = settings.BASE_DIR
        if hasattr(settings, 'ASSET_REPO_DIR'):
            repo_dir = settings.REPO_DIR
        self.repo = Repo(repo_dir)

    def version_long(self):
        """
        Returns the full hash of the latest commit found.

        :return: Latest commit hash (full)
        :rtype: str
        """
        return self.repo.commit().hexsha

    def version_short(self):
        """
        Returns the short hash of the latest commit found.

        :return: Latest commit hash (short)
        :rtype: str
        """
        return self.repo.commit().hexsha[:6]


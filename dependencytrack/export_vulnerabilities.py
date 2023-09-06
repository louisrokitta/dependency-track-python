import logging

from .exceptions import DependencyTrackApiError

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Vulnerabilities:

    def get_vulnerabilities(self, uuid):
        response = self.session.get(self.api + "/finding/project/{uuid}/export".format(uuid=uuid), params=self.paginated_param_payload)
        if response.status_code == 200:
            return response.json()
        else:
            description = f"Unable to get vulnerabilities of project"
            raise DependencyTrackApiError(description, response)

from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:


    def __init__(self, app):
        self.app = app


    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self):
        project_list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
                                                                  self.app.config['webadmin']['password'])
        for row in projects:
            project_list.append(Project(name=row.name, status=row.status.name, view_status=row.view_state.name,
                                        description=row.description))
        return project_list

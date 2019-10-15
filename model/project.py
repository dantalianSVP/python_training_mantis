

class Project:

    def __init__(self, name, status=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description

    def __eq__(self, other):
        return self.name == other.name and \
               (self.status is None or other.status is None or self.status == other.status) and \
               (self.view_status is None or other.view_status is None or self.view_status == other.view_status) and \
               (self.description is None or other.description is None or self.description == other.description)

    def __repr__(self):
        return "Project(%s, %s, %s, %s)" % (self.name, self.status, self.view_status, self.description)
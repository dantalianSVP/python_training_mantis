

class Project:

    def __init__(self, app):
        self.app = app


    def open_page_for_create(self,app):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php") and
                len(wd.find_elements_by_name("manage_proj_create_page_token")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()



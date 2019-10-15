from selenium.webdriver.support.select import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php") and
                len(wd.find_elements_by_name("manage_proj_create_page_token")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        self.open_home_page()
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("status", project.status)
        self.change_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)
        if not (wd.find_element_by_name("inherit_global").is_selected() == project.inherit):
            wd.find_element_by_name("inherit_global").click()

    def select_field_value(self, select_param, select_value):
        wd = self.app.wd
        if select_value is not None:
            wd.find_element_by_name(select_param).click()
            Select(wd.find_element_by_name(select_param)).select_by_visible_text(select_value)
            wd.find_element_by_name(select_param).click()

    def find_project_id_by_name(self, name):
        wd = self.app.wd
        self.open_home_page()
        link = wd.find_element_by_link_text(name).get_attribute('href')
        id_project = link.split('=')[1]
        return id_project

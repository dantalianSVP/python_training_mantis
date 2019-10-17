from random import randrange
from model.project import Project
import operator


def test_del_project(app, start, db):
    if len(app.soap.get_projects()) == 0:
        app.project.create(Project(name="New_project"))
    old_project_list = app.soap.get_projects()
    index = randrange(len(old_project_list))
    app.project.delete_project_by_index(old_project_list[index].name)
    new_project_list = app.soap.get_projects()
    assert len(old_project_list) - 1 == len(new_project_list)
    old_project_list[index:index + 1] = []
    assert sorted(old_project_list, key=operator.attrgetter('name')) == sorted(new_project_list,
                                                                               key=operator.attrgetter('name'))

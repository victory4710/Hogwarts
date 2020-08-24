from Hogwarts.PageObject.Page.contact import Contact
from Hogwarts.PageObject.Page.main import MainPage


class TestAddDepartment:
    def test_add_department(self):
        main = MainPage()
        main.go_to_contact().go_to_add_department().add_department("菜菜子4")
        contact = Contact()
        result = contact.get_department_list()
        assert "菜菜子4" in result

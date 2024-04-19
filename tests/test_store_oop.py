class TestStore:

    def test_possibility_to_get_empty_catalog(self):
        result = self.store.show_catalog()
        assert not result
        assert isinstance(result, list)

    def test_add_to_catalog(self):
        result = self.store.add_phone_to_catalog('iPhone', 1)
        assert str(result) == 'iPhone at 1'

    def test_possibility_to_get_catalog(self):
        result = self.store.show_catalog()
        assert ['iPhone at 1'] == [str(phone) for phone in result]
        assert isinstance(result, list)

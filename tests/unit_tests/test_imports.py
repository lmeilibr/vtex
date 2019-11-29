def test_import_module():
    try:
        import vtex
        assert True
    except:
        assert False

def test_import_class():
    try:
        from vtex import Vtex
        assert True
    except:
        assert False

def test_import_module():
    try:
        import vtex
        assert True
    except ImportError:
        assert False

def test_import_class():
    try:
        from vtex import Vtex
        assert True
    except ImportError:
        assert False

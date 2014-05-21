import unittest


testmodules = [
    'test_tape',
    'test_rule'
]
suite = unittest.TestSuite()


for t in testmodules:
    try:
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))


unittest.TextTestRunner().run(suite)

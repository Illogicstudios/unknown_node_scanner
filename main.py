import importlib
from common import utils

utils.unload_packages(silent=True, package="unknown_node_scanner")
importlib.import_module("unknown_node_scanner")

from unknown_node_scanner.UnknownNodeScanner import UnknownNodeScanner
try:
    unknown_node_scanner.close()
except:
    pass
unknown_node_scanner = UnknownNodeScanner()
unknown_node_scanner.show()

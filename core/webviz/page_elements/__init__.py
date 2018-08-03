import pkg_resources

__all__ = []

for entry_point in pkg_resources.iter_entry_points('webviz_page_elements'):
    globals()[entry_point.name] = entry_point.load()
    __all__.append(entry_point.name)

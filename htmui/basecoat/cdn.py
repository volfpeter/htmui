from htmy import SafeStr

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com"

css = SafeStr(
    '<link rel="stylesheet" '
    'href="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/basecoat.cdn.min.css" />'
)

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/all.min.js" defer></script>'
)

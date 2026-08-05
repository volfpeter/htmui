from htmy import SafeStr

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com"

css = SafeStr(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/basecoat.cdn.min.css" />'
)

js = SafeStr('<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/all.min.js" defer></script>')

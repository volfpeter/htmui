from htmy import ComponentType, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/"


copy_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-6"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="M8.25 7.5V6.108c0-1.135.845-2.098 1.976-2.192.373-.03.748-.057 1.123-.08M15.75 18H18a2.25 '
    "2.25 0 0 0 2.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 0 0-1.123-.08M15.75 "
    "18.75v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5A3.375 3.375 "
    "0 0 0 6.375 7.5H5.25m11.9-3.664A2.251 2.251 0 0 0 15 2.25h-1.5a2.251 2.251 0 0 0-2.15 1.586m5.8 "
    "0c.065.21.1.433.1.664v.75h-6V4.5c0-.231.035-.454.1-.664M6.75 7.5H4.875c-.621 0-1.125.504-1.125 "
    '1.125v12c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V16.5a9 9 0 0 0-9-9Z" /></svg>'
)
"""`clipboard-document` icon from https://heroicons.com/."""


copy_button_click_handler = SafeStr("""
const button = this;
const code = this.parentElement.querySelector('pre code');
if (!code) return;
const clickedClass = 'text-green-700';
const svg = this.parentElement.querySelector('svg');
navigator.clipboard.writeText(code.textContent || '').then(() => {
  svg?.classList.add(clickedClass);
  setTimeout(() => {
    svg?.classList.remove(clickedClass);
  }, 2000);
}).catch(err => {
  console.error('Failed to copy text: ', err);
});""")
"""JavaScript for handling copy button click events."""


def copy_button(icon: ComponentType = copy_icon) -> ComponentType:
    return html.button(
        icon,
        onclick=copy_button_click_handler,
        class_=(
            "btn-icon-ghost size-8 absolute right-2.5 top-2 "
            "group hover:text-foreground text-muted-foreground"
        ),
    )


def codeblock(code: str, *, code_class: str | None = None) -> ComponentType:
    return html.pre(
        html.code(code, class_=join_classes(code_class, "!bg-muted/40 !p-3.5")),
        copy_button(),
        class_="grid text-sm max-h-[650px] overflow-y-auto rounded-xl scrollbar relative",
    )

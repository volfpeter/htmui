from htmy import ComponentType, SafeStr, html

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/theme-switcher/"

light_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-6"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 '
    "18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 "
    '12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" /></svg>'
)
"""`sun` icon from https://heroicons.com/."""

dark_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-6"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 '
    "0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 "
    '12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" /></svg>'
)
"""`moon` icon from https://heroicons.com/."""

js = SafeStr(
    """<script>
    (() => {
    try {
        const stored = localStorage.getItem('themeMode');
        if (stored ? stored === 'dark'
                    : matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.classList.add('dark');
        }
    } catch (_) {}

    const apply = dark => {
        document.documentElement.classList.toggle('dark', dark);
        try { localStorage.setItem('themeMode', dark ? 'dark' : 'light'); } catch (_) {}
    };

    document.addEventListener('basecoat:theme', (event) => {
        const mode = event.detail?.mode;
        apply(mode === 'dark' ? true
            : mode === 'light' ? false
            : !document.documentElement.classList.contains('dark'));
    });
    })();
</script>"""
)


def theme_switcher(class_: str = "btn-icon-outline size-8") -> ComponentType:
    return html.button(
        html.span(light_icon, class_="hidden dark:block"),
        html.span(dark_icon, class_="block dark:hidden"),
        type="button",
        aria_label="Toggle theme",
        data_tooltip="Toggle theme",
        data_side="bottom",
        onclick="document.dispatchEvent(new CustomEvent('basecoat:theme'))",
        class_=class_,
    )

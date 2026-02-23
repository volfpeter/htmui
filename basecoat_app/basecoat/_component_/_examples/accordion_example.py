from htmy import ComponentType, html

from htmui.basecoat import accordion


def example() -> ComponentType:
    return accordion.accordion(
        *(
            (
                _summary_template.format(i=i),
                html.div(*(html.p(_content_template.format(line=line, i=i)) for line in range(1, 4))),
            )
            for i in range(1, 6)
        ),
        root_class="w-full",
    )


_summary_template = "Accordion summary {i}"
_content_template = "{line}. Multiline content for accordion {i}"

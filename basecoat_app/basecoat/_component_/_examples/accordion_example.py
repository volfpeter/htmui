from htmy import ComponentType, html

from htmui.basecoat import accordion


def example() -> ComponentType:
    return accordion.accordion(
        *(
            accordion.accordion_item(
                html.div(
                    *(
                        html.p(
                            _content_template.format(line=line, i=i),
                        )
                        for line in range(1, 4)
                    )
                ),
                summary=_summary_template.format(i=i),
                open=i == 1,
            )
            for i in range(1, 6)
        ),
        class_="w-full",
    )


_summary_template = "Accordion summary {i}"
_content_template = "{line}. Multiline content for accordion {i}"

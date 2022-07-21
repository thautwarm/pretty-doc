## pretty-doc

```python
from __future__ import annotations  # 和Python的类型标注如`a: int`有关
from dataclasses import dataclass   # 根据类型标注生成数据记录类型，这样的类型有默认构造器
import pretty_doc as PD
from xml.sax.saxutils import escape

@dataclass
class XML:   # 定义XML的语法树
    name: str
    attributes: dict[str, object]
    children: list[XML | str]

def render_attributes(attributes: dict[str, object]) -> str:
    if not attributes:
        return ""
    
    return " " + " ".join(
        [f"{key}=\"{escape(str(value))}\"" for key, value in attributes.items()]
    )

def xml_to_doc(xml: XML):
    return PD.vsep([
        PD.seg("<") * PD.seg(xml.name) * PD.seg(render_attributes(xml.attributes)) * PD.seg(">"),
        PD.align(
            PD.vsep(
                [
                    xml_to_doc(child) if isinstance(child, XML) else PD.seg(escape(child))
                    for child in xml.children
                ]
            )
        ) >> 4,
        PD.seg("<") * PD.seg(xml.name) * PD.seg("/>"),
    ])

doc = xml_to_doc(
    XML(
        name="root",
        attributes={"a": 1, "b": 2},
        children=[
            XML(
                name="child",
                attributes={"c": 3, "d": 4},
                children=[
                    "child 1 text",
                    XML(
                        name="grandchild",
                        attributes={"e": 5, "f": 6},
                        children=["grandchild text", XML("More", {}, [])],
                    ),
                ]
            ),
            "root text",
            "root <>",
            XML("child", attributes={}, children=["child 2 text"]),
        ]
    )
)

print(doc.show())
```


```html
<root a="1" b="2">
    <child c="3" d="4">
        child 1 text
        <grandchild e="5" f="6">
            grandchild text
            <More>
            <More/>
        <grandchild/>
    <child/>
    root text
    root &lt;&gt;
    <child>
        child 2 text
    <child/>
<root/>
```

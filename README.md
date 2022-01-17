## pretty-doc


```python
from __future__ import annotations
from dataclasses import dataclass
import pretty_doc as doc
import json

@dataclass
class Block:
    name: str
    contents: list[Block] | str = ""

    def to_doc(self):
        return to_doc(self)

def to_doc(self: Block) -> doc.Doc:
    if isinstance(self.contents, list):
        return doc.vsep([
            doc.seg(self.name) + doc.seg("{"),
            doc.indent(4, doc.vsep(
                list(map(to_doc, self.contents)))),
            doc.seg("}")
        ])

    return doc.seg(self.name) + doc.seg(json.dumps(self.contents))

doc = Block(
    "A",
    [
        Block("C", "ccc"),
        Block("B",
            [
                Block("C", "ccc"),
            ]
        ),
        Block("C", "ccc"),
        Block("C", "ccc"),
    ]
).to_doc()

print(doc.show())
# out:
A {
    C "ccc"
    B {
        C "ccc"
    }
    C "ccc"
    C "ccc"
}

import sys
doc.render(sys.stdout.write)
# out:
A {
    C "ccc"
    B {
        C "ccc"
    }
    C "ccc"
    C "ccc"
}
```

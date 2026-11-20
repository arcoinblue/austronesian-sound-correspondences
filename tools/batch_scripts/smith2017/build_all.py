import sys
from lib import Batch
from sources import SOURCES
from common import add_general_decisions
import kayanic, melkaj, punmul, landdayak, malayic

b = Batch("smith2017-borneo")
b.sources.extend(SOURCES)
add_general_decisions(b)
for mod in (kayanic, melkaj, punmul, landdayak, malayic):
    mod.build(b)
    if mod is kayanic:
        kayanic.hold_intermediate(b)
out = b.write()
print(out, len(b.corrs), "rows,", len(b.lects), "lects")

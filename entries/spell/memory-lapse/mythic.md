+++
id = "ref/spell/memory-lapse/mythic"
kind = "rule"
title = "Memory Lapse, Mythic"
source_ids = ["mythic-adventures"]
relations = [
  { kind = "addon", target = "ref/spell/memory-lapse", label = "mythic" },
]

[fields]
kind = "none"
+++

**Sources:** Mythic Adventures pg 100\
The target forgets an additional round, back to the beginning of the turn before its last turn.

_Augmented (3rd):_ If you expend two uses of mythic power, you can spend 1 round implanting a false
memory in the affected target. This false memory is limited to events that could have occurred
during the time it just forgot, as if using [modify memory](ref/spell/modify-memory) but limited to
that short period of time. For example, you couldn't implant the memory of a lengthy conversation,
as that couldn't happen in the forgotten length of time.

The target can attempt a Will saving throw (DC equal to the mythic memory lapse DC plus your tier)
to resist this implanted memory. Success means no memory is implanted, but the target still forgets
the allotted time.

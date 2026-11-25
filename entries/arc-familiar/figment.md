+++
id = "ref/arc-familiar/figment"
kind = "archetype"
title = "Figment"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "figment", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "211"
[[sources]]
publication = "familiar-folio"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "recurring-dream" },
  { anchor = "manifest-dreams", level = 3 },
]
trades = [
  { replaces = "Improved evasion", by = ["recurring-dream"] },
  { replaces = "Deliver touch spells", by = ["manifest-dreams"] },
  { replaces = "speak with animals of its kind", by = ["manifest-dreams"] },
  { replaces = "scry on familiar", by = ["manifest-dreams"] },
]
+++

Figments are born from their masters' imaginations rather than being ordinary creatures that are
awakened.

## Recurring Dream (Su) {#recurring-dream}

A figment has a total number of hit points equal to 1/4 of its master's total hit points. If the
figment dies, it vanishes, appearing again with 1 hit point after its master awakens from a full
night's sleep. If a figment ever strays more than 100 feet from its master or enters an antimagic
field, or if a figment's master is unconscious or asleep, the figment disappears until the next time
its master prepares spells or regains her spells per day. Because it is a being of its master's
mind, a figment can never serve as a witch's familiar, a shaman's spirit animal, or any other
spell-granting familiar, and it can't use any divination spells or
[spell-like abilities](ref/umr/spell-like-abilities) the base creature has.

This replaces improved evasion.

## Manifest Dreams (Su) {#manifest-dreams}

At 3rd level, a figment is shaped by its master's dreams. Each time the master awakens from a full
night's rest, he can apply to the figment 1 evolution point's worth of eidolon evolutions that don't
have a base form requirement. At 7th level, he can apply 2 points' worth of eidolon evolutions; at
13th level, he can apply 3 points' worth of eidolon evolutions.

This replaces deliver touch spells, speak with animals of its kind, and scry on familiar.

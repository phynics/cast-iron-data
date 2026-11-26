+++
id = "ref/arc-antipaladin/fearmonger"
kind = "archetype"
title = "Fearmonger"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Fearmonger"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fearmonger", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "monster-codex"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "feed-on-fear", level = 2 },
  { anchor = "frightening-cruelty" },
]
trades = [
  { replaces = "Touch of corruption", feature = "touch-of-corruption", by = ["feed-on-fear"] },
  { alters = "Cruelty", feature = "cruelty", by = ["frightening-cruelty"] },
]
+++

The fearmonger wants to do more than cause pain, misery, and confusion. He wishes to spread fear
among his foes and infect entire populations with it. The fearmonger archetype is available only to
the antipaladin alternate class.

## Feed on Fear (Su) {#feed-on-fear}

At 2nd level, the first time in a round a creature fails a saving throw against a fear effect
created by a fearmonger's spell, [spell-like ability](ref/umr/spell-like-abilities), or supernatural
ability (including any ability that causes a creature to be shaken, frightened, or panicked), the
fearmonger is healed of 1 point of damage per 2 antipaladin levels. If the fearmonger is at full hit
points when this ability is activated, he instead gains an equal number of
[temporary hit points](ref/rule/temporary-hit-points). These temporary hit points last for 1 minute.
Temporary hit points gained through multiple successful uses of this ability do not stack; the
duration increases instead.

The antipaladin can use this ability a number of times per day equal to 1/2 his antipaladin level
plus his Charisma bonus. This ability replaces touch of corruption.

## Frightening Cruelty (Su) {#frightening-cruelty}

The fearmonger must select [shaken](ref/misc/shaken) as his 3rd-level cruelty,
[dazed](ref/misc/dazed) as his 6th-level cruelty, and [frightened](ref/misc/frightened) as his
9th-level cruelty. At 12th level, the fearmonger gains the panicked cruelty.

### Panicked {#panicked}

The target is [panicked](ref/misc/panicked) for 1 round per 4 class levels the antipaladin
possesses. The antipaladin must have the shaken and frightened cruelties before selecting this
cruelty.

This class feature alters cruelty.

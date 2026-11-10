+++
id = "ref/arc-summoner/spirit-summoner"
kind = "archetype"
title = "Spirit Summoner"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Spirit%20Summoner"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_summoner", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "advanced-class-guide"
page = "123"

[fields]
kind = "archetype"
replaces = ["Summon monster", "Aspect", "maker's call", "merge forms", "transposition"]
alters = ["Eidolon"]
+++

A spirit summoner is an arcane spellcaster whose eidolon is a manifestation of a shamanic spirit.
The bond connecting the summoner and this spirit might be friendly, as a member of a tribe giving
flesh to his protector spirit, or hostile, as an outlander or rival compelling service from an
unwilling spirit. The summoner can draw upon the divine power of this spirit, but is not constrained
by the spirit's morals or ethics.

**Spirit (Su)**

**Ability:** A spirit summoner forms a mystical bond with one [spirit](ref/ability/shaman-spirits)
from the shaman class. He gains the _spirit ability_ of that spirit and uses his summoner level as
his shaman level for determining its effects. The spirit summoner can select spells granted by that
spirit as summoner spells known, using the shaman level of the spell as the summoner spell level.
The summoner cannot select spirit spells that are above 6th level.

**At 17th Level:** The summoner gains the abilities listed for the _true_ version of his selected
spirit.

**At 9th Level:** The summoner gains the abilities listed in the _greater_ version of his selected
spirit.

**Replaces:** Summon monster

**Eidolon**

**Alters:** Eidolon

**Info:** A spirit summoner begins play with a powerful outsider called an eidolon. The eidolon's
form and abilities must be appropriate to his chosen spirit, at the GM's discretion - for example, a
summoner with the [flame](ref/shamanspirit/flame) spirit cannot have an eidolon with ice or water
abilities, a summoner with a [heavens](ref/shamanspirit/heavens) spirit cannot have a fiend-like
eidolon, and so on. The summoner can use temporary effects (such as
_[evolution surge](ref/spell/evolution-surge)_) to alter the eidolon into an inappropriate form, but
cannot use permanent effects (such as _[transmogrify](ref/spell/transmogrify)_) to do so.

**Gained:** At 1st Level

**Hex**

**Ability:** A spirit summoner can select a shaman hex that is appropriate to his spirit, chosen
from the general list of shaman hexes or the specific hexes allowed by his spirit. This otherwise
functions as a shaman's hex, and uses his summoner level as his shaman level. Like a shaman, a
spirit summoner uses his Wisdom modifier to determine hex DCs.

**Gained:** At 6th Level

**Repeat At:** The summoner can select another hex., 8, 10, 16

**Replaces:** Aspect, maker's call, merge forms, transposition

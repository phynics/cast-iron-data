+++
id = "ref/arc-cavalier/strategist"
kind = "archetype"
title = "Strategist"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Strategist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "strategist", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-combat"
page = "39"

[fields]
kind = "archetype"
replaces = ["Expert trainer", "Greater banner", "The cavalier's 18th-level bonus feat"]
alters = ["Tactician"]
replaces_features = ["expert-trainer", "greater-banner"]
alters_features = ["tactician"]
+++

Some cavaliers make a lifelong mission out of their exceptional ability to direct troops on the
battlefield, combining tactical insight with a preternatural skill at improving the teamwork of
their allies in order to win the day. Such strategists are masters at learning the strengths and
weaknesses of those they fight alongside, and at employing those observations at the most opportune
moments. The best of them are also skilled at determining the strengths and weaknesses of their
enemies, as well as at countering some of those strengths with their own formidable abilities.

**Tactician (Ex)**

**Ability:** As the cavalier class feature, except that a strategist can use this ability once per
day, plus one additional time for every four levels after 1st (to a maximum of five times per day at
17th level).

**Alters:** Tactician

**Gained:** At 1st Level

**Drill Instructor (Ex)**

**Ability:** A strategist learns to train his fellow adventurers in the nuances of squad combat. By
spending 10 minutes and expending 1 use of his _challenge_ ability, the strategist can grant the use
of a teamwork feat that he knows to up to four of his allies, similar to the _tactician_ ability. As
with _tactician,_ allies need not meet the prerequisites of the granted feat, but they retain the
use of this feat for 10 minutes plus an additional number of minutes equal to
[half](ref/misc/fractions-and-rounding) of his cavalier level, as long as the cavalier is visible
and can be heard by his allies.

**Gained:** At 4th Level

**Replaces:** Expert trainer

**Special:** If the cavalier falls unconscious or cannot be both seen and heard, his allies lose the
benefit of the granted feat until the condition is remedied.

**Tactical Advantage (Ex)**

**Free:** Whenever a strategist uses his _tactician_ ability to grant the use of a teamwork feat to
his allies, he can move up to his speed either before or after granting the feat. This movement
provokes attacks of opportunity normally.

**Gained:** At 14th Level

**Replaces:** Greater banner

**Strategic Supremacy (Ex)**

**Ability:** A strategist gains the ability not only to improve his allies' abilities, but also to
disrupt the teamwork of his enemies. Whenever the strategist uses the _tactician_ ability, he can
choose to cancel out the effects of one teamwork feat employed by any of his opponents within 30
feet instead of granting the use of a teamwork feat to his allies.

**Gained:** At 18th Level

**Replaces:** The cavalier's 18th-level bonus feat

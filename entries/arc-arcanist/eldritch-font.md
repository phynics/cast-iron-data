+++
id = "ref/arc-arcanist/eldritch-font"
kind = "archetype"
title = "Eldritch Font"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20Eldritch%20Font"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_font", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "77"

[fields]
kind = "archetype"
replaces = ["The arcanist exploit gained at 3rd level", "The arcanist exploit gained at 7th level", "The arcanist exploit gained at 13th level", "Magical supremacy"]
replaces_features = ["magical-supremacy"]
+++

For some arcanists, the power bubbling up from within is nearly too much to contain. They become
adept at shaping this magical energy without needing to bind it up in spells.

**Font of Power**

**Passive:** An eldritch font gains one additional spell slot for each level of arcanist spell she
can cast. However, the number of spells of each level that she can prepare reduces by 1. If this
reduces her spells prepared for a level to 0, she still gains spell slots of that level, which can
be consumed using the _consume spells_ class feature to fuel her _arcane reservoir_ or cast spells
using metamagic feats.

**Eldritch Surge (Su)**

**Gained:** At 3rd Level

**Replaces:** The arcanist exploit gained at 3rd level

**Special:** This ability does not stack with spending points from her arcane reservoir to increase
the spell's caster level or DC (as the _arcane reservoir_ class feature). Only rest can remove
fatigue or exhaustion caused by an eldritch surge - spells and abilities have no effect.

**Swift:** An eldritch font can pour more power into her spells and abilities. She can add 2 to the
caster level and DC of a spell, or increase her effective arcanist level by 2 when using an arcanist
exploit. She becomes [fatigued](ref/misc/fatigued) upon using this ability. If she is already
fatigued, she becomes [exhausted](ref/misc/exhausted). If she's already exhausted, or something
would prevent her from becoming fatigued or exhausted, she cannot use this ability.

**Improved Surge (Su)**

**Ability:** An eldritch font can use her _eldritch surge_ ability to reroll an attack roll
associated with a spell or arcanist exploit, or to reroll all of the damage dice associated with a
spell or arcanist exploit. In the case of attack rolls, this ability must be used after the die is
rolled but before the results are revealed. The eldritch font must take the results of the reroll,
even if they are lower.

**Gained:** At 7th Level

**Replaces:** The arcanist exploit gained at 7th level

**Greater Surge (Su)**

**Ability:** An eldritch font can use her _eldritch surge_ ability to force a creature to reroll a
saving throw against one spell or arcanist exploit and take the lower value. The eldritch font must
declare the use of this ability before the result of that creature's saving throw is revealed. If
the spell or arcanist exploit affects more than one target, only one target is affected by this
ability.

**Gained:** At 13th Level

**Replaces:** The arcanist exploit gained at 13th level

**Bottomless Well**

**Ability:** An eldritch font can spend 1 hour studying her spellbook to refuel herself. Doing so
allows her to prepare new spells and regain points of arcane reservoir equal to
[half](ref/misc/fractions-and-rounding) her level. She can use this ability multiple times per day,
however she still only regains spell slots once per day.

**Gained:** At 20th Level

**Replaces:** Magical supremacy

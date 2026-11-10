+++
id = "ref/arc-wizard/clocksmith"
kind = "archetype"
title = "Clocksmith"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Clocksmith"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "clocksmith", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "construct-handbook"
page = "10"

[fields]
kind = "archetype"
replaces = ["School powers granted by the wizard's arcane school", "Scribe Scroll", "5th-, 10th-, 15th-, and 20th-level bonus feats"]
alters = ["Arcane bond"]
+++

Clocksmiths are oddities among wizard communities, pursuing the study and creation of clockwork
constructs to near obsession. These wizards favor mechanical experiments over other arcane pursuits.

**Clockwork Bond (Ex)**

**Ability:** A clocksmith forms a bond with one of his clockwork creations and begins play with a
constructed familiar. He must select this familiar as his _arcane bond._ The constructed familiar
functions as a typical familiar of its type except as noted here. The construct familiar is always a
construct with the [clockwork](ref/subtype/clockwork) subtype. A construct familiar grants only half
of its typical bonus (minimum +1 bonus) from its special familiar ability to its master.

**Alters:** Arcane bond

**Clockwork Expertise (Ex)**

**At 8th Level:** The bonus to saves becomes +4 and he treats his caster level as 2 higher when
affecting clockwork creatures.

**Passive:** A clocksmith is especially adept at dealing with clockworks. He gains a +2 bonus on
saving throws against effects created by creatures of the clockwork subtype. Additionally, he treats
his caster level as 1 higher when casting a spell that affects or targets only creatures of the
clockwork subtype.

**Replaces:** School powers granted by the wizard's arcane school

**Craft Construct**

**Ability:** A clocksmith gains [Craft Construct](ref/feat/craft-construct) as a bonus feat, even if
he does not meet the prerequisites. He can create any construct, but he increases the cost required
to create constructs without the clockwork subtype by 50%.

**Replaces:** Scribe Scroll

**Familiar Tinkering (Ex)**

**Ability:** A clocksmith learns to improve upon his clockwork familiar. A clocksmith can grant his
familiar an amount of evolution points equal to [one-fifth](ref/misc/fractions-and-rounding) of his
wizard level. He can use these points to grant his familar eidolon evolutions, though he can't
select any evolutions that require a specific base form.

**Gained:** At 5th Level

**Replaces:** 5th-, 10th-, 15th-, and 20th-level bonus feats

**Special:** Each time the clocksmith gains a level, he can change his familiar's evolutions. These
evolutions stack with those from the [Evolved Familiar](ref/feat/evolved-familiar) feat.

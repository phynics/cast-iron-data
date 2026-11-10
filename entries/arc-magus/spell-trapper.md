+++
id = "ref/arc-magus/spell-trapper"
kind = "archetype"
title = "Spell Trapper"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Spell%20Trapper"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_trapper", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "15"

[fields]
kind = "archetype"
replaces = ["Spell recall", "Fighter training"]
alters = ["Magus arcana"]
+++

Spell trappers are found in lands where hunting and magic are abundant, particularly the deserts of
Thuvia and the harsh lands of Geb and Nex. They forsake much of their arcane skill and martial
knowledge in exchange for the ability to conjure magical traps to hinder their foes.

**Gained class skills:** dd

**Lost class skills:** kp

**Diminished Arcana**

**Alters:** Magus arcana

**Info:** A spell trapper treats his effective magus level as 3 lower when determining which arcana
he can select. A spell trapper can choose to learn a new trap (see _Spell Traps_ below) in place of
learning a new magus arcana.

**Spell Traps (Sp)**

**Ability:** A spell trapper learns how to craft magical traps in exchange for the use of spell
slots. These [traps](ref/rule/traps) work as ranger traps, except they always count as
[spell-like abilities](ref/umr/spell-like-abilities). A spell trap is always considered magical, and
is treated as a spell with a spell level equal to 1/3 the spell trapper's class level. A magical
trap lasts only 1 hour per level or until triggered, whichever comes first. A trap's DC decreases by
1 for each full hour that passes after it is set. Upon gaining this ability, the spell trapper
automatically knows the [snare trap](ref/rangertrap/snare-trap).

**Gained:** At 4th Level

**Replaces:** Spell recall

**Special:** Setting a spell trap is a **full-round action** that provokes attacks of opportunity.
If attacked during the course of conjuring a trap, the spell trapper must attempt a
[concentration](ref/rule/concentration) check, as though damaged while casting a spell. A trap fills
a single 5-foot square, and cannot be placed in the same area as another spell trapper trap or a
magical trap such as a [glyph of warding](ref/spell/glyph-of-warding). Spell trappers need access to
a material component pouch to craft spell traps (unless they have the
[Eschew Materials](ref/feat/eschew-materials) feat) and must sacrifice a spell slot to create the
trap. The DCs for Perception checks to notice the trap, Disable Device checks to disable it, and
saving throws to avoid it are equal to 10 + 1/2 the spell trapper's magus level + the spell slot
level sacrificed to create the trap. All spell traps are [Trigger](ref/rule/trigger) location, and
[Reset](ref/rule/reset) none.

**Distant Trapping (Sp)**

**Ability:** She can create her traps at close range (25 feet + 5 feet per 2 caster levels) as a
**full-round action** that provokes attacks of opportunity.

**Flavor:** A spell trapper can create spell traps at a distance.

**Gained:** At 10th Level

**Replaces:** Fighter training

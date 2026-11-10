+++
id = "ref/arc-magus/iron-ring-striker"
kind = "archetype"
title = "Iron-Ring Striker"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Iron-Ring%20Striker"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iron_ring_striker", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "5"

[fields]
kind = "archetype"
replaces = ["Medium armor", "heavy armor", "Knowledge pool", "Counterstrike"]
alters = ["Weapon proficiency", "Spellcasting", "Arcane pool", "Spellstrike", "5th-level bonus feat"]
replaces_features = ["medium-armor", "heavy-armor", "knowledge-pool", "counterstrike"]
alters_features = ["arcane-pool", "spellstrike"]
+++

Practitioners of this martial art, powered by arcane magic, wear an iron ring on the finger of one
hand. This legacy has been handed down from the tradition's Vudrani founders.

**Weapon Proficiency**

**Alters:** Weapon proficiency

**Info:** An iron-ring striker is not proficient with martial weapons.

**Diminished Spellcasting**

**Ability:** An iron-ring striker has one fewer spell slot of each level than a regular magus. If
this reduces his number of spell slots of a particular level to 0, he can cast spells of that level
only if his Intelligence allows [bonus spells](ref/rule/determine-bonuses) of that level.

**Alters:** Spellcasting

**Arcane Pool (Su)**

**Ability:** An iron-ring striker can use his _arcane pool_ to enhance his unarmed strikes as if
they were manufactured weapons.

**Alters:** Arcane pool

**At 5th Level:** He can use these bonuses to add any of the following weapon special abilities to
his weapons or unarmed strikes: [advancing](ref/magic-enh/advancing), [cruel](ref/magic-enh/cruel),
[defending](ref/magic-enh/defending), [guardian](ref/magic-enh/guardian),
[impact](ref/magic-enh/impact), [invigorating](ref/magic-enh/invigorating),
[mimetic](ref/magic-enh/mimetic), [negating](ref/magic-enh/negating), [speed](ref/magic-enh/speed),
and [vicious](ref/magic-enh/vicious).

**Unarmed Spellstrike (Su)**

**Ability:** An iron-ring striker gains the magus _spellstrike_ class feature. However, an iron-ring
striker can deliver spells with _spellstrike_ with only unarmed strikes.

**Alters:** Spellstrike

**Unarmed Strike**

**Ability:** An iron-ring striker gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike)
as a bonus feat. He deals unarmed strike damage as per a [monk](ref/class/monk) of his level. For
the purpose of determining damage, these levels stack with levels from any other class that grants
increased damage to unarmed strikes.

**Unarmed Strike**

**Flavor:** Relevant text from the monk class ability.

**At 12th Level:** Your unarmed strike now deals 1d10 (Small), 2d6 (Medium), or 3d6 (Large) damage.

**At 16th Level:** Your unarmed strike now deals 2d6 (Small), 2d8 (Medium), or 3d8 (Large) damage.

**At 20th Level:** Your unarmed strike now deals 2d8 (Small), 2d10 (Medium), or 4d8 (Large) damage.

**At 4th Level:** Your unarmed strike now deals 1d6 (Small), 1d8 (Medium), or 2d6 (Large) damage.

**At 8th Level:** Your unarmed strike now deals 1d8 (Small), 1d10 (Medium), or 2d8 (Large) damage.

**At 1st Level:** Your unarmed strike deals 1d4 (Small), 1d6 (Medium), or 1d8 (Large) damage.

**Bonus Feat**

**Ability:** An iron-ring striker must select his bonus feat from this list:
[Improved Bull Rush](ref/feat/improved-bull-rush), [Improved Disarm](ref/feat/improved-disarm),
[Improved Sunder](ref/feat/improved-sunder), or [Improved Trip](ref/feat/improved-trip). He doesn't
need to meet the prerequisites normally required for these feats.

**Alters:** 5th-level bonus feat

**Gained:** At 5th Level

**Empower Combat (Su)**

**Flavor:** An iron-ring striker learns to use magic to grant himself the power of a larger
creature.

**Gained:** At 7th Level

**Replaces:** Medium armor, heavy armor

**Standard:** He can expend one non-cantrip prepared magus spell to treat his size as if it were
larger for the purposes of determining the
[size modifier to his CMB and CMD](ref/rule/combat-maneuvers), as well as which creatures he can
affect with combat maneuvers. For every level of the spell he sacrifices, his effective size
increases by one step, up to a maximum of Colossal. For every two effective size increments he
increases, he gains a +2 size bonus to Strength, to a maximum of +6. This does not change the
iron-ring striker's actual size. This effect lasts for 1 minute per level of the spell sacrificed.

**Spell Maneuvers (Su)**

**Ability:** As long as an iron-ring striker is wearing light armor or no armor, he can use his
_unarmed spellstrike_ ability as part of a combat maneuver check to [bull rush](ref/rule/bull-rush),
[disarm](ref/rule/disarm), [sunder](ref/rule/sunder), or [trip](ref/rule/trip) an opponent.

**Gained:** At 7th Level

**Replaces:** Knowledge pool

**Reflexive Spell Maneuver (Ex)**

**Immediate:** When an iron-ring striker is the target of a combat maneuver check to bull rush,
disarm, sunder, or trip, he can target his attacker with a magus spell he has prepared with a range
of touch. If the spell would normally require a touch attack, an iron-ring striker can attempt a
combat maneuver check for this attack instead.

**Gained:** At 16th Level

**Replaces:** Counterstrike

**Special:** The iron-ring striker must be wearing light armor or no armor to use reflexive spell
maneuver.

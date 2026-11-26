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
features = [
  { anchor = "diminished-spellcasting", level = 1 },
  { anchor = "arcane-pool", level = 1 },
  { anchor = "unarmed-spellstrike" },
  { anchor = "unarmed-strike" },
  { anchor = "bonus-feat", level = 5 },
  { anchor = "empower-combat", level = 7 },
  { anchor = "spell-maneuvers", level = 7 },
  { anchor = "reflexive-spell-maneuver", level = 16 },
]
trades = [
  { replaces = "Medium armor", feature = "medium-armor", by = ["empower-combat"] },
  { replaces = "heavy armor", feature = "heavy-armor", by = ["empower-combat"] },
  { replaces = "Knowledge pool", feature = "knowledge-pool", by = ["spell-maneuvers"] },
  { replaces = "Counterstrike", feature = "counterstrike", by = ["reflexive-spell-maneuver"] },
  { alters = "Weapon proficiency", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { alters = "Spellcasting", feature = "spells", by = ["diminished-spellcasting"] },
  { alters = "Arcane pool", feature = "arcane-pool", by = ["arcane-pool"] },
  { alters = "Spellstrike", feature = "spellstrike", by = ["unarmed-spellstrike"] },
  { alters = "Bonus feat gained at 5th level", feature = "bonus-feats", levels = [5], by = ["bonus-feat"] },
]
+++

Practitioners of this martial art, powered by arcane magic, wear an iron ring on the finger of one
hand. This legacy has been handed down from the tradition's Vudrani founders.

## Weapon Proficiency {#weapon-proficiency}

An iron-ring striker is not proficient with martial weapons.

This alters the magus's weapon proficiency.

## Diminished Spellcasting {#diminished-spellcasting}

An iron-ring striker has one fewer spell slot of each level than a regular magus. If this reduces
his number of spell slots of a particular level to 0, he can cast spells of that level only if his
Intelligence allows [bonus spells](ref/rule/determine-bonuses) of that level.

This alters the magus's spellcasting.

## Arcane Pool (Su) {#arcane-pool}

An iron-ring striker can use his arcane pool to enhance his unarmed strikes as if they were
manufactured weapons. At 5th level, he can use these bonuses to add any of the following weapon
special abilities to his weapons or unarmed strikes: _[advancing](ref/magic-enh/advancing)_,
_[cruel](ref/magic-enh/cruel)_, _[defending](ref/magic-enh/defending)_,
_[guardian](ref/magic-enh/guardian)_, _[impact](ref/magic-enh/impact)_,
_[invigorating](ref/magic-enh/invigorating)_, _[mimetic](ref/magic-enh/mimetic)_,
_[negating](ref/magic-enh/negating)_, _[speed](ref/magic-enh/speed)_, and
_[vicious](ref/magic-enh/vicious)_.

This alters arcane pool.

## Unarmed Spellstrike (Su) {#unarmed-spellstrike}

An iron-ring striker gains the magus spellstrike class feature. However, an iron-ring striker can
deliver spells with spellstrike with only unarmed strikes.

This alters spellstrike.

## Unarmed Strike {#unarmed-strike}

An iron-ring striker gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus
feat. He deals unarmed strike damage as per a [monk](ref/class/monk) of his level. For the purpose
of determining damage, these levels stack with levels from any other class that grants increased
damage to unarmed strikes.

## Bonus Feat {#bonus-feat}

At 5th level, an iron-ring striker must select his bonus feat from this list:
[Improved Bull Rush](ref/feat/improved-bull-rush), [Improved Disarm](ref/feat/improved-disarm),
[Improved Sunder](ref/feat/improved-sunder), or [Improved Trip](ref/feat/improved-trip). He doesn't
need to meet the prerequisites normally required for these feats.

This modifies the bonus feat gained at 5th level.

## Empower Combat (Su) {#empower-combat}

At 7th level, an iron-ring striker learns to use magic to grant himself the power of a larger
creature. As a standard action, he can expend one non-cantrip prepared magus spell to treat his size
as if it were larger for the purposes of determining the
[size modifier to his CMB and CMD](ref/rule/combat-maneuvers), as well as which creatures he can
affect with combat maneuvers. For every level of the spell he sacrifices, his effective size
increases by one step, up to a maximum of Colossal. For every two effective size increments he
increases, he gains a +2 size bonus to Strength, to a maximum of +6. This does not change the
iron-ring striker's actual size. This effect lasts for 1 minute per level of the spell sacrificed.

This replaces medium armor and heavy armor.

## Spell Maneuvers (Su) {#spell-maneuvers}

At 7th level, as long as an iron-ring striker is wearing light armor or no armor, he can use his
unarmed spellstrike ability as part of a combat maneuver check to [bull rush](ref/rule/bull-rush),
[disarm](ref/rule/disarm), [sunder](ref/rule/sunder), or [trip](ref/rule/trip) an opponent.

This replaces knowledge pool.

## Reflexive Spell Maneuver (Ex) {#reflexive-spell-maneuver}

At 16th level, when an iron-ring striker is the target of a combat maneuver check to bull rush,
disarm, sunder, or trip, as an immediate action he can target his attacker with a magus spell he has
prepared with a range of touch. If the spell would normally require a touch attack, an iron-ring
striker can attempt a combat maneuver check for this attack instead. The iron-ring striker must be
wearing light armor or no armor to use reflexive spell maneuver.

This replaces counterstrike.

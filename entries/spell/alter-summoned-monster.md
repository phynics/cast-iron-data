+++
id = "ref/spell/alter-summoned-monster"
kind = "spell"
title = "Alter Summoned Monster"
aon = "SpellDisplay.aspx?ItemName=Alter%20Summoned%20Monster"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alter_summoned_monster", path = "json/spells.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "22"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one summoned creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Antipaladin, Arcanist, Bard, Cleric, Druid, Hunter, Oracle, Ranger, Skald, Sorcerer, Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one summoned creature
Subschool: Summoning
:::

You swap a creature summoned by a conjuration (summoning) spell for a creature you could summon with
a [summon monster](ref/spell/summon-monster) or
[summon nature's ally](ref/spell/summon-natures-ally) spell. The new creature must be an option from
a spell of the same level or lower as the spell that summoned the target. The new creature cannot be
summoned into an environment that cannot support it. The target can attempt a Will saving throw to
negate this effect, but if the target is under your control, it receives no saving throw. Alter
summoned monster does not alter the duration of the spell that summoned the target, nor does it
affect any additional creatures summoned by the same spell as the target. The new creature has the
same conditions and amount of damage as the target creature, and remains affected by all curses,
diseases, poisons, and penalties that affected the target, but no other spells or effects carry
over. Alter summoned monster is a spell of the same alignment type or types as the creature for
which you exchange the target. An eidolon can't be targeted by this spell.

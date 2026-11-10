+++
id = "ref/spell/scamper"
kind = "spell"
title = "Scamper"
aon = "SpellDisplay.aspx?ItemName=Scamper"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scamper", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "234"
[[sources]]
publication = "animal-archive"
page = "25"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 swift action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "your animal companion" },
]
duration = "1 round; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Ranger
Casting time: 1 swift action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round; see text
Saving throw: none
Spell resistance: no
Target: your animal companion
:::

Your animal companion moves with astonishing agility and speed until the end of its turn. It can
move at full speed while using Acrobatics, and it gains a competence bonus equal to twice your
caster level (maximum +20 at 10th level) on Acrobatics checks to avoid attacks of opportunity or
move through a square occupied by an enemy.

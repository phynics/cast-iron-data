+++
id = "ref/spell/earsend"
kind = "spell"
title = "Earsend"
aon = "SpellDisplay.aspx?ItemName=Earsend"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "earsend", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/skinsend" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "25"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (butterfly wing)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Alchemist, Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (butterfly wing)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

You cause one of your ears to tear itself free of your body and transform into a fly-like magical
creature you control. This functions like [skinsend](ref/spell/skinsend), except your ear is a Fine
construct with a fly speed equal to your base speed and a bonus on Fly checks equal to half your
caster level. Your sense of hearing functions from your animated ear as if it were connected to your
head, allowing you to hear as well as you normally could from your animated ear's vantage point.

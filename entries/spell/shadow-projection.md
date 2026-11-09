+++
id = "ref/spell/shadow-projection"
kind = "spell"
title = "Shadow Projection"
aon = "SpellDisplay.aspx?ItemName=Shadow%20Projection"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_projection", path = "json/spells15.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "243"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Sorcerer, Wizard
Casting time: 1 minute
Components: S
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: evil
:::

With this spell, you infuse your life force and psyche into your shadow, giving it independent life
and movement as if it were an undead [shadow](ref/monster/shadow). Your physical body lies comatose
while you are projecting your shadow, and your body has no shadow or reflection while the spell is
in effect.

While projecting your shadow, you gain a shadow's [darkvision](ref/rule/darkvision), defensive
abilities, fly speed, racial stealth modifier, and strength damage attack. You do not gain the
creature's create spawn ability, nor its skill ranks or Hit Dice. Your shadow has Hit Dice and hit
points equal to your own. Your shadow projection has the undead type and may be turned or affected
as undead.

If your shadow projection is slain, you return to your physical body and are immediately reduced to
-1 hit points. Your condition becomes dying, and you must begin making Constitution checks to
stabilize.

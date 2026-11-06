+++
id = "ref/spell/fools-teleport"
kind = "spell"
title = "Fool's Teleport"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fools_teleport", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "personal and touch"
effects = [
  { label = "Target", value = "you and other touched willing creatures" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless), see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: personal and touch
Duration: 1 minute/level
Saving throw: Will negates (harmless), see text
Spell resistance: no
Target: you and other touched willing creatures
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Occult Origins pg 13

This spell instantly renders you unseen as per invisibility, but creates a visual and auditory
display that makes it appear as if you had teleported away. You can affect one additional Medium or
smaller creature or its equivalent per 3 caster levels (a Large creature counts as two Medium
creatures, a Huge creature counts as four Medium creatures, and so forth). All creatures to be
affected must be in contact with one another, and at least one of those creatures must be in contact
with you.

If a viewer identifies the spell with a successful Spellcraft check, she can attempt an immediate
Will saving throw as if interacting with an illusion. With a successful Will save, the observer can
correctly identify fool's teleport for what it is; otherwise, she perceives the spell to be
dimension door, teleport, or similar conjuration magic. A successful Will save doesn't negate the
invisibility.

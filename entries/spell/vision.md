+++
id = "ref/spell/vision"
kind = "spell"
title = "Vision"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vision", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (incense worth 250 gp), F (four pieces of ivory worth 50 gp each)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 7: Arcanist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (incense worth 250 gp), F (four pieces of ivory worth 50 gp each)
Range: personal
Duration: see text
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** PRPG Core Rulebook pg 365

This spell functions like legend lore, except that it works more quickly and produces some strain on
you. You pose a question about some person, place, or object, then cast the spell. If the person or
object is at hand or if you are in the place in question, you receive a vision about it by
succeeding on a caster level check (1d20 + 1 per caster level; maximum +25) against DC 20. If only
detailed information on the person, place, or object is known, the DC is 25, and the information
gained is incomplete. If only rumors are known, the DC is 30, and the information gained is vague.
After this spell is complete, you are fatigued.

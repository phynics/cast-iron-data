+++
id = "ref/spell/detect-scrying"
kind = "spell"
title = "Detect Scrying"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_scrying", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of mirror and a miniature brass hearing trumpet)"
range = "40 ft."
effects = [
  { label = "Area", value = "40-ft.-radius emanation centered on you" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium\
4: Arcanist, Bard, Inquisitor, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of mirror and a miniature brass hearing trumpet)
Range: 40 ft.
Duration: 24 hours
Saving throw: none
Spell resistance: no
Area: 40-ft.-radius emanation centered on you
:::

**Sources:** PRPG Core Rulebook pg 268

You immediately become aware of any attempt to observe you by means of a divination (scrying) spell
or effect. The spell's area radiates from you and moves as you move. You know the location of every
magical sensor within the spell's area.

If the scrying attempt originates within the area, you also know its location; otherwise, you and
the scrier immediately make opposed caster level checks (1d20 + caster level). If you at least match
the scrier's result, you get a visual image of the scrier and an accurate sense of his direction and
distance from you.

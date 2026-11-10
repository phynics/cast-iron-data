+++
id = "ref/spell/psychic-crush-5"
kind = "spell"
title = "Psychic Crush V"
aon = "SpellDisplay.aspx?ItemName=Psychic%20Crush%20V"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_crush_5", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/psychic-crush-4" },
]
[[sources]]
publication = "occult-adventures"
page = "183"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 5 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will partial and Fortitude partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will partial and Fortitude partial, see text
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

### Psychic Crush V

This functions as [psychic crush IV](ref/spell/psychic-crush-4), but on a successful Fortitude or
Will save, the target takes 11d6 points of damage + 1 point of damage per caster level. If it is at
fewer than half its total hit points, the target takes a -2 penalty on the Will save to resist this
spell. This spell can be undercast.

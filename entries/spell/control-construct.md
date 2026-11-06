+++
id = "ref/spell/control-construct"
kind = "spell"
title = "Control Construct"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "control_construct", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Occultist", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one construct" },
]
duration = "concentration"
saving_throw = "none (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Occultist\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration
Saving throw: none (see text)
Spell resistance: no
Target: one construct
:::

**Sources:** Ultimate Magic pg 211

You wrest the control of a construct from its master. For as long as you concentrate, you can
control the construct as if you were its master. You must make a Spellcraft check each round to
maintain control. The DC of the Spellcraft check is (10 + the construct's HD). If the construct's
creator or master is present and trying to control the construct, you both must make opposed
Spellcraft checks each round to control the construct.

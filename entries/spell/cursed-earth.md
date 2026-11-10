+++
id = "ref/spell/cursed-earth"
kind = "spell"
title = "Cursed Earth"
aon = "SpellDisplay.aspx?ItemName=Cursed%20Earth"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cursed_earth", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "215"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "evil"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (powdered onyx 10,000 gp)"
range = "touch"
effects = [
  { label = "Area", value = "1-mile radius emanating from the touched point" },
]
duration = "permanent"
saving_throw = "none (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, DF, M (powdered onyx 10,000 gp)
Range: touch
Duration: permanent
Saving throw: none (see text)
Spell resistance: no
Area: 1-mile radius emanating from the touched point
Descriptors: curse, evil
:::

You lay a terrible curse upon the land, blighting those who live and die there. Choose one of the
following effects.

_Famine:_ All normal plants in the area reduce their growth and food production by half, as if
affected by the stunt growth effect of diminish plants.

_Living Death:_ Any creatures of Small size or larger killed in the area rise as uncontrolled
zombies 24 hours after their death, as do corpses buried in the area. Burning or dismembering the
corpses prevents them from rising as zombies.

_Plague:_ Every day at sundown, all creatures in the area must make a Fortitude save or catch one of
the following diseases (your choice, decided at the time of casting): blinding sickness, bubonic
plague, cackle fever, filth fever, leprosy, mindfire, red ache, shakes, or slimy doom. The disease
is contracted immediately (the onset period does not apply). Use the disease's listed frequency and
save DC to determine further effects. This is a disease effect.

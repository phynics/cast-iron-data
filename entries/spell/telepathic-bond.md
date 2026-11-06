+++
id = "ref/spell/telepathic-bond"
kind = "spell"
title = "Telepathic Bond"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telepathic_bond", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (two eggshells from two different creatures)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "you plus one willing creature per three levels, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Medium, Mesmerist, Psychic\
5: Arcanist, Inquisitor, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (two eggshells from two different creatures)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Targets: you plus one willing creature per three levels, no two of which can be more than 30 ft. apart
:::

**Sources:** PRPG Core Rulebook pg 358

You forge a telepathic bond among yourself and a number of willing creatures, each of which must
have an Intelligence score of 3 or higher. Each creature included in the link is linked to all the
others. The creatures can communicate telepathically through the bond regardless of language. No
special power or influence is established as a result of the bond. Once the bond is formed, it works
over any distance (although not from one plane to another).

If desired, you may leave yourself out of the telepathic bond forged. This decision must be made at
the time of casting.

Telepathic bond can be made permanent with a [permanency](ref/spell/permanency) spell, though it
only bonds two creatures per casting of permanency.

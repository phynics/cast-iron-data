+++
id = "ref/spell/charnel-house"
kind = "spell"
title = "Charnel House"
aon = "SpellDisplay.aspx?ItemName=Charnel%20House"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charnel_house", path = "json/spells2.json" },
]
[[sources]]
publication = "horror-adventures"
page = "111"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["evil", "shadow"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M (one Tiny or larger living creature)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft. cube (S)" },
]
duration = "10 minutes/level"
saving_throw = "Will partial"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Antipaladin\
5: Arcanist, Cleric, Mesmerist, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (one Tiny or larger living creature)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will partial
Spell resistance: no
Area: 20-ft. cube (S)
Subschool: Shadow
Descriptors: evil, shadow
:::

By sacrificing a living creature, you create the grisly illusion of viscera and gore splattered
about the nearby area. When the casting time is complete, the walls drip with blood and the floor is
slick with unidentifiable lumps of meat and other signs of a massacre. Anyone entering the area must
attempt a Will save or be sickened for 1d6 rounds. This is a mind-affecting effect. If a creature
succeeds at its save, it can see the semi-real nature of the illusion.

The room itself is covered in a layer of slippery, semi-real gore. Any creature attempting to walk
within or through the area of gore can move at half normal speed with a DC 10 Acrobatics check.
Failure means it can't move that round, and failure by 5 or more means it falls prone (see the
[Acrobatics](ref/skill/acrobatics) skill for details). Creatures that don't move on their turns
don't need to attempt this check and are not considered flat-footed. A creature that succeeded at
its Will save gains a +5 bonus on the Acrobatics check.

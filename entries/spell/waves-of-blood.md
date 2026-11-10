+++
id = "ref/spell/waves-of-blood"
kind = "spell"
title = "Waves of Blood"
aon = "SpellDisplay.aspx?ItemName=Waves%20of%20Blood"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "waves_of_blood", path = "json/spells11.json" },
]
[[sources]]
publication = "horror-adventures"
page = "130"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of the caster's blood)"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous and 1 round; see text"
saving_throw = "Reflex negates, Fortitude negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bloodrager, Magus, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of the caster's blood)
Range: 30 ft.
Duration: instantaneous and 1 round; see text
Saving throw: Reflex negates, Fortitude negates (see text)
Spell resistance: no
Area: cone-shaped burst
Subschool: Creation
:::

You cause torrents of roiling blood to push your opponents away from you. This wave attempts a bull
rush combat maneuver against all creatures within its area of effect, and you bull rush creatures of
any size in this way. Attempt a single combat maneuver check and apply the result to each creature
within the area. Your CMB for this bull rush is equal to your caster level plus your Intelligence,
Wisdom, or Charisma modifier, whichever is highest. This bull rush doesn't provoke attacks of
opportunity. Any creature in the area must also succeed at a Fortitude saving throw or become
sickened for 1d6 rounds by the tide of blood.

The area covered by the cone remains slick for 1 round, requiring a successful DC 10 Acrobatics
check from any creature attempting to move within it (as if moving on uneven ground). Any creature
that falls prone due to failing the check must Succeed at a Fortitude save or become sickened until
it stands back up.

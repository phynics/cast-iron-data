+++
id = "ref/spell/shadow-invasion"
kind = "spell"
title = "Shadow Invasion"
aon = "SpellDisplay.aspx?ItemName=Shadow%20Invasion"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_invasion", path = "json/spells15.json" },
]
[[sources]]
publication = "planar-adventures"
page = "44"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (a masterwork piercing or slashing weapon)"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft. radius emanation centered on you" },
]
duration = "1 round/level (d); see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Magus, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F (a masterwork piercing or slashing weapon)
Range: 30 ft.
Duration: 1 round/level (d); see text
Saving throw: none
Spell resistance: no
Area: 30-ft. radius emanation centered on you
Subschool: Summoning
:::

Using a slashing motion with the spell's focus as part of the casting of shadow invasion, you cut
open a rift to the Plane of Shadow that fills a 30-foot area with shadowy energies. This area is
stationary and becomes dark and gloomy, reducing the light level by one step (as darkness). Certain
spells are enhanced within the area; spells of the shadow subschool that have reduced effects when
disbelieved (such as shadow evocation) have their reduced effects increased by 20% (to a maximum of
90%) when determining their effects on targets within the area of shadow invasion.

In addition, the rift created by shadow invasion has a chance of attracting attention from the other
side, and the spell can be inverted to bring these watchers through. When shadow invasion is
dismissed as a standard action, there is a chance that a single evangelist kyton will be summoned
under the caster's command (as per [summon monster V](ref/spell/summon-monster-5)). This chance is
5% for every full round that shadow invasion was active. If the caster level of shadow invasion is
16th or greater, this effect summons an interlocutor kyton instead. A kyton summoned this way
remains for a number of rounds equal to what the remaining duration of shadow invasion would have
been had it not been dismissed. Successfully summoning a kyton this way is a lawful and evil act, as
though casting a spell with the lawful and evil descriptors.

+++
id = "ref/spell/force-anchor"
kind = "spell"
title = "Force Anchor"
aon = "SpellDisplay.aspx?ItemName=Force%20Anchor"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "force_anchor", path = "json/spells13.json" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "26"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a twisted nail)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one anchor of force" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Inquisitor, Magus, Summoner, Unchained Summoner\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a twisted nail)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: yes
Effect: one anchor of force
Subschool: Creation
Descriptors: force
:::

You conjure an anchor of pure force that immediately skewers your target on a successful ranged
touch attack. If it hits, the attack deals the target 1d4 points of force damage per 2 caster levels
(max 5d4) and the anchor becomes firmly lodged in the target's torso. The anchor has no weight, but
its wide flukes prevent the target from moving through any space smaller than the creature's size.
The anchor also prevents incorporeal targets from moving through solid objects. Whenever the target
moves through a square occupied by another creature, the square counts as 2 squares for the purpose
of calculating movement, even if the square's occupant is the target's ally.

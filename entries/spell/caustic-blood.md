+++
id = "ref/spell/caustic-blood"
kind = "spell"
title = "Caustic Blood"
aon = "SpellDisplay.aspx?ItemName=Caustic%20Blood"
source_ids = ["inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "caustic_blood", path = "json/spells2.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "230"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["acid"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (vial of black adder venom)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "Reflex half or negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Bloodrager, Druid, Hunter, Investigator, Magus, Summoner, Unchained Summoner\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (vial of black adder venom)
Range: personal
Duration: 1 round/level
Saving throw: Reflex half or negates, see text
Spell resistance: no
Target: you
Descriptors: acid
:::

You imbue your blood with corrosive acid. Any time you take piercing or slashing damage, a spray of
acidic blood spurts from your body in the direction of the opponent who inflicted the wound, dealing
1d6 points of acid damage per caster level (maximum 15d6, Reflex half). This spurt travels in a
10-foot line, damaging the first creature or object it touches, with no splash damage. After it
contacts a creature or object, your acidic blood continues to burn that creature for 1 round,
dealing 1d6 points of acid damage per 2 caster levels (maximum 7d6). A second successful Reflex save
negates this additional damage.

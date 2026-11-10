+++
id = "ref/spell/baleful-polymorph"
kind = "spell"
title = "Baleful Polymorph"
aon = "SpellDisplay.aspx?ItemName=Baleful%20Polymorph"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "baleful_polymorph", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-3" },
]
[[sources]]
publication = "core-rulebook"
page = "246"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Adept", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Fortitude negates, Will partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner\
5: Adept, Arcanist, Druid, Hunter, Magus, Shaman, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Fortitude negates, Will partial, see text
Spell resistance: yes
Target: one creature
Subschool: Polymorph
:::

As [beast shape III](ref/spell/beast-shape-3), except that you change the subject into a Small or
smaller animal of no more than 1 HD. If the new form would prove fatal to the creature, such as an
aquatic creature not in water, the subject gets a +4 bonus on the save.

If the spell succeeds, the subject must also make a Will save. If this second save fails, the
creature loses its extraordinary, supernatural, and
[spell-like abilities](ref/umr/spell-like-abilities), loses its ability to cast spells (if it had
the ability), and gains the alignment, special abilities, and Intelligence, Wisdom, and Charisma
scores of its new form in place of its own. It still retains its class and level (or HD), as well as
all benefits deriving therefrom (such as base attack bonus, base save bonuses, and hit points). It
retains any class features (other than spellcasting) that aren't extraordinary, supernatural, or
spell-like abilities.

Any polymorph effects on the target are automatically dispelled when a target fails to resist the
effects of baleful polymorph, and as long as baleful polymorph remains in effect, the target cannot
use other polymorph spells or effects to assume a new form. Incorporeal or gaseous creatures are
immune to baleful polymorph, and a creature with the shapechanger subtype can revert to its natural
form as a standard action.

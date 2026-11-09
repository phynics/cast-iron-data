+++
id = "ref/spell/symbol-of-striking"
kind = "spell"
title = "Symbol of Striking"
aon = "SpellDisplay.aspx?ItemName=Symbol%20of%20Striking"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_striking", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]
[[sources]]
publication = "ultimate-combat"
page = "245"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M (a masterwork melee weapon costing at least 300 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "see text"
saving_throw = "Will half, see text"
spell_resistance = "yes, see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Occultist\
5: Arcanist, Cleric, Magus, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (a masterwork melee weapon costing at least 300 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will half, see text
Spell resistance: yes, see text
Effect: one symbol
Subschool: Shadow
:::

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that using the
material component, you scribe a symbol of striking so it fills a 5-foot square. Once triggered, the
symbol of striking glows and lasts for 10 minutes per caster level or until it has made a number of
attacks of opportunity equal to your level, whichever comes first. When triggered, the symbol
threatens its area and the area around it as if it were a Medium creature wielding a magic version
of the weapon you used as the material component. Using your caster level + 1 + your Intelligence
modifier (magus, witch, wizard) or Wisdom modifier (cleric) or Charisma modifier (oracle, sorcerer)
as its attack bonus, the symbol can make a number of attacks of opportunity each round equal to 1 +
the same ability score modifier you used to determine its attack bonus. It gains a bonus on damage
rolls equal to the same ability score modifier you used to determine its attack bonus. A shadowy
version of you wielding the material component appears to make these attacks.

The symbol attacks any non-attuned creature that provokes an attack of opportunity from the symbol.
However, when the symbol first attacks a creature, the symbol must overcome that creature's
[spell resistance](ref/rule/spell-resistance) or be rendered unable to harm it. The symbol never
again attacks such creatures. Further, when the symbol first attacks a creature, a successful Will
saving throw allows the creature to see the shadow nature of the attacks and take half damage when
such attacks hit.

Symbol of striking can be made permanent with a [permanency](ref/spell/permanency) spell by a caster
of 13th level or higher for the cost of 10,000 gp.

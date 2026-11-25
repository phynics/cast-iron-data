+++
id = "ref/spell/undead-anatomy-4"
kind = "spell"
title = "Undead Anatomy IV"
aon = "SpellDisplay.aspx?ItemName=Undead%20Anatomy%20IV"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undead_anatomy_4", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/undead-anatomy-3" },
]
[[sources]]
publication = "ultimate-magic"
page = "245"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["polymorph"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Red Mantis Assassin", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (d) (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (d) (see text)
Saving throw: none
Spell resistance: no
Target: you
Subschool: polymorph
:::

### Undead Anatomy IV

This spell functions as [undead anatomy III](ref/spell/undead-anatomy-3), except it allows you to
use more abilities. If the form you assume has any of the following abilities, you gain the listed
ability: burrow 60 feet, climb 90 feet, fly 120 feet (good maneuverability), swim 120 feet,
[blindsense](ref/rule/blindsight-and-blindsense) 60 feet, [darkvision](ref/rule/darkvision) 90 feet,
lifesense 60 feet, [low-light vision](ref/rule/low-light-vision), scent,
[tremorsense](ref/umr/tremorsense) 60 feet, breath weapon, constrict, DR 10/magic and silver, DR
15/bludgeoning and magic, [fast healing](ref/umr/fast-healing) 5, fiery death, fire aura, grab,
incorporeal, jet, poison, pounce, rake, rend, roar, spikes, trample, trip, and web.

If the creature's form is incorporeal, the spell's duration is in rounds per level instead of
minutes per level, and your bite and claw (or slam) attacks are incorporeal touch attacks. If the
creature has immunity or resistance to any energy types, you gain resistance 30 to those energy
types. If the creature has vulnerability to an energy type, you gain that vulnerability. In this
form, you gain a +8 bonus on saves against mind-affecting effects, disease, poison, sleep, and
stunning. If the form has a vulnerability to an attack (such as sunlight), you gain that
vulnerability.

_Tiny undead:_ If the form you take is that of a Tiny undead, you gain a -2 penalty to your
Strength, a +8 size bonus to your Dexterity, and a +3 natural armor bonus.

_Large undead:_ If the form you take is that of a Large undead, you gain a +6 size bonus to your
Strength, a -2 penalty on your Dexterity, a +2 size bonus to your Constitution, and a +6 natural
armor bonus.

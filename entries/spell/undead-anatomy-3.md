+++
id = "ref/spell/undead-anatomy-3"
kind = "spell"
title = "Undead Anatomy III"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undead_anatomy_3", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/undead-anatomy-2" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Red Mantis Assassin, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

## Undead Anatomy I

**Sources:** Ultimate Magic pg 244

When you cast this spell, you can assume the form of any Small or Medium corporeal creature of the
undead type, which must be vaguely humanoid-shaped (like a ghoul, skeleton, or zombie). You gain a
bite attack (1d6 for Medium forms, 1d4 for Small forms), two claw or slam attacks (1d6 for Medium
forms, 1d4 for Small forms), and [darkvision](ref/rule/darkvision) 60 feet. If the form you assume
has any of the following abilities, you gain the listed ability: climb 30 feet, fly 30 feet (average
maneuverability), swim 30 feet, [low-light vision](ref/rule/low-light-vision), and scent.

In this form, you detect as an undead creature (such as with
[detect undead](ref/spell/detect-undead), but not with magic that reveals your true form, such as
[true seeing](ref/spell/true-seeing)) and are treated as undead for the purposes of channeled
energy, cure spells, and inflict spells, but not for other effects that specifically target or react
differently to undead (such as [searing light](ref/spell/searing-light)).

_Small undead:_ If the form you take is that of a Small undead, you gain a +2 size bonus to your
Dexterity and a +1 natural armor bonus.

_Medium undead:_ If the form you take is that of a Medium undead, you gain a +2 size bonus to your
Strength and a +2 natural armor bonus.

### Undead Anatomy II

**Sources:** Ultimate Magic pg 244

This spell functions as undead anatomy I, except it also allows you to assume the form of a Tiny or
Large corporeal creature of the undead type. If the form you assume has any of the following
abilities, you gain the listed ability: climb 60 feet, fly 60 feet (good maneuverability), swim 60
feet, [darkvision](ref/rule/darkvision) 60 feet, [low-light vision](ref/rule/low-light-vision),
blood drain, DR 5/bludgeoning, scent, freeze, grab, mimicry, pounce, shadowless, sound mimicry, and
trip.

In this form, you gain a +4 bonus on saves against mind-affecting effects, disease, poison, sleep,
and stunning. If the form has a vulnerability to an attack (such as sunlight), you gain that
vulnerability.

_Tiny undead:_ If the form you take is that of a Tiny undead, you gain a +4 size bonus to your
Dexterity, a -2 penalty to your Strength, and a +1 natural armor bonus.

_Large undead:_ If the form you take is that of a Large undead, you gain a +4 size bonus to your
Strength, a -2 penalty to your Dexterity, and a +4 natural armor bonus.

### Undead Anatomy III

**Sources:** Ultimate Magic pg 245

This spell functions as [undead anatomy II](ref/spell/undead-anatomy-2), except it also allows you
to assume the form of a Diminutive or Huge corporeal creature of the undead type. If the form you
assume has any of the following abilities, you gain the listed ability: burrow 30 feet, climb 90
feet, fly 90 feet (good maneuverability), swim 90 feet, all-around vision,
[blindsense](ref/rule/blindsight-and-blindsense) 30 feet, [darkvision](ref/rule/darkvision) 60 feet,
[low-light vision](ref/rule/low-light-vision), scent, constrict, disease, DR 5/-, fear aura, grab,
jet, natural cunning, overwhelming, poison, pounce, rake, trample, trip, unnatural aura, and web.

If the creature has immunity or resistance to any energy types, you gain resistance 20 to those
energy types. If the creature has vulnerability to an energy type, you gain that vulnerability. In
this form, you gain a +8 bonus on saves against mind-affecting effects, disease, poison, sleep, and
stunning. If the form has a vulnerability to an attack (such as sunlight), you gain that
vulnerability.

_Diminutive undead:_ If the form you take is that of a Diminutive undead, you gain a +6 size bonus
to your Dexterity, a -4 penalty to your Strength, and a +1 natural armor bonus.

_Huge undead:_ If the form you take is that of a Huge undead, you gain a +6 size bonus to your
Strength, a -4 penalty to your Dexterity, and a +6 natural armor bonus.

### Undead Anatomy IV

**Sources:** Ultimate Magic pg 245

This spell functions as undead anatomy III, except it allows you to use more abilities. If the form
you assume has any of the following abilities, you gain the listed ability: burrow 60 feet, climb 90
feet, fly 120 feet (good maneuverability), swim 120 feet,
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

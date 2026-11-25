+++
id = "ref/arc-arcanist/blade-adept"
kind = "archetype"
title = "Blade Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20Blade%20Adept"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blade_adept", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "76"

[fields]
kind = "archetype"
features = [
  { anchor = "sword-bond", level = 1 },
  { anchor = "sentient-sword", level = 3 },
  { anchor = "adept-exploits" },
]
trades = [
  { replaces = "The arcanist exploits gained at 1st and 9th levels", feature = "arcanist-exploits", levels = [1, 9], by = ["sword-bond"] },
  { replaces = "The arcanist exploit gained at 3rd level", feature = "arcanist-exploits", levels = [3], by = ["sentient-sword"] },
]
+++

A small number of arcanists learn to use blades as part of their spellcasting and in combat. While
these blade adepts are not as capable with a sword as a true master duelist, their combination of
swordplay and arcane power makes them quite deadly.

## Sword Bond (Su) {#sword-bond}

At 1st level, a blade adept develops a bond with a blade and infuses it with arcane power. This
ability works like a [wizard's](ref/class/wizard) arcane bond ability save that the blade adept must
bond to a one-handed piercing or slashing melee weapon. Additionally, the blade adept gains
proficiency with the weapon if it is a simple or martial weapon. This ability replaces the arcanist
exploits gained at 1st and 9th levels.

## Sentient Sword (Su) {#sentient-sword}

At 3rd level, the blade adept's bonded sword becomes a powerful, sentient
_[black blade](ref/arc-magus/bladebound)_. The blade advances as a _black blade_ using the blade
adept's class level in place of the magus's class level and points from her arcane reservoir in
place of the magus's arcane pool. A blade adept with this class feature cannot have a familiar of
any kind, even from another class. This ability replaces the arcanist exploit gained at 3rd level.

## Adept Exploits {#adept-exploits}

A blade adept can select from the following additional exploits.

### Eldritch Blade {#eldritch-blade}

A blade adept with this exploit uses her caster level instead of her class level for the purpose of
advancing her bonded sword's powers.

### Magus Arcana {#magus-arcana}

A blade adept can select any of the following magus arcana, using her arcane reservoir in place of
the magus's arcane pool: [arcane accuracy](ref/arcana/arcane-accuracy),
[close range](ref/arcana/close-range), [critical strike](ref/arcana/critical-strike),
[dispelling strike](ref/arcana/dispelling-strike), and [hasted assault](ref/arcana/hasted-assault).
The blade adept treats her arcanist level as her magus level when determining the effects of magus
arcana and when specific arcana are available. A blade adept can take this exploit multiple times.
Each time it is taken, it applies to a different magus arcana.

### Spell Strike (Su) {#spell-strike}

The blade adept can deliver touch spells with her bonded weapon. This works as the
[magus](ref/class/magus) ability of the same name.

### Student of the Blade (Ex) {#student-of-the-blade}

A blade adept can choose from any of the following bonus feats:
[Arcane Strike](ref/feat/arcane-strike), [Weapon Finesse](ref/feat/weapon-finesse), and
[Weapon Focus](ref/feat/weapon-focus) (in the weapon she is bonded to). This exploit can be taken
multiple times. Each time it is taken, it applies to a different feat.

### Weapon Specialization (Ex) {#weapon-specialization}

The arcanist gains [Weapon Specialization](ref/feat/weapon-specialization) with her chosen weapon as
a bonus feat. The blade adept does not need to meet the prerequisites for this feat, but must have
the Weapon Focus feat with her chosen weapon to select this exploit. The arcanist must be at least
5th level to select this exploit.

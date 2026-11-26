+++
id = "ref/arc-wizard/spellslinger"
kind = "archetype"
title = "Spellslinger"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Spellslinger"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellslinger", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "ultimate-combat"
page = "75"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-gun", level = 1 },
  { anchor = "gunsmith", level = 1 },
  { anchor = "mage-bullets", level = 1 },
  { anchor = "school-of-the-gun", level = 1 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["arcane-gun"] },
  { replaces = "Scribe scroll", feature = "scribe-scroll", by = ["gunsmith"] },
  { replaces = "Cantrips", feature = "cantrips", by = ["mage-bullets"] },
  { replaces = "Arcane school", feature = "arcane-school", by = ["school-of-the-gun"] },
]
+++

While few contest the seductive allure of commanding arcane and occult powers, there are those
wizards who become obsessed with the natural mysteries of black powder. Combining this emerging
technology with their considerable arcane skills, they transform firearms into a powerful focus.

## Arcane Gun (Su) {#arcane-gun}

The spellslinger gains the [Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency)
(firearms) feat, and one or two of his firearms can be _arcane guns_. _Arcane guns_ are normal
one-handed or two-handed firearms in the hands of others, as they were normal firearms before the
spellslinger imbued them with magic. In a spellslinger's hands, they both fire projectiles (bullets
and pellets) and cast magic. At 1st level, the spellslinger decides whether he wants to have one or
two _arcane guns_ at a time. If the spellslinger chooses to have only one arcane gun at a time,
spells fired through the arcane gun that require an attack roll have a ×3 critical hit multiplier.

A spellslinger can cast any ranged touch attack, cone, line, or ray spells through his _arcane gun_.
When he casts through the _arcane gun_, the gun's enhancement bonus (if any) is a bonus to the
spell's attack rolls or to the spell's saving throw DCs. Yet there are dangers inherent to this
method. If any of the spells' attack rolls result in a natural 1 (a misfire), or a natural 20 is
rolled on any saving throw made against the spell by a target (an overload), the _arcane gun_ gains
the [broken](ref/misc/broken) condition. If the _arcane gun_ already has the broken condition, the
gun explodes. When a gun explodes, it lets loose a blast of force, or if the spell has the acid,
cold, electricity, or sonic descriptor, it deals that type of energy damage instead. In the case of
spells with multiple descriptors, roll randomly among the descriptors to determine the type of
damage dealt by the blast. The blast is centered on a single intersection within the spellslinger's
space (spellslinger's choice) and deals 1d6 points of the appropriate energy damage or force damage
per level of the spell cast. Any creature within the blast other than the spellslinger can make a
Reflex saving throw to halve the damage. The Reflex save DC is calculated using the spell level of
the spell being sacrificed.

A spellslinger can attune his _arcane guns_ at the start of each day. That attunement lasts until
the spellslinger attunes to a new gun, even if a formally attuned gun is destroyed. This ability
replaces arcane bond.

## Gunsmith {#gunsmith}

The spellslinger gains the [Gunsmithing](ref/feat/gunsmithing) feat (see page 103) and a battered
gun that is identical to the gun a [gunslinger](ref/class/gunslinger) (see page 9) gains at first
level. If the spellslinger chooses the ability to attune two arcane guns, he still only starts out
with one gun. Like a gunslinger, a spellslinger can use the Gunsmithing feat to restore his battered
gun. This ability replaces scribe scroll.

## Mage Bullets (Su) {#mage-bullets}

A spellslinger is adept at transferring spell energy into his _arcane gun_ attacks. As a swift
action, he can sacrifice a spell and transform that energy into a weapon bonus equal to the level of
the spell sacrificed on a single barrel of his firearm. With that weapon bonus the spellslinger can
apply any of the following to his arcane bond: enhancement bonuses (up to +5) and
_[dancing](ref/magic-enh/dancing)_, _[defending](ref/magic-enh/defending)_,
_[distance](ref/magic-enh/distance)_, _[flaming](ref/magic-enh/flaming)_,
_[flaming burst](ref/magic-enh/flaming-burst)_, _[frost](ref/magic-enh/frost)_,
_[ghost touch](ref/magic-enh/ghost-touch-weapon)_, _[icy burst](ref/magic-enh/icy-burst)_,
_[merciful](ref/magic-enh/merciful)_, _seeking, shock_,
_[shocking burst](ref/magic-enh/shocking-burst)_, _[spell storing](ref/magic-enh/spell-storing)_,
_[thundering](ref/magic-enh/thundering)_, _[vicious](ref/magic-enh/vicious)_, and
_[wounding](ref/magic-enh/wounding)_. An arcane gun gains no benefit from having two of the same
weapon special abilities on the same barrel. The effect of the mage bullets ability lasts for a
number of minutes equal to the level of the spell sacrificed, or until this ability is used again to
assign the barrel different enhancements. This ability replaces cantrips, but the spellslinger gains
the _[detect magic](ref/spell/detect-magic)_ and _[read magic](ref/spell/read-magic)_ cantrips and
places them in his spellbook. He can cast either of these as 1st-level spells.

## School of the Gun {#school-of-the-gun}

The rigor and care required by arcane guns is so great that a spellslinger forsakes four schools of
magic. These opposition schools are chosen at 1st level and cannot be changed later. A spellslinger
who prepares a spell from his opposition school must use two spell slots of that level to prepare
the spell. In addition, the spellslinger takes a -4 penalty on any skill checks made when crafting a
magic item that has a spell from one of his opposition schools as a prerequisite. This ability
replaces arcane school.

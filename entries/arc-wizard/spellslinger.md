+++
id = "ref/arc-wizard/spellslinger"
kind = "archetype"
title = "Spellslinger"
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
replaces = ["Arcane bond", "Scribe scroll", "Cantrips", "Arcane school"]
replaces_features = ["arcane-bond", "scribe-scroll", "cantrips", "arcane-school"]
+++

While few contest the seductive allure of commanding arcane and occult powers, there are those
wizards who become obsessed with the natural mysteries of black powder. Combining this emerging
technology with their considerable arcane skills, they transform firearms into a powerful focus.

**Arcane Gun (Su)**

**Ability:** The spellslinger gains the
[Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency) (firearms) feat, and one or two of
his firearms can be _arcane guns. Arcane guns_ are normal one-handed or two-handed firearms in the
hands of others, as they were normal firearms before the spellslinger imbued them with magic. In a
spellslinger's hands, they both fire projectiles (bullets and pellets) and cast magic.

**Ability2:** A spellslinger can cast any ranged touch attack, cone, line, or ray spells through his
_arcane gun._ When he casts through the _arcane gun,_ the gun's enhancement bonus (if any) is a
bonus to the spell's attack rolls or to the spell's saving throw DCs.

Yet there are dangers inherent to this method. If any of the spells' attack rolls result in a
natural 1 (a misfire), or a natural 20 is rolled on any saving throw made against the spell by a
target (an overload), the _arcane gun_ gains the [broken](ref/misc/broken) condition. If the _arcane
gun_ already has the broken condition, the gun explodes.

When a gun explodes, it lets loose a blast of force, or if the spell has the acid, cold,
electricity, or sonic descriptor, it deals that type of energy damage instead. In the case of spells
with multiple descriptors, roll randomly among the descriptors to determine the type of damage dealt
by the blast. The blast is centered on a single intersection within the spellslinger's space
(spellslinger's choice) and deals 1d6 points of the appropriate energy damage or force damage per
level of the spell cast. Any creature within the blast other than the spellslinger can make a Reflex
saving throw to halve the damage. The Reflex save DC is calculated using the spell level of the
spell being sacrificed.

**Choice:** At 1st level, the spellslinger decides whether he wants to have one or two _arcane guns_
at a time. If the spellslinger chooses to have only one _arcane gun_ at a time, spells fired through
the _arcane gun_ that require an attack roll have a &times&3 critical hit multiplier.

**Replaces:** Arcane bond

**Special:** A spellslinger can attune his _arcane guns_ at the start of each day. That attunement
lasts until the spellslinger attunes to a new gun, even if a formally attuned gun is destroyed.

**Gunsmith**

**Ability:** The spellslinger gains the [Gunsmithing](ref/feat/gunsmithing) feat and a battered gun
that is identical to the gun a [gunslinger](ref/class/gunslinger) gains at first level.

**Replaces:** Scribe scroll

**Special:** If the spellslinger chooses the ability to attune two _arcane guns,_ he still only
starts out with one gun. Like a gunslinger, a spellslinger can use the Gunsmithing feat to restore
his battered gun.

**Mage Bullets (Su)**

**Ability:** The spellslinger gains the [detect magic](ref/spell/detect-magic) and
[read magic](ref/spell/read-magic) cantrips and places them in his spellbook. He can cast either of
these as 1st-level spells.

**Flavor:** A spellslinger is adept at transferring spell energy into his _arcane gun_ attacks.

**Replaces:** Cantrips

**Special:** An _arcane gun_ gains no benefit from having two of the same weapon special abilities
on the same barrel. The effect of the _mage bullets_ ability lasts for a number of minutes equal to
the level of the spell sacrificed, or until this ability is used again to assign the barrel
different enhancements.

**Swift:** He can sacrifice a spell and transform that energy into a weapon bonus equal to the level
of the spell sacrificed on a single barrel of his firearm. With that weapon bonus the spellslinger
can apply any of the following to his _arcane bond:_ enhancement bonuses (up to +5) and
[dancing](ref/magic-enh/dancing), [defending](ref/magic-enh/defending),
[distance](ref/magic-enh/distance), [flaming](ref/magic-enh/flaming),
[flaming burst](ref/magic-enh/flaming-burst), [frost](ref/magic-enh/frost),
[ghost touch](ref/magic-enh/ghost-touch-weapon), [icy burst](ref/magic-enh/icy-burst),
[merciful](ref/magic-enh/merciful), [seeking](ref/magic-enh/seeking), [shock](ref/magic-enh/shock),
[shocking burst](ref/magic-enh/shocking-burst), [spell storing](ref/magic-enh/spell-storing),
[thundering](ref/magic-enh/thundering), [vicious](ref/magic-enh/vicious), and
[wounding](ref/magic-enh/wounding).

**School of the Gun**

**Info:** The rigor and care required by _arcane guns_ is so great that a spellslinger forsakes four
schools of magic. These opposition schools are chosen at 1st level and cannot be changed later. A
spellslinger who prepares a spell from his opposition school must use two spell slots of that level
to prepare the spell. In addition, the spellslinger takes a -4 penalty on any skill checks made when
crafting a magic item that has a spell from one of his opposition schools as a prerequisite.

**Replaces:** Arcane school

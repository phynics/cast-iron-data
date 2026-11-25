+++
id = "ref/arc-cleric/elder-mythos-cultist"
kind = "archetype"
title = "Elder Mythos Cultist"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Elder%20Mythos%20Cultist"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elder_mythos_cultist", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "horror-adventures"
page = "48"

[fields]
kind = "archetype"
features = [
  { anchor = "deities" },
  { anchor = "domains" },
  { anchor = "forbidden-knowledge" },
  { anchor = "unhinged-mind" },
  { anchor = "channel-the-void", level = 1 },
  { anchor = "maddening-gaze", level = 5 },
  { anchor = "new-domain" },
  { anchor = "void-domain" },
  { anchor = "granted-powers" },
  { anchor = "domain-spells" },
  { anchor = "new-subdomains" },
  { anchor = "dark-tapestry" },
  { anchor = "associated-domain" },
  { anchor = "associated-deities" },
  { anchor = "replacement-power" },
  { anchor = "replacement-domain-spells" },
  { anchor = "isolation" },
  { anchor = "isolation-associated-domain" },
  { anchor = "isolation-associated-deities" },
  { anchor = "isolation-replacement-power" },
  { anchor = "isolation-replacement-domain-spells" },
  { anchor = "stars" },
  { anchor = "stars-associated-domain" },
  { anchor = "stars-associated-deities" },
  { anchor = "stars-replacement-power" },
  { anchor = "stars-replacement-domain-spells" },
]
trades = [
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["channel-the-void"] },
  { replaces = "Increases to channel energy gained at 5th, 11th, and 19th levels", feature = "channel-energy", levels = [5, 11, 19], by = ["maddening-gaze"] },
  { alters = "The cleric's required alignment" },
  { alters = "Domains", feature = "domains", by = ["domains"] },
  { alters = "Channel energy", feature = "channel-energy", by = ["channel-the-void"] },
]
+++

Typically grasping, secretive, and thoroughly mad, Elder Mythos cultists open their bodies and minds
to horrifying realities not meant for the sane as they strive to prepare the world for the eventual
return of their alien masters.

## Alignment {#alignment}

An Elder Mythos cultist must be chaotic evil or chaotic neutral.

This alters the cleric's required alignment.

## Deities {#deities}

An Elder Mythos cultist must worship an Outer God or Great Old One.

## Domains {#domains}

An Elder Mythos cultist receives only a single domain, chosen from the following list: Chaos,
[Madness](ref/domain/madness), or [Void](ref/domain/void). He can choose any subdomain of those
domains offered by an Outer God or Great Old One he worships.

This ability alters domains.

## Forbidden Knowledge (Ex) {#forbidden-knowledge}

An Elder Mythos cultist gains a +2 profane bonus on all Knowledge (arcana), Knowledge
(dungeoneering), Knowledge (history), Knowledge (planes), and Knowledge (religion) checks, and can
attempt these checks untrained. This bonus doubles if the check is related to the Elder Mythos.

## Unhinged Mind (Ex) {#unhinged-mind}

Bartering sanity for unspeakable knowledge, an Elder Mythos cultist props up his crumbling sanity
with a darkly enigmatic personality. An Elder Mythos cultist uses Charisma instead of Wisdom as his
key spellcasting ability score (to determine his spell DCs,
[bonus spells](ref/rule/determine-bonuses) per day, bonus on concentration checks, and so on), to
determine the effects and number of uses of his domain powers, and to modify his Will saving throws.
However, because of the fragile state of his mind, the Elder Mythos cultist takes a -2 penalty on
Will saves to resist mind-affecting effects. An Elder Mythos cultist automatically fails any save to
resist the effects of _[confusion](ref/spell/confusion)_, _[insanity](ref/spell/insanity)_, and
_[nightmare](ref/spell/nightmare)_, and other similar effects so long as the effect's caster level
is higher than his character level.

## Channel the Void (Su) {#channel-the-void}

At 1st level, when an Elder Mythos cultist channels energy, he taps into the unthinkable void
between the stars. This is similar to channeling negative energy, but instead of healing undead,
this blast of energy harms and devours living beings, corporeal non-skeletal undead, and constructs
crafted from flesh (such as [flesh golems](ref/monster/golem-flesh-golem)). This is not negative
energy damage; instead, the damage manifests in the form of wounds from supernatural deterioration
and rot. A creature that would take damage from this energy can attempt a Fortitude save to halve
the damage, rather than a Will save. At 8th level, a creature that both fails the Fortitude save and
would be killed or destroyed by this effect is entirely disintegrated, leaving behind only a trace
of fine dust. A disintegrated creature's equipment is unaffected. This ability still counts as
channel energy, but it counts as neither positive nor negative energy specifically (for example, the
Elder Mythos cultist couldn't take the [Turn Undead](ref/feat/turn-undead) or
[Command Undead](ref/feat/command-undead) feat).

For the purposes of feats that require channel energy but refer to what happens if the character
channels positive or negative energy, this ability alters the listed effect for negative energy. For
instance, an Elder Mythos cultist could use [Channel Smite](ref/feat/channel-smite) to damage living
or fleshy creatures with his melee attack.

This ability alters channel energy and replaces spontaneous casting.

## Maddening Gaze (Su) {#maddening-gaze}

At 5th level, as a standard action, an Elder Mythos cultist can focus his gaze on a single living
creature within 30 feet and inundate the creature's mind with visions of alien horror. The target
takes 2 points of [Wisdom damage](ref/rule/ability-damage-drain) and becomes
[confused](ref/misc/confused) and [sickened](ref/misc/sickened) for 1d4 rounds. A successful Will
save (DC = 10 + 1/2 the Elder Mythos cultist's cleric level + his Charisma modifier) negates the
Wisdom damage and the confusion effect, though the target is sickened for 1 round. This gaze attack
is a mind-affecting effect. An Elder Mythos cultist can use this ability once per day at 5th level,
plus an additional time per day for every 3 cleric levels thereafter.

At 11th level, the target takes 1d6+1 points of Wisdom damage and is confused and sickened for 2d4
rounds. A successful Will save reduces the Wisdom damage to 1 point, and the target is instead
sickened for 1d6 rounds.

At 19th level, the target takes 2d6 points of Wisdom damage and is rendered permanently confused and
sickened. Only _[greater restoration](ref/spell/restoration-greater)_, _[heal](ref/spell/heal)_,
_[limited wish](ref/spell/limited-wish)_, _[miracle](ref/spell/miracle)_, or
_[wish](ref/spell/wish)_ can remove the confused and sickened conditions. A successful Will save
halves the Wisdom damage, and the target is instead sickened for 2d6 rounds.

This ability replaces the increases to channel energy gained at 5th, 11th, and 19th levels.

## NEW DOMAIN {#new-domain}

The following domain is available to followers of Azathoth, Cthulhu, Hastur, Shub-Niggurath, and
Yog-Sothoth, as well as various daemon harbingers. If a domain ability calls for a saving throw, the
DC of the save is equal to 10 + 1/2 the character's cleric level + his Wisdom modifier.

## Void Domain {#void-domain}

## Granted Powers {#granted-powers}

You can call upon the cold darkness between the stars to gain flight, travel to other worlds, or
summon monsters from beyond to do your bidding.

_Guarded Mind (Ex)_: You gain a +2 insight bonus on saving throws against all mind-affecting
effects.

_Part the Veil (Su)_: At 8th level, you can lace spells you cast with the raw madness that waits in
the outer darkness. Activating this ability is a swift action that you must use as you cast a spell
that targets a single creature and allows a Will saving throw to negate or reduce the spell's
primary effect. If the target fails to resist the spell, the target is also confused for a number of
rounds equal to the spell's level as visions of the void cause temporary insanity.

The victim can attempt a new saving throw each round to end the effect—these additional saving
throws apply only to the additional confusion effect and not to the original spell effect. Part the
veil is a mind-affecting effect. You can use this ability a number of times per day equal to 1/2
your class level.

## Domain Spells {#domain-spells}

1st—_feather fall_, 2nd—_levitate_, 3rd—_fly_, 4th—_lesser planar binding_, 5th—_overland flight_,
6th—_planar binding_, 7th—_reverse gravity_, 8th—_greater planar binding_, 9th—_interplanetary
teleport_.

## NEW SUBDOMAINS {#new-subdomains}

The Void domain has the following subdomains. If a subdomain ability calls for a saving throw, the
DC of the save is equal to 10 + 1/2 the character's cleric level + his Wisdom modifier.

## Dark Tapestry {#dark-tapestry}

## Associated Domain {#associated-domain}

Void.

## Associated Deities {#associated-deities}

Azathoth, Cthulhu, Hastur, Shub- Niggurath, Yog-Sothoth.

## Replacement Power {#replacement-power}

The following granted power replaces the guarded mind power of the Void domain.

_It Came from Beyond (Su)_: Once per day, when you cast a summoning spell, any one creature you
summon is more powerful than normal. The creature gains the advanced creature simple template. If
you summon more than one creature with a spell, only one of the summoned creatures gains the
advanced creature simple template. A summoned creature that gains the advanced creature simple
template in this manner appears unnaturally deformed or hideous, bringing with it a whiff of the
emptiness of the void. This ability works only on spells you cast as a cleric—it does not work on
spellcasting abilities gained from any other spellcasting classes you might have.

## Replacement Domain Spells {#replacement-domain-spells}

2nd—_summon monster II_, 5th—_summon monster V_, 7th—_insanity_.

## Isolation {#isolation}

## Associated Domain {#isolation-associated-domain}

Void.

## Associated Deities {#isolation-associated-deities}

Daemon harbingers with the Void domain.

## Replacement Power {#isolation-replacement-power}

The following granted power replaces the part the veil power of the Void domain.

_Aura of Isolation (Su)_: As a standard action, you can create a 20-foot aura that causes enemies
within to be overcome with feelings of isolation and loss. Your enemies treat the aura as difficult
terrain, as they become sluggish within its area of effect. Furthermore, while within the aura, your
enemies cannot provide flanking, nor can they use or benefit from the aid another action. The aura
lasts for a number of rounds equal to 3 + your Wisdom modifier, but the rounds need not be
consecutive. This is a mind-affecting emotion effect.

## Replacement Domain Spells {#isolation-replacement-domain-spells}

4th—_crushing despair_, 6th—_wall of force_, 8th—_prismatic wall_.

## Stars {#stars}

## Associated Domain {#stars-associated-domain}

Void.

## Associated Deities {#stars-associated-deities}

Azathoth, Cthulhu, Hastur, Shub- Niggurath, Yog-Sothoth.

## Replacement Power {#stars-replacement-power}

The following granted power replaces the part the veil power of the Void domain.

_The Stars are Right (Su)_: If you prepare cleric spells while the stars are visible to you, you can
spontaneously cast any of your Stars subdomain spells by swapping out a spell of an equal spell
level. Casting a Stars subdomain spell while the stars are visible to you restores an amount of hit
point damage equal to the spell's level to you; this effect happens as you cast the spell.

## Replacement Domain Spells {#stars-replacement-domain-spells}

2nd—_hypnotic pattern_, 7th—_sunbeam_, 9th—_meteor swarm_.

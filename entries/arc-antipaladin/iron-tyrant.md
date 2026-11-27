+++
id = "ref/arc-antipaladin/iron-tyrant"
kind = "archetype"
title = "Iron Tyrant"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Iron%20Tyrant"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iron_tyrant", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "iron-fist", level = 2 },
  { anchor = "unstoppable", level = 4 },
  { anchor = "fiendish-bond", level = 5 },
]
trades = [
  { replaces = "Touch of corruption", feature = "touch-of-corruption", by = ["iron-fist"] },
  { replaces = "Cruelty", feature = "cruelty" },
  { replaces = "Channel negative energy", feature = "channel-negative-energy", by = ["unstoppable"] },
  { replaces = "Fiendish boon", feature = "fiendish-boon", by = ["fiendish-bond"] },
]
+++

Covered from head to toe in blackened armor decorated with grotesque shapes and bristling with
spikes, iron tyrants make an unmistakable impression on the battlefield. These antipaladins' armor
is an outward symbol of their inner power, and they are rarely seen without it. Iron tyrants seek
the strength to rule over domains as unfettered despots, and depend on their armor as protection
against those they have not yet cowed.

Most iron tyrants are orcs or half-orcs who worship the orc deities [Lanishra](ref/faith/lanishra)
(god of slavery, subjugation, and tyranny) or [Varg](ref/faith/varg) (god of iron, siege weapons,
and warfare). Though rarer, some iron tyrants belong to other races and worship
[Urazra](ref/faith/urazra) (giant god of battle, brutality, and strength) or demon lords such as
[Aldinach](ref/faith/aldinach) (She of the Six Venoms), [Angazhan](ref/faith/angazhan) (the Ravenous
King), or [Izyagna](ref/faith/izyagna) (She of the Sevenfold Swarm).

## Iron Fist (Ex) {#iron-fist}

At 2nd level, an iron tyrant gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a
bonus feat. In addition, whenever the iron tyrant makes a successful attack with a gauntlet, spiked
gauntlet, or armor spikes, the weapon damage is based on his level and not the weapon type, as per
the [warpriest's](ref/class/warpriest) sacred weapon ability (_Pathfinder RPG Advanced Class Guide_
60).

This ability replaces touch of corruption.

## Bonus Feats {#bonus-feats}

At 3rd level and every 3 antipaladin levels thereafter, an iron tyrant gains a bonus feat in
addition to those gained from normal advancement. This feat must be a combat feat that relates to
the iron tyrant's armor or shield, such as [Shield Focus](ref/feat/shield-focus), or one of the
armor mastery feats on page 16.

This ability replaces cruelty.

## Unstoppable (Ex) {#unstoppable}

At 4th level, when wearing heavy armor, an iron tyrant is not slowed by terrain that halves movement
(such as dense rubble, light undergrowth, and shallow bogs). Terrain that has been magically
manipulated to impede motion or terrain that reduces movement by more than half still affects him.

This ability replaces channel negative energy.

## Fiendish Bond (Su) {#fiendish-bond}

At 5th level, instead of forming a fiendish bond with his weapon or a servant, an iron tyrant can
form a bond with his armor. As a standard action, an iron tyrant can enhance his armor by calling
upon a fiendish spirit's aid. This bond lasts for 1 minute per antipaladin level. When called, the
spirit causes the armor to shed unholy light like a [torch](ref/eq-misc/torch). At 5th level, the
spirit grants the armor a +1 enhancement bonus. For every 3 antipaladin levels beyond 5th, the armor
gains another +1 enhancement bonus, to a maximum of +6 at 20th level. These bonuses stack with
existing armor enhancement bonuses to a maximum of +5, or they can be used to add any of the
following armor special abilities: _[dastard](ref/magic-enh/dastard)_,
_[ghost touch](ref/magic-enh/ghost-touch-armor)_, _fortification_ (heavy, light, or medium),
_[invulnerability](ref/magic-enh/invulnerability)_, _[spell resistance](ref/rule/spell-resistance)_
(13, 15, 17, or 19). Adding these special abilities consumes an amount of bonus equal to the special
ability's base price modifier. In addition, the iron tyrant can grant his armor the
_[unrighteous](ref/magic-enh/unrighteous)_ special ability at the cost of a +4 bonus. These special
abilities are added to any special abilities the armor already has, but duplicate abilities do not
stack. If the armor is not magical, at least a +1 enhancement bonus must be added before any other
special abilities can be added. The bonus and special abilities granted by the spirit are determined
when the spirit is called and cannot be changed until the spirit is called again. The fiendish
spirit imparts no bonuses if the armor is worn by anyone other than the iron tyrant, but it resumes
giving bonuses if the iron tyrant dons the armor again. An iron tyrant can use this ability once per
day at 5th level, and one additional time per day for every 4 levels beyond 5th, to a total of four
times per day at 17th level.

If a suit of bonded armor with a fiendish spirit is destroyed, the iron tyrant loses the use of this
ability for 30 days, or until he gains a level, whichever comes first. During this 30-day period,
the iron tyrant takes a -1 penalty on attack rolls and weapon damage rolls.

This ability replaces fiendish boon.

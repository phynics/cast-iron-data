+++
id = "ref/arc-wizard/elder-mythos-scholar"
kind = "archetype"
title = "Elder Mythos Scholar"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Elder%20Mythos%20Scholar"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elder_mythos_scholar", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "horror-adventures"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-bond", level = 1 },
  { anchor = "eldritch-knowledge", level = 1 },
  { anchor = "eldritch-grimoire" },
  { anchor = "talisman-of-revealing", level = 1 },
  { anchor = "eldritch-infusion", level = 8 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["talisman-of-revealing"] },
  { replaces = "the 5th- and 10th-level bonus feats", feature = "bonus-feats", levels = [5, 10], by = ["talisman-of-revealing"] },
  { replaces = "The school ability gained at 8th level", feature = "arcane-school", levels = [8], power = "school powers", by = ["eldritch-infusion"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["arcane-bond"] },
  { alters = "The 1st-level arcane school ability", feature = "arcane-school", levels = [1], power = "school powers", by = ["eldritch-knowledge"] },
  { alters = "Spellbook", feature = "spellbooks", by = ["eldritch-grimoire"] },
]
+++

Elder Mythos scholars risk their sanity to seek knowledge of alien and awful entities from beyond
the stars.

## Arcane Bond {#arcane-bond}

An Elder Mythos scholar must choose to bond with an object, inscribing that object with eldritch
runes.

This alters arcane bond.

## Eldritch Knowledge (Su) {#eldritch-knowledge}

An Elder Mythos scholar gains two fewer daily uses of his 1st-level arcane school ability, which is
normally used a number of times per day equal to 3 + his Intelligence modifier. If he has no such
ability, he can't take this archetype.

When an Elder Mythos scholar attempts a Will save against confusion, fear, insanity, or madness (see
page 12), whether magical or mundane, he can spend 2 daily uses of that arcane school ability to
apply his Intelligence modifier instead of his Wisdom modifier to the save. However, whenever he
uses this ability, he is affected by a _[nightmare](ref/spell/nightmare)_ the next time he sleeps,
with no saving throw. Until he sleeps and experiences the nightmare, he can't recover the spent uses
of the arcane school ability by any means.

This ability alters the 1st-level arcane school ability.

## Eldritch Grimoire {#eldritch-grimoire}

An Elder Mythos scholar keeps copious notes on how to use magic against the servants of the Elder
Mythos in his spellbook. Every spell he adds to his spellbook takes up an additional 1d6 pages and
costs twice the normal amount to inscribe; however, when casting spells prepared from his grimoire,
he gains a +2 bonus on caster level checks and increases the save DCs by 1 against the creatures
listed in talisman of revealing below.

This ability alters spellbook.

## Talisman of Revealing {#talisman-of-revealing}

While wearing or wielding his bonded item, an Elder Mythos scholar can spontaneously cast a special
_[detect aberration](ref/spell/detect-aberration)_ spell by sacrificing a prepared 1st-level spell.
Instead of detecting aberrations, this spell detects creatures associated with the Elder Mythos,
such as the following (or similar creatures, at the GM's discretion): [bhole](ref/monster/bhole),
[colour out of space](ref/monster/colour-out-of-space), [deep one](ref/monster/deep-one), deep one
elder, [denizen of Leng](ref/monster/denizen-of-leng), [elder thing](ref/monster/elder-thing),
[flying polyp](ref/monster/flying-polyp), [gug](ref/monster/gug),
[hound of Tindalos](ref/monster/hound-of-tindalos), [Leng ghoul](ref/monster/ghoul-leng-ghoul),
[Leng spider](ref/monster/leng-spider), [mi-go](ref/monster/mi-go),
[nightgaunt](ref/monster/nightgaunt), [ratling](ref/monster/ratling),
[shantak](ref/monster/shantak), [shoggoth](ref/monster/shoggoth),
[spawn of Yog-Sothoth](ref/monster/spawn-of-yog-sothoth),
[star-spawn of Cthulhu](ref/monster/star-spawn-of-cthulhu), [voonith](ref/monster/voonith),
[wendigo](ref/monster/wendigo), and [yithian](ref/monster/yithian). He gains a +2 circumstance bonus
on Knowledge checks to identify such creatures and Spellcraft checks to identify effects they
create.

At 5th level, an Elder Mythos scholar adds _[invisibility purge](ref/spell/invisibility-purge)_ and
_[see invisibility](ref/spell/see-invisibility)_ to his spellbook and can spontaneously cast either
spell by sacrificing a prepared spell of the same or higher level while wearing or wielding his
bonded item. At 10th level, he adds _[banish seeming](ref/spell/banish-seeming)_ and
_[true seeing](ref/spell/true-seeing)_ to his spellbook as 5th-level spells and can spontaneously
cast them in the same fashion.

This replaces Scribe Scroll and the 5th- and 10th-level bonus feats.

## Eldritch Infusion (Su) {#eldritch-infusion}

At 8th level, once each day while preparing spells, an Elder Mythos scholar can spend 1 extra hour
to brew a tincture of hallucinogens and alien trace minerals. Though it has no effect for others, if
he drinks it, the elixir expands his mind and perceptions into transitive dimensions, granting him a
+4 alchemical bonus to his Intelligence score and reducing his Wisdom and Constitution scores by 2
for 10 minutes per wizard level he has. While under the effects of this elixir, he adds 1/2 his
class level to his Perception checks against aberrations and creatures listed in talisman of
revealing, but subtracts the same amount from all other Perception checks. His spells have a 20%
failure chance, unless they summon, call, or contact a creature listed in talisman of revealing or
otherwise affect only such creatures (for instance, a _[fireball](ref/spell/fireball)_ aimed at 3
gugs but not a _fireball_ aimed at 3 gugs and a gnome).

This ability replaces the school ability gained at 8th level.

+++
id = "ref/arc-monk/black-asp"
kind = "archetype"
title = "Black Asp"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Black%20Asp"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "black_asp", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "67"

[fields]
kind = "archetype"
features = [
  { anchor = "black-asp-s-path", level = 1 },
  { anchor = "forbidden-powers" },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["black-asp-s-path"] },
  { replaces = "still mind", feature = "still-mind", by = ["black-asp-s-path"] },
]
+++

The black asps are a sinister order of monks who train as assassins and infiltrators with no need
for weapons to achieve their goals. Through meditation and study, they learn how to use poison, hide
any magics they choose to employ, and even empty their minds of thought to protect themselves from
divinations.

## Black Asp's Path (Ex) {#black-asp-s-path}

A black asp is trained in the use of poison and cannot accidentally poison himself when applying
poison to a weapon or when rolling a natural 1 on an attack roll with a poisoned weapon. At 3rd
level, the black asp's ability to use poison improves. He gains
[Adder Strike](ref/feat/adder-strike) as a bonus feat even if he does not meet the prerequisites.

This ability replaces stunning fist and still mind.

## Forbidden Powers (Su) {#forbidden-powers}

A black asp can select a forbidden ki power in place of any of the following monk class abilities
(or as a ki power if he is an unchained monk): slow fall (4th), high jump (5th), wholeness of body
(7th), diamond body (11th), abundant step (12th), diamond soul (13th), quivering palm (15th), tongue
of the sun and moon (17th), and empty body (19th). If he chooses to do so, he replaces the monk
class ability the black asp gives up for the chosen forbidden ki power. The black asp can select any
of the following forbidden ki powers.

### Black Asp Venom (Su) {#black-asp-venom}

As a swift action, a black asp with this ki power can [poison](ref/spell/poison) his unarmed strike
or a weapon in his hand. The poison lasts for 1 minute or until expended. A creature damaged by the
poisoned weapon is affected as per the _poison_ spell. The save DC is equal to 10 + 1/2 the black
asp's monk level + his Wisdom modifier. Each use of this ability costs 2 ki points. A black asp must
be at least 12th level before selecting this ki power.

### Empty Mind (Sp) {#empty-mind}

A black asp with this ki power can choose to lower the number of ki points in his ki pool by 3 when
he recovers his ki points for the day. If he does so, he gains the benefits of
_[mind blank](ref/spell/mind-blank)_ for 24 hours. A black asp must be at least 16th level and
possess the greater hidden magic ki power before selecting this ki power.

### Greater Hidden Magic (Sp) {#greater-hidden-magic}

As long as he has at least 1 point in his ki pool, all of the black asp's items are constantly under
the effects of _[magic aura](ref/spell/magic-aura)_. As an immediate action, he can spend 2 ki
points to cause himself and any magic items he is carrying to appear to be nonmagical (as if he had
cast _[greater magic aura](ref/spell/magic-aura-greater)_; see page 219) for 1 hour per monk level.
A black asp must be at least 8th level and possess the hidden magic ki power before selecting this
ki power.

### Hidden Magic (Sp) {#hidden-magic}

As an immediate action, the black asp can spend 1 ki point to hide the auras of all magic items he
is carrying (as if they were all under _[magic aura](ref/spell/magic-aura)_) for 1 hour per monk
level.

### Shifting Form (Su) {#shifting-form}

As an immediate action, a black asp can spend 1 ki point to make his outline shift and waver for 1
round. This ability otherwise functions as per the spell _[blur](ref/spell/blur)_.

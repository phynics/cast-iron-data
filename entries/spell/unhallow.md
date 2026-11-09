+++
id = "ref/spell/unhallow"
kind = "spell"
title = "Unhallow"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unhallow", path = "json/spells11.json" },
]
[[sources]]
publication = "core-rulebook"
page = "363"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "24 hours"
components = "V, S, M (herbs, oils, and incense worth at least 1,000 gp, plus 1,000 gp per level of the spell to be tied to the unhallowed area)"
range = "touch"
effects = [
  { label = "Area", value = "40-ft. radius emanating from the touched point" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Cleric, Druid, Hunter, Inquisitor, Oracle, Warpriest
Casting time: 24 hours
Components: V, S, M (herbs, oils, and incense worth at least 1,000 gp, plus 1,000 gp per level of the spell to be tied to the unhallowed area)
Range: touch
Duration: instantaneous
Saving throw: see text
Spell resistance: see text
Area: 40-ft. radius emanating from the touched point
Descriptors: evil
:::

Unhallow makes a particular site, building, or structure an unholy site. This has three major
effects.

First, the site or structure is guarded by a
[magic circle against good](ref/spell/magic-circle-against-good) effect.

Second, the DC to resist negative channeled energy within the spell's area of effect gains a +4
sacred bonus and the DC to resist positive energy is reduced by 4.
[Spell resistance](ref/rule/spell-resistance) does not apply to this effect. This provision does not
apply to the druid version of the spell.

Finally, you may choose to fix a single spell effect to the unhallowed site. The spell effect lasts
for 1 year and functions throughout the entire site, regardless of its normal duration and area or
effect. You may designate whether the effect applies to all creatures, creatures that share your
faith or alignment, or creatures that adhere to another faith or alignment. At the end of the year,
the chosen effect lapses, but it can be renewed or replaced simply by casting unhallow again.

Spell effects that may be tied to an unhallowed site include [aid](ref/spell/aid),
[bane](ref/spell/bane), [bless](ref/spell/bless), [cause fear](ref/spell/cause-fear),
[darkness](ref/spell/darkness), [daylight](ref/spell/daylight), [death ward](ref/spell/death-ward),
[detect good](ref/spell/detect-good), [deeper darkness](ref/spell/deeper-darkness),
[detect magic](ref/spell/detect-magic), [dimensional anchor](ref/spell/dimensional-anchor),
[discern lies](ref/spell/discern-lies), [dispel magic](ref/spell/dispel-magic),
[endure elements](ref/spell/endure-elements), [freedom of movement](ref/spell/freedom-of-movement),
[invisibility purge](ref/spell/invisibility-purge),
[protection from energy](ref/spell/protection-from-energy), [remove fear](ref/spell/remove-fear),
[resist energy](ref/spell/resist-energy), [silence](ref/spell/silence),
[tongues](ref/spell/tongues), and [zone of truth](ref/spell/zone-of-truth).

Saving throws and [spell resistance](ref/rule/spell-resistance) might apply to these spells'
effects. (See the individual spell descriptions for details.)

An area can receive only one unhallow spell (and its associated spell effect) at a time.

Unhallow counters but does not dispel [hallow](ref/spell/hallow).

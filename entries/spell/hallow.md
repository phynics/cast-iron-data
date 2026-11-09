+++
id = "ref/spell/hallow"
kind = "spell"
title = "Hallow"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hallow", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "293"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "24 hours"
components = "V, S, DF, M (herbs, oils, and incense worth at least 1,000 gp, plus 1,000 gp per level of he spell to be included in the hallowed area)"
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
Components: V, S, DF, M (herbs, oils, and incense worth at least 1,000 gp, plus 1,000 gp per level of he spell to be included in the hallowed area)
Range: touch
Duration: instantaneous
Saving throw: see text
Spell resistance: see text
Area: 40-ft. radius emanating from the touched point
Descriptors: good
:::

Hallow makes a particular site, building, or structure a holy site. This has four major effects.

First, the site is warded by a [magic circle against evil](ref/spell/magic-circle-against-evil)
effect.

Second, the DC to resist positive channeled energy within this area gains a +4 sacred bonus and the
DC to resist negative energy is reduced by 4. [Spell resistance](ref/rule/spell-resistance) does not
apply to this effect. This provision does not apply to the druid version of the spell.

Third, any dead body interred in a hallowed site cannot be turned into an undead creature.

Finally, you can fix a single spell effect to the hallowed site. The spell effect lasts for 1 year
and functions throughout the entire site, regardless of the normal duration and area or effect. You
may designate whether the effect applies to all creatures, creatures who share your faith or
alignment, or creatures who adhere to another faith or alignment. At the end of the year, the chosen
effect lapses, but it can be renewed or replaced simply by casting hallow again.

Spell effects that may be tied to a hallowed site include [aid](ref/spell/aid),
[bane](ref/spell/bane), [bless](ref/spell/bless), [cause fear](ref/spell/cause-fear),
[darkness](ref/spell/darkness), [daylight](ref/spell/daylight), [death ward](ref/spell/death-ward),
[deeper darkness](ref/spell/deeper-darkness), [detect evil](ref/spell/detect-evil),
[detect magic](ref/spell/detect-magic), [dimensional anchor](ref/spell/dimensional-anchor),
[discern lies](ref/spell/discern-lies), [dispel magic](ref/spell/dispel-magic),
[endure elements](ref/spell/endure-elements), [freedom of movement](ref/spell/freedom-of-movement),
[invisibility purge](ref/spell/invisibility-purge),
[protection from energy](ref/spell/protection-from-energy), [remove fear](ref/spell/remove-fear),
[resist energy](ref/spell/resist-energy), [silence](ref/spell/silence),
[tongues](ref/spell/tongues), and [zone of truth](ref/spell/zone-of-truth). Saving throws and
[spell resistance](ref/rule/spell-resistance) might apply to these spells' effects. (See the
individual spell descriptions for details.)

An area can receive only one hallow spell (and its associated spell effect) at a time. Hallow
counters but does not dispel [unhallow](ref/spell/unhallow).

+++
id = "ref/spell/planar-ally"
kind = "spell"
title = "Planar Ally"
source_ids = ["core-rulebook", "adventurers-guide", "arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_ally", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Calling"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 500 gp plus payment, see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one called outsider of 6 HD or less" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 3: Medium\
4: Cleric, Oracle, Psychic, Shaman, Warpriest
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 500 gp plus payment, see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one called outsider of 6 HD or less
Subschool: Calling
:::

## Lesser Planar Ally

**Sources:** PRPG Core Rulebook pg 320

By casting this spell, you request your deity to send you an outsider (of 6 HD or less) of the
deity's choice. If you serve no particular deity, the spell is a general plea answered by a creature
sharing your philosophical alignment. If you know an individual creature's name, you may request
that individual by speaking the name during the spell (though you might get a different creature
anyway).

You may ask the creature to perform one task in exchange for a payment from you. Tasks might range
from the simple to the complex. You must be able to communicate with the creature called in order to
bargain for its services.

The creature called requires a payment for its services. This payment can take a variety of forms,
from donating gold or magic items to an allied temple, to a gift given directly to the creature, to
some other action on your part that matches the creature's alignment and goals. Regardless, this
payment must be made before the creature agrees to perform any services. The bargaining takes at
least 1 round, so any actions by the creature begin in the round after it arrives.

A task taking up to 1 minute per caster level requires a payment of 100 gp per HD of the creature
called. For a task taking up to 1 hour per caster level, the creature requires a payment of 500 gp
per HD. A long-term task, one requiring up to 1 day per caster level, requires a payment of 1,000 gp
per HD.

A non-hazardous task requires only half the indicated payment, while an especially hazardous task
might require a greater gift. Few if any creatures will accept a task that seems suicidal (remember,
a called creature actually dies when it is killed, unlike a summoned creature). However, if the task
is strongly aligned with the creature's ethos, it may halve or even waive the payment.

At the end of its task, or when the duration bargained for expires, the creature returns to its home
plane (after reporting back to you, if appropriate and possible).

_Note:_ When you use a calling spell that calls an air, chaotic, earth, evil, fire, good, lawful, or
water creature, it is a spell of that type.

### Planar Ally

**Sources:** PRPG Core Rulebook pg 320

This spell functions like lesser planar ally, except you may call a single creature of 12 HD or
less, or two creatures of the same kind whose HD total no more than 12. The creatures agree to help
you and request your return payment together.

### Greater Planar Ally

**Sources:** PRPG Core Rulebook pg 320

This spell functions like lesser planar ally, except that you may call a single creature of 18 HD or
less, or up to three creatures of the same kind whose Hit Dice total no more than 18. The creatures
agree to help you and request your return payment together.

### Planar Inquiry

**Sources:** Adventurer's Guide pg 125, Arcane Anthology pg 14

Although he was hardly the first to turn to the Outer Planes for answers, Jatembe's dealings with
outsiders in his pursuit of enlightenment are legendary, and the Magaambya credits the Old-Mage with
the creation of this spell.

This spell calls a creature from another plane to your precise location, functioning like
_[lesser planar ally](ref/spell/planar-ally-lesser)_ except as noted. When you call a creature using
_[planar inquiry](ref/spell/planar-inquiry),_ the only task that you can ask of the creature is for
it to answer questions or gather information regarding a specific topic (a person, a place, or a
thing). After hearing your request, if the creature has an appropriate Knowledge skill, it can
attempt a check to provide the information it has. If it lacks such a skill, the called creature
leaves for 1d4 hours to gather this information. Upon its return, you roll 1d20 + your caster level,
and use the result to determine what information the creature has gathered about the subject (as if
using Diplomacy). The called creature stays for up to 10 minutes as it relays this information to
you, after which it departs to its home plane. If the creature is attacked or damaged at any time
during the spell's duration, the spell ends and the creature returns to the plane from which you
summoned it.

When you cast this spell, you can choose a specific kind of outsider to call, even calling an
individual creature by name. The kind of outsider called doesn't alter the effects of the spell, but
when you use planar inquiry to summon a creature with an alignment or elemental subtype, the spell
gains that descriptor. You cannot call an outsider whose Hit Dice exceed your caster level (maximum
18 HD) and you cannot use this spell to contact a unique outsider (such as a deity's herald) or an
outsider with mythic ranks.

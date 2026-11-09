+++
id = "ref/spell/recorporeal-incarnation"
kind = "spell"
title = "Recorporeal Incarnation"
source_ids = ["inner-sea-intrigue", "pathfinder-16-endless-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "recorporeal_incarnation", path = "json/spells8.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "61"
[[sources]]
publication = "pathfinder-16-endless-night"
page = "10"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, F (a gem worth at least 250 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one willing living creature and one humanoid corpse" },
]
duration = "1 week/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (a gem worth at least 250 gp)
Range: touch
Duration: 1 week/level
Saving throw: none
Spell resistance: no
Target: one willing living creature and one humanoid corpse
:::

Recorporeal incarnation effectively replaces the target living creature's body with that of the
target corpse. The target corpse must be fresh - either dead for no more than 24 hours or
appropriately preserved by an effect such as gentle repose. While casting the spell, you must remain
in contact with the corpse while touching the living target with the focus item. As the spell is
cast, the dead body's flesh unravels like ribbons to sheathe the living target, who must be within
one size category of the corpse. While the spell is in effect, the focus item must remain within 30
feet of the target living creature.

The living target gains the physical appearance and size of the corpse, and gains its abilities as
defined in alter self as well as any immunities, weapon proficiencies, weaknesses, and
[spell resistance](ref/rule/spell-resistance) the dead target had while living. The living target
gains a +20 circumstance bonus on Disguise checks to impersonate the individual whose corpse is
targeted by this spell. The disguise created by recorporeal incarnation lasts for a number of weeks
equal to your caster level, or until the focus item is moved more than 30 feet away from the living
target. When the effect ends, the living target returns to its normal form, sloughing off the
corpse's flesh.

The greatest strength of recorporeal incarnation is the difficulty of detecting it as a disguise. If
subjected to detect magic, the living target sheds no magical aura, though the focus item gives off
an aura of strong necromantic magic. True seeing does not reveal the living target's true form,
since the corpse's flesh magically obscures it. The spell detect undead and similar effects indicate
the living target is an undead creature, but the target is not truly undead, and is not affected by
any other effects that target undead creatures. Recorporeal incarnation does not disguise the
target's alignment.

If the living target of recorporeal incarnation dies while the spell is in effect, the spell
continues. Any [raise dead](ref/spell/raise-dead) or similar spell cast upon that target resurrects
that target, not the corpse flesh. Since recorporeal incarnation destroys the majority of the target
corpse's physical remains, the target corpse cannot be restored to life except by
[miracle](ref/spell/miracle), [resurrection](ref/spell/resurrection),
[true resurrection](ref/spell/true-resurrection), or [wish](ref/spell/wish). Recorporeal incarnation
can be made permanent by a 15th-level caster using [permanency](ref/spell/permanency) with a
material component worth 17,500 gp.

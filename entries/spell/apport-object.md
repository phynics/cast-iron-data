+++
id = "ref/spell/apport-object"
kind = "spell"
title = "Apport Object"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "apport_object", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "one touched object of up to 1 lb. and 1 cu. ft." },
]
duration = "instantaneous or 1 hour/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: instantaneous or 1 hour/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one touched object of up to 1 lb. and 1 cu. ft.
Subschool: Teleportation
:::

**Sources:** Occult Adventures pg 157

This spell allows you to instantaneously transport a small nonliving object from one location to
another. There are two ways to use the spell: sending allows you to immediately send an object held
in your hands to a nearby location, while receiving permits you to cast the spell ahead of time on
an object and summon it to your location at a later time.

_Sending:_ If you choose to send the object elsewhere, the spell functions like teleport object,
except the size of the object is limited and the distance it can travel is equal to only 25 feet + 5
feet per 2 levels. You can't transport an object to the Ethereal Plane. You can send the held object
to any square within range, and you don't need line of sight to the target location. You can place
the object in the open or inside a container, a pocket, or even someone's hand. If there isn't room
in the space you select (either because the space chosen is too small or because there is already
something else there), or if the person doesn't want or isn't expecting the object in his hands, it
appears on the ground within the target's square instead. You can transport the object to an
elevation above the floor as long as the destination is within the spell's total distance limit.

_Receiving:_ You can prepare an object ahead of time to apport it to yourself by casting the spell
upon it and assigning a mental trigger to complete the spell. You don't need line of sight to the
object to apport it to you, but the object must be within a distance equal to 25 feet + 5 feet per 2
levels. Completing the spell is a swift action that has the same restrictions as a thought spell
component. You can apport an object in this way even if someone holding the object is unwilling to
let you take it. Once you apport the object, the spell ends.

You can't send or receive an object into a space that is protected by an
[antimagic field](ref/spell/antimagic-field),
[globe of invulnerability](ref/spell/globe-of-invulnerability), or similar effect that keeps magical
effects out; if you attempt to do so, the spell is lost.

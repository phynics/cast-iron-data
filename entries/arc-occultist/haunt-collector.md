+++
id = "ref/arc-occultist/haunt-collector"
kind = "archetype"
title = "Haunt Collector"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "haunt_collector", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "horror-adventures"
page = "62"

[fields]
kind = "archetype"
replaces = ["Aura sight", "Outside contact", "Magic circles", "binding circles", "fast circles"]
alters = ["Implements"]
replaces_features = ["aura-sight", "outside-contact", "magic-circles", "binding-circles", "fast-circles"]
alters_features = ["implements"]
+++

Haunt collectors use items haunted by their former owners to create ghostly presences imbued with
psychic power.

**Possessed Possessions (Su)**

**Ability:** When he selects a haunted implement, he forsakes the resonant power from the item's
implement group and instead selects a spirit from the [medium's](ref/class/medium) list of
[spirits](ref/ability/spirits), gaining that spirit's _seance boon_ in place of the resonant power.
Once the spirit type is selected for an implement, it cannot be changed.

**Alters:** Implements

**Choice:** When the haunt collector chooses an implement school he doesn't already know, instead of
using implements as normal for that school, he can gain access to a haunted implement - a powerful,
spirit-possessed item collected during his travels.

**Gained:** At 2nd Level

**Repeat:** The haunt collector may either learn a new implement school or a choose a new haunted
implement., 6, 4

**Swift:** He can also call upon the implement's haunting entity to temporarily gain bonuses on all
checks associated with the selected legendary spirit's spirit bonus for 1 round. This spirit bonus
is equal to 1/2 the amount of mental focus invested in the implement, to a maximum bonus of 1 +
[one-fourth](ref/misc/fractions-and-rounding) of his occultist level. He can call upon this spirit
bonus a number of times per day equal to the amount of mental focus invested in the implement,
though invoking it doesn't expend any mental focus.

**Hauntist (Su)**

**Ability:** A haunt collector with at least one haunted implement gains the medium's _haunt
channeler_ class feature, with an effective medium level equal to his occultist level - 2.

**Gained:** At 5th Level

**Replaces:** Aura sight

**Haunt Channeler (Su)**

**Ability:** Your touch funnels a portion of the haunt into yourself, dealing 1d6 points of damage
to the haunt per 2 medium levels you possess as if via positive energy and allowing you to ask the
haunt a single question. The haunt can answer the question however it chooses.

**Ability2:** Additionally, you can forgo your saving throw against a haunt's effects to funnel the
haunt entirely into yourself. If you do so, you suffer the haunt's full effect, but the haunt
doesn't affect anyone else (even if it normally would). The haunt then gains control of your body
for 24 hours. Once per minute, you can attempt to end this possession early by succeeding at a Will
save (DC = 20 + 1/2 your medium level).

**Flavor:** Text from the medium class

**Passive:** You can always act on the surprise round against a haunt.

**Spirit Speaker (Sp)**

**Ability:** A haunt collector with at least one haunted implement can commune with the spirits once
per day. By holding a seance for 10 minutes, he can ask questions of a destroyed undead or a
neutralized or destroyed haunt. To use this ability on a corporeal undead, the haunt collector must
have the creature's head in his possession. For a haunt or incorporeal undead, this seance must be
held in the haunt's location or where the incorporeal undead was destroyed. Treat this ability as
[speak with haunt](ref/spell/speak-with-haunt) or as [speak with dead](ref/spell/speak-with-dead)
(but affecting only destroyed undead rather than only corpses), using the haunt collector's
occultist level as the caster level.

**At 12th Level:** He can use this ability twice a day.

**At 16th Level:** He may use this ability three times a day.

**Gained:** At 8th Level

**Replaces:** Outside contact

**Extricate Haunt (Su)**

**Action:** Ability

**At 12th Level:** The haunt collector can create a free-roaming haunt by expending an additional
point of mental focus, granting it a fly speed of 10 feet with good maneuverability, which allows it
to change locations or seek targets, under the restrictions for trigger conditions as outlined
above. If the haunt wanders beyond [medium range](ref/rule/range) (measured from the haunt
collector's current position), it is instantly destroyed.

**At 16th Level:** The haunt collector can extricate an implement's spirit as a **standard action**.

**Replaces:** Magic circles, binding circles, fast circles

**Special:** While a haunting presence is extricated from its implement, the haunt collector does
not receive the benefit of the implement's _seance boon,_ nor can he call upon the implement's
spirit bonus or use its focus powers, though he can still cast spells associated with the implement
without penalty. If the spell is discharged successfully (rather than the haunt being destroyed),
the spirit's presence returns to the haunt collector's implement the following round, and the
_seance boon_ and spirit bonus abilities are again available to the haunt collector.

**Usage:** Intelligence1 modifier times/day

The haunt collector can temporarily exorcise his haunted implements' possessing entities to
spontaneously create phenomena similar to [haunts](ref/rule/haunts) and imbue them with spells the
occultist knows. As a **full-round action** that provokes attacks of opportunity, the haunt
collector expends 1 point of mental focus to extricate an implement's spirit and infuse an adjacent
square with its ghostly presence while granting it the power to deliver a spell from the implement's
associated school (whose range is touch or greater) on the haunt collector's behalf. This action
consumes the spell just as if it had been cast, but the energy is held in check by the created haunt
until triggered by conditions set forth by the haunt collector. The conditions needed to trigger the
haunt's spell effect must be clear, although they can be general, using the guidelines of the
[magic mouth](ref/spell/magic-mouth) spell. The haunt is stationary, and once the conditions for the
trigger are met, the spell is discharged normally, though it now originates from the haunt's square.

The haunt itself is an invisible, incorporeal, spectral force, similar to a stationary
[unseen servant](ref/spell/unseen-servant) with an undead aura for the purposes of spells such as
[detect undead](ref/spell/detect-undead). It has a number of hit points equal to the double the
level of the spell used to create it + the occultist's Intelligence modifier. If triggered during
the same combat it is created, the haunt acts at initiative count 10; otherwise, when the trigger
occurs, the haunt initiates combat and acts at initiative count 10 on the surprise round. Other
creatures must succeed at a Perception check (DC = 10 + the haunt collector's occultist level) to
act in the surprise round. The haunt can be damaged by positive energy and anything else that can
harm haunts, and if destroyed before it is triggered, it dissipates harmlessly. If the haunt is
destroyed, it does not reform in its haunted implement until the occultist next invests his
implements with mental focus. If the haunt doesn't trigger before the occultist next invests his
implements with mental focus, the haunt dissolves at that point and reforms in its haunted
implement.

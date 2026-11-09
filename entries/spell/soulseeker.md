+++
id = "ref/spell/soulseeker"
kind = "spell"
title = "Soulseeker"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soulseeker", path = "json/spells9.json" },
]
[[sources]]
publication = "planar-adventures"
page = "44"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 8 },
]
casting_time = "1 hour"
components = "V, S, M (incense worth 250 gp), F (see text)"
range = "unlimited"
effects = [
  { label = "Target", value = "one soul" },
]
duration = "instantaneous or 1 hour/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Medium\
6: Occultist, Spiritualist\
8: Cleric, Oracle, Shaman, Witch
Casting time: 1 hour
Components: V, S, M (incense worth 250 gp), F (see text)
Range: unlimited
Duration: instantaneous or 1 hour/level
Saving throw: Will negates
Spell resistance: no
Target: one soul
:::

You identify the stage of a given soul's judgment, or determine its fate post-judgment. You must
either unambiguously identify the soul you seek or use the skull of the body the soul vacated as a
focus. If the subject does not share your alignment, the soul can attempt a Will save to resist this
spell's effects as if it were still alive. If the subject is still alive or its soul has been
destroyed, this spell fails without providing any information.

If the soul has not yet been judged and moved on to its final reward or punishment, soulseeker
provides an estimate of its location; in most cases, this is somewhere in the River of Souls or the
Boneyard. While this may assist in physically traveling to the soul's location, especially in cases
involving effects such as soul bind or a devourer's devour soul ability, the spell's primary purpose
is to identify how long the subject has been dead (and what form of life-restoring magic is
necessary). If the soul has already been judged, soulseeker instead identifies the plane to which
the soul has been sent as a petitioner and the petitioner's general location on that plane (such as
"Elysium, beneath the boughs of the Witchwood").

If soulseeker is cast on the same plane on which the soul's new petitioner form currently exists, it
guides you along the shortest, most direct physical route to the petitioner, as described in find
the path. In this case, the spell's duration is 1 hour per level.

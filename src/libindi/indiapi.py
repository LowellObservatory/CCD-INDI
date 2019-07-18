""" Define constants and data structures used for INDI Property Definitions.
    Based on the indiapi.h definitions (version 1.7) by Elwood C. Downey.
"""

from enum import Enum

# Switch state.
ISState = Enum('ISState', 'ISS_OFF ISS_ON')

# Property State.
IPState = Enum('IPState', 'ISP_IDLE ISP_OK IPS_BUSY IPS_ALERT')

# Switch vector rule hint.
# ISR_1OFMANY: Only 1 switch of many can be ON (e.g. radio buttons)
# ISR_ATMOST1: At most one switch can be ON, but all switches can be off.
#     Similar to ISR_1OFMANY with the exception that all switches can be off.
# ISR_NOFMANY: Any number of switches can be ON (e.g. check boxes)
ISRule = Enum('ISRule', 'ISR_1OFMANY ISR_ATMOST1 ISR_NOFMANY')

# Permission hint, with respect to client.
# RO: Read Only
# WO: Write Only
# RW: Read & Write
IPerm = Enum('IPerm', 'IP_RO IP_WO IP_RW')

# IText structure
# One text descriptor.
class IText():
    def __init__(self, name, label, text, tvp, aux0, aux1):
        self.name  = name   # Index Name  (string)
        self.label = label  # Short Description (string)
        self.text  = text   # Allocated text string (string)
        self.tvp   = tvp    # Pointer to Parent (ITextVectorProperty)
        self.aux0  = aux0   # Helper info (None)
        self.aux1  = aux1   # Helper info (None)

# ITextVectorProperty structure
# Text vector property descriptor.
class ITextVectorProperty():
    def __init__(self, device, name, label, group, p, timeout, s, tp,
                 ntp, timestamp, aux):
        self.device    = device     # Device name (string)
        self.name      = name       # Property name (string)
        self.label     = label      # Short description (string)
        self.group     = group      # GUI grouping hint (string)
        self.p         = p          # Client sccessibility hint (IPerm)
        self.timeout   = timeout    # Current max time to change, secs (double)
        self.s         = s          # Current property state (IPState)
        self.tp        = tp         # Texts comprising this vector (IText[])
        self.ntp       = ntp        # Dimension of tp[] (int)
        self.timestamp = timestamp  # ISO 8601 timestamp of this event (string)
        self.aux       = aux        # Helper info (None)
        
# INumber.format may be any printf-style appropriate for double
# or style "m" to create sexigesimal using the form "%<w>.<f>m" where
#   <w> is the total field width.
#   <f> is the width of the fraction. valid values are:
#      9  ->  :mm:ss.ss
#      8  ->  :mm:ss.s
#      6  ->  :mm:ss
#      5  ->  :mm.m
#      3  ->  :mm
#
# examples:
#
#   to produce     use
#
#    "-123:45"    %7.3m
#  "  0:01:02"    %9.6m

# INumber structure
# One number descriptor.
class INumber():
    def __init__(self, name, label, format, min, max, setp, value, nvp,
                 aux0, aux1):
        self.name   = name   # Index Name  (string)
        self.label  = label  # Number label (string)
        self.format = text   # GUI display format string (string)
        self.min    = min    # Range min, ignored if min == max (double)
        self.max    = max    # Range max, ignored if min == max (double)
        self.step   = step   # Step size, ignored if step == 0 (double)
        self.value  = value  # Current value (double)
        self.tvp    = nvp    # Pointer to Parent (INumberVectorProperty)
        self.aux0   = aux0   # Helper info (None)
        self.aux1   = aux1   # Helper info (None)
        
# INumberVectorProperty structure
# Number vector property descriptor.
class INumberVectorProperty():
    def __init__(self, device, name, label, group, p, timeout, s, np,
                 nnp, timestamp, aux):
        self.device    = device     # Device name (string)
        self.name      = name       # Property name (string)
        self.label     = label      # Short description (string)
        self.group     = group      # GUI grouping hint (string)
        self.p         = p          # Client sccessibility hint (IPerm)
        self.timeout   = timeout    # Current max time to change, secs (double)
        self.s         = s          # Current property state (IPState)
        self.np        = np         # Numbers comprising this vector (INumber[])
        self.nnp       = nnp        # Dimension of np[] (int)
        self.timestamp = timestamp  # ISO 8601 timestamp of this event (string)
        self.aux       = aux        # Helper info (None)
        
# ISwitch structure
# One switch descriptor.
class ISwitch():
    def __init__(self, name, label, s, svp, aux):
        self.name  = name   # Index Name  (string)
        self.label = label  # Switch Label (string)
        self.s     = s      # Switch state (ISState)
        self.svp   = svp    # Pointer to Parent (ISwitchVectorProperty)
        self.aux   = aux    # Helper info (None)
        
# ISwitchVectorProperty structure
# Switch vector property descriptor.
class ISwitchVectorProperty():
    def __init__(self, device, name, label, group, p, r, timeout, s, sp,
                 nsp, timestamp, aux):
        self.device    = device     # Device name (string)
        self.name      = name       # Property name (string)
        self.label     = label      # Short description (string)
        self.group     = group      # GUI grouping hint (string)
        self.p         = p          # Client sccessibility hint (IPerm)
        self.r         = r          # Switch behavior hint. (ISRule)
        self.timeout   = timeout    # Current max time to change, secs (double)
        self.s         = s          # Current property state (IPState)
        self.sp        = sp         # Switches comprising this vector (ISwitch[])
        self.nsp       = nsp        # Dimension of sp[] (int)
        self.timestamp = timestamp  # ISO 8601 timestamp of this event (string)
        self.aux       = aux        # Helper info (None)
        
# ILight structure
# One light descriptor.
class ILight():
    def __init__(self, name, label, s, lvp, aux):
        self.name  = name   # Index Name  (string)
        self.label = label  # Light label (string)
        self.s     = s      # Switch state (IPState)
        self.lvp   = lvp    # Pointer to Parent (ILightVectorProperty)
        self.aux   = aux    # Helper info (None)
        
# ILightVectorProperty structure
# Light vector property descriptor.
class ILightVectorProperty():
    def __init__(self, device, name, label, group, p, r, timeout, s, lp,
                 nlp, timestamp, aux):
        self.device    = device     # Device name (string)
        self.name      = name       # Property name (string)
        self.label     = label      # Short description (string)
        self.group     = group      # GUI grouping hint (string)
        self.s         = s          # Current property state (IPState)
        self.lp        = lp         # Lights comprising this vector (ILight[])
        self.nlp       = nlp        # Dimension of lp[] (int)
        self.timestamp = timestamp  # ISO 8601 timestamp of this event (string)
        self.aux       = aux        # Helper info (None)
        
# IBLOB structure
# One Blob (Binary Large Object) descriptor.
class IBLOB():
    def __init__(self, name, label, format, blob, bloblen, size, bvp,
                 aux0, aux1, aux2):
        self.name     = name    # Index Name  (string)
        self.label    = label   # BLOB label (string)
        self.format   = format  # Format attr (string)
        self.blob     = blob    # Allocated binary large object bytes (None)
        self.bloblen  = bloblen # Blob size in bytes (int)
        self.size     = size    # N uncompressed bytes (int)
        self.bvp      = bvp     # Pointer to parent (IBLOBVectorProperty)
        self.aux0     = aux0    # Helper info (None)
        self.aux1     = aux1    # Helper info (None)
        self.aux2     = aux2    # Helper info (None)
        
# IBLOBVectorProperty structure
# BLOB (Binary Large Object) vector property descriptor.
class IBLOBVectorProperty():
    def __init__(self, device, name, label, group, p, r, timeout, s, lp,
                 nlp, timestamp, aux):
        self.device    = device     # Device name (string)
        self.name      = name       # Property name (string)
        self.label     = label      # Short description (string)
        self.group     = group      # GUI grouping hint (string)
        self.s         = s          # Current property state (IPState)
        self.lp        = lp         # BLOBs comprising this vector (ILight[])
        self.nlp       = nlp        # Dimension of lp[] (int)
        self.timestamp = timestamp  # ISO 8601 timestamp of this event (string)
        self.aux       = aux        # Helper info (None)